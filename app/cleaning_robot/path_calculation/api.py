import time
from datetime import datetime
from flask import request, make_response

from app.cleaning_robot.database import session_context
from app.cleaning_robot.path_calculation.models import PathCalculationExecution
from app.cleaning_robot.path_calculation.robot_cleaning_simulator import (
    RobotCleaningSimulator,
)


def post_path_calculation():
    """
    Given a path, the endpoint will calculate uniquely visited
    points. The service will report the results back to the
    requester as a response.
    """
    robot_path = request.json
    path_calculation = PathCalculationExecution(
        timestamp=datetime.now(),
        commands=len(robot_path["commands"]),
        result=0,
        duration=0,
    )

    start = time.time()
    robot_cleaning_simulator = RobotCleaningSimulator(path=robot_path)
    places = robot_cleaning_simulator.get_unique_places()
    end = time.time()
    path_calculation.result = places
    path_calculation.duration = end - start

    with session_context() as session:
        session.add(path_calculation)
        session.commit()

        return make_response(path_calculation.as_dict(), 201)

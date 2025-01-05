import time
from app.cleaning_robot.path_calculation.robot_cleaning_simulator import (
    RobotCleaningSimulator,
)


class TestRobotCleaningSimilator:
    def test_load_max_grid_of_full_rows(self, memory_load_max_grid_rows):
        simulator = RobotCleaningSimulator(memory_load_max_grid_rows)
        start = time.time()
        result = simulator.get_unique_places()
        end = time.time()
        assert end - start < 1
        assert result == 200_001 * 2 * 2_500 + 1

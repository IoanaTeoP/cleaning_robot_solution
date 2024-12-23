import time
from app.cleaning_robot.path_calculation.robot_cleaning_simulator import RobotCleaningSimulator


class TestRobotCleaningSimilator:
    def test_memory_load_full_grid(self, memory_load_robot_path):
        simulator = RobotCleaningSimulator(memory_load_robot_path)
        start = time.time()
        result = simulator.get_unique_places()
        end = time.time()
        duration = '{:.6f}'.format(end-start)
        assert result
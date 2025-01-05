import pytest
from app.cleaning_robot.path_calculation.robot_cleaning_simulator import (
    RobotCleaningSimulator,
)
from app.cleaning_robot.path_calculation.grid_helpers import PlaceOnGrid


class TestRobotCleaningSimilator:
    def test_should_compute_simple_path(self, simple_robot_path):
        simulator = RobotCleaningSimulator(simple_robot_path)
        assert simulator.get_unique_places() == 4
        assert simulator.current_place == PlaceOnGrid(x=12, y=23)

    def test_should_compute_path_with_negative_integers(
        self, with_negative_integers_robot_path
    ):
        simulator = RobotCleaningSimulator(with_negative_integers_robot_path)
        result = simulator.get_unique_places()
        assert result == 301
        assert simulator.current_place == PlaceOnGrid(x=0, y=0)

    def test_should_compute_path_with_zero_steps(self, with_zero_steps_robot_path):
        simulator = RobotCleaningSimulator(with_zero_steps_robot_path)
        result = simulator.get_unique_places()
        assert result == 1
        assert simulator.current_place == PlaceOnGrid(x=-100, y=-200)

    def test_should_compute_path_with_loop(self, with_loop_robot_path):
        simulator = RobotCleaningSimulator(with_loop_robot_path)
        result = simulator.get_unique_places()
        assert result == 4
        assert simulator.current_place == PlaceOnGrid(x=10, y=50)

    @pytest.mark.parametrize(
        "x,y,commands",
        [
            (-100_000, 0, [{"direction": "west", "steps": 10}]),
            (100_000, 0, [{"direction": "east", "steps": 11}]),
            (9, -100_000, [{"direction": "south", "steps": 12}]),
            (9, 100_000, [{"direction": "north", "steps": 199}]),
        ],
    )
    def test_out_of_bounds_should_be_stationary(self, x, y, commands):
        """Robot not outside of the office case"""
        stationary_point = PlaceOnGrid(x=x, y=y)
        path = {"start": {"x": x, "y": y}, "commands": commands}
        simulator = RobotCleaningSimulator(path)
        result = simulator.get_unique_places()
        assert result == 1
        assert simulator.current_place == stationary_point

    @pytest.mark.parametrize(
        "x,y,commands",
        [
            (0, 0, [{"direction": "west", "steps": 0}]),
            (0, 0, [{"direction": "north", "steps": 0}]),
            (0, 0, [{}]),
        ],
    )
    def test_no_commands_should_be_stationary(self, x, y, commands):
        path = {
            "start": {"x": 0, "y": 0},
            "commands": [{"direction": "west", "steps": 0}],
        }
        simulator = RobotCleaningSimulator(path)
        result = simulator.get_unique_places()
        assert result == 1
        assert simulator.current_place == PlaceOnGrid(0, 0)

    def test_should_compute_a_complex_robot_path(self, one_complex_robot_path):
        simulator = RobotCleaningSimulator(one_complex_robot_path)
        result = simulator.get_unique_places()
        assert result == 14
        assert simulator.current_place == PlaceOnGrid(x=3, y=1)

    def test_snake_robot_path(self, snake_robot_path_on_rows):
        simulator = RobotCleaningSimulator(snake_robot_path_on_rows)
        result = simulator.get_unique_places()
        assert result == 12
        assert simulator.current_place == PlaceOnGrid(x=-1, y=2)

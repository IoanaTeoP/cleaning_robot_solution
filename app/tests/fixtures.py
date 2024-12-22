import pytest


@pytest.fixture
def simple_robot_path():
    return {
        "start": {"x": 10, "y": 22},
        "commands": [
            {"direction": "east", "steps": 2},
            {"direction": "north", "steps": 2},
        ],
    }

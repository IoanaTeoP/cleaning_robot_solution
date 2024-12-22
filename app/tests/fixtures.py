import pytest


@pytest.fixture
def simple_robot_path():
    return {"start": {"x": 0, "y": 0}, "commands": [{"direction": "east", "steps": 1}]}

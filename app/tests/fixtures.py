import pytest


@pytest.fixture
def simple_robot_path():
    return {
        "start": {"x": 10, "y": 22},
        "commands": [
            {"direction": "east", "steps": 2},
            {"direction": "north", "steps": 1},
        ],
    }


@pytest.fixture
def with_negative_integers_robot_path():
    return {
        "start": {"x": -100, "y": -200},
        "commands": [
            {"direction": "east", "steps": 100},
            {"direction": "north", "steps": 200},
        ],
    }


@pytest.fixture
def with_zero_steps_robot_path():
    return {
        "start": {"x": -100, "y": -200},
        "commands": [
            {"direction": "east", "steps": 0},
            {"direction": "north", "steps": 0},
            {"direction": "south", "steps": 0},
            {"direction": "west", "steps": 0},
        ],
    }


@pytest.fixture
def with_loop_robot_path():
    loop = [
        {"direction": "east", "steps": 1},
        {"direction": "north", "steps": 1},
        {"direction": "west", "steps": 1},
        {"direction": "south", "steps": 1},
    ]
    return {
        "start": {"x": 10, "y": 50},
        "commands": loop*100
    }


@pytest.fixture
def one_complex_robot_path():
    return {
        "start": {"x": 1, "y": 2},
        "commands": [
        {"direction": "east", "steps": 1},
        {"direction": "south", "steps": 3},
        {"direction": "west", "steps": 2},
        {"direction": "south", "steps": 1},
        {"direction": "east", "steps": 1},
        {"direction": "north", "steps": 1},
        {"direction": "west", "steps": 1},
        {"direction": "north", "steps": 2},
        {"direction": "west", "steps": 1},
        {"direction": "east", "steps": 4},
        ]
    }


@pytest.fixture
def memory_load_robot_path():
    two_rows_path = [
        {"direction": "east", "steps": 200_000},
        {"direction": "north", "steps": 1},
        {"direction": "west", "steps": 200_000},
        {"direction": "north", "steps": 1},
    ]
    return {
        "start": {"x": -100_000, "y": -100_00},
        "commands": two_rows_path * 10,
    }

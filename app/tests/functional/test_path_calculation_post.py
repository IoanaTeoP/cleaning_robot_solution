from app.cleaning_robot.path_calculation.models import PathCalculationExecution
class TestPathCalculationPOST:
    BASE_URL = "/tibber-developer-test/enter-path"

    def test_success_returns_201_status(self, client, simple_robot_path, db_session):
        response = client.post(self.BASE_URL, json=simple_robot_path)
        assert response.status_code == 201
        response_json = response.json()
        assert response_json["commands"] == 2
        assert response_json["result"] == 4
        assert response_json["id"]
        assert response_json["duration"]
        assert response_json["timestamp"]
        stored_object = db_session.query(PathCalculationExecution).scalar()
        assert stored_object.commands == 2
        assert stored_object.result == 4
        assert stored_object.id
        assert stored_object.duration < 1
        assert stored_object.timestamp

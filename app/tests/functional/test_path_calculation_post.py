class TestPathCalculationPOST:
    BASE_URL = "/api/tibber-developer-test/enter-path"

    def test_success_returns_201_status(self, client, simple_robot_path, db_session):
        response = client.post(self.BASE_URL, json=simple_robot_path)
        assert response.status_code == 201
        response_json = response.json()
        assert response_json["id"]
        assert response_json["commands"] == 2
        assert response_json["duration"]
        assert response_json["timestamp"]

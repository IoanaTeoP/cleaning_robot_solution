class TestPathCalculationPOST:
    BASE_URL = "/api/path_calculation"

    def test_success_returns_201_status(
        self,
        client,
        simple_robot_path
    ):
        response = client.post(self.BASE_URL, json=simple_robot_path)
        assert response.status_code == 201

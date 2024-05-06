import unittest

from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case.case_response import (
    CaseResponse,
)


class TestCaseResponse(unittest.TestCase):
    def test_success_response(self):
        response_data = {
            "_id": "123",
            "title": "Test Title",
            "description": "Test Description",
            # ... adicione outros atributos conforme necessário ...
        }
        response = CaseResponse(200, response_data)

        # Verifique se os atributos estão corretos
        assert response.status_code == 200
        assert response._id == "123"
        assert response.title == "Test Title"
        assert response.description == "Test Description"
        assert response.is_success()
        assert str(response) == "Case: Test Title - Test Description"

    def test_missing_attributes(self):
        response_data = {}
        response = CaseResponse(200, response_data)

        # Verifique se os atributos que não estão presentes no response_data estão None
        assert response._id is None
        assert response.title is None
        assert response.description is None
        assert response.is_success()

    def test_str_representation(self):
        response_data = {
            "_id": "123",
            "title": "Test Title",
            "description": "Test Description",
            "type": "Test Error Type",
            "message": "Test Error Message",
        }
        success_response = CaseResponse(200, response_data)
        error_response = CaseResponse(400, response_data)

        # Verifique a representação de string
        assert str(success_response) == "Case: Test Title - Test Description"
        assert str(error_response) == "Error (400): Test Error Type - Test Error Message"


if __name__ == "__main__":
    unittest.main()

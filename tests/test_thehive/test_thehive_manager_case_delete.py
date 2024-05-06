import unittest
from unittest.mock import Mock

from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case.delete_case import (
    DeleteCase,
)
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_session import (
    SessionThehive,
)


class TestDeleteCase(unittest.TestCase):
    def setUp(self):
        # Create a mock SessionThehive object
        self.mock_session = Mock(spec=SessionThehive)

        # Create an instance of DeleteCase with the mocked session
        self.delete_case = DeleteCase(session=self.mock_session)

    def test_delete_case_success(self):
        # Set up the mock to return a successful response
        self.mock_session.request.return_value = ("Success", 200)

        # Call the delete_case method
        response, status_code = self.delete_case.delete_case("test_case_id")

        # Assertions
        self.assertEqual(status_code, 200)
        self.assertEqual(response, "Success")
        self.mock_session.request.assert_called_once_with(
            endpoint="v1/case/test_case_id", method="DELETE"
        )

    def test_delete_case_failure(self):
        # Set up the mock to return a failure response
        self.mock_session.request.return_value = ("Not Found", 404)

        # Call the delete_case method
        response, status_code = self.delete_case.delete_case("nonexistent_case_id")

        # Assertions
        self.assertEqual(status_code, 404)
        self.assertEqual(response, "Not Found")
        self.mock_session.request.assert_called_once_with(
            endpoint="v1/case/nonexistent_case_id", method="DELETE"
        )


if __name__ == "__main__":
    unittest.main()

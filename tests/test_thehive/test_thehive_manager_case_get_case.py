import unittest
from unittest.mock import Mock

from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case.get_case import (
    GetCase,
)
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_session import (
    SessionThehive,
)


class TestGetCase(unittest.TestCase):
    def setUp(self):
        # Create a Mock object for SessionThehive class
        self.mock_session = Mock(spec=SessionThehive)

        # Create an object of GetCase with mock_session
        self.get_case = GetCase(session=self.mock_session)

    def test_fetch_case_with_id(self):
        # Arrange
        case_id = "1234"
        expected_response = ({"data": "some_data"}, 200)  # Replace with what you expect

        # Setting up the mock object to return the expected response
        self.mock_session.request.return_value = expected_response

        # Act
        actual_response = self.get_case.fetch_case(id_or_name=case_id)

        # Assert
        assert actual_response == expected_response
        self.mock_session.request.assert_called_once_with(endpoint=f"v1/case/{case_id}")

    def test_fetch_case_with_name(self):
        # You can create a similar test case if name can also be used to fetch case details.
        pass


if __name__ == "__main__":
    unittest.main()

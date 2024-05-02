import unittest
from unittest.mock import Mock

from requests.exceptions import RequestException

from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case.list_case import (
    ListCase,
)
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_session import (
    SessionThehive,
)


class TestListCase(unittest.TestCase):
    def setUp(self):
        self.mock_session = Mock(spec=SessionThehive)
        self.list_case = ListCase(session=self.mock_session)

    def test_list_cases_success(self):
        # Arrange
        expected_response = ([{"id": "1", "name": "case1"}], 200)

        # Setting up the mock object to return the expected response
        self.mock_session.request.return_value = expected_response

        # Act
        actual_response, actual_status = self.list_case.list_cases()

        # Assert
        assert actual_response == expected_response[0]
        assert actual_status == expected_response[1]
        self.mock_session.request.assert_called_once_with(endpoint="case")

    def test_list_cases_failure(self):
        # Arrange
        error_message = "Some Error Occurred"

        # Setting up the mock object to raise an exception
        self.mock_session.request.side_effect = RequestException(error_message)

        # Act
        actual_response, actual_status = self.list_case.list_cases()

        # Assert
        assert actual_response is None
        assert actual_status == f"Error in request: {error_message}"


if __name__ == "__main__":
    unittest.main()

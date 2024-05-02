import unittest
from unittest.mock import Mock, create_autospec

import pytest
from typeguard import TypeCheckError

from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_datatype import (
    CaseDataType,
)
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case.create_case import (
    CreateCase,
)
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_session import (
    SessionThehive,
)


class TestCreateCase(unittest.TestCase):
    def setUp(self):
        # Cria um objeto Mock para SessionThehive que passará pela verificação isinstance
        self.session_mock = create_autospec(SessionThehive)

        # Inicializa CreateCase com o objeto Mock
        self.create_case = CreateCase(session=self.session_mock)

    def test_init(self):
        with pytest.raises(TypeCheckError):
            CreateCase(
                session="Invalid Session"
            )  # Passando uma string em vez de um objeto SessionThehive

    def test_check_case_exist(self):
        # Configura o objeto Mock para retornar uma resposta esperada
        self.session_mock.request.return_value = ([{"title": "Existing Case"}], 200)
        assert self.create_case._check_case_exist("Existing Case")
        assert not self.create_case._check_case_exist("Non-Existing Case")

    def test_validate_string_length(self):
        with pytest.raises(ValueError):
            self.create_case._validate_string_length("test", 5, 10, "test_string")

        self.create_case._validate_string_length("valid_string", 5, 20, "test_string")

    def test_validate_in_list(self):
        with pytest.raises(ValueError):
            self.create_case._validate_in_list("invalid", ["valid"], "test_value")

        self.create_case._validate_in_list("valid", ["valid"], "test_value")

    def test_create_case(self):
        case_data_mock = Mock(spec=CaseDataType)
        case_data_mock.title = "Valid Title"
        case_data_mock.description = "Valid Description"
        case_data_mock.severity = 2
        case_data_mock.tlp = 2
        case_data_mock.pap = 1
        case_data_mock.status = "Open"
        case_data_mock.tags = ["Open"]
        case_data_mock.customFields = {"a": ""}
        case_data_mock.stats = {"a": ""}

        # Configura o objeto Mock para retornar False ao verificar a existência do caso
        self.create_case._check_case_exist = Mock(return_value=False)

        self.session_mock.request.return_value = ({"success": True}, 200)

        response, status_code = self.create_case.create(case_data_mock)
        assert response == {"success": True}
        assert status_code == 200

        self.create_case._check_case_exist.return_value = True
        response = self.create_case.create(case_data_mock)
        assert response == "A case with the same title already exists"

    def test_validate_inputs(self):
        valid_case_data_mock = Mock(spec=CaseDataType)
        valid_case_data_mock.title = "Valid Title"
        valid_case_data_mock.description = "Valid Description"
        valid_case_data_mock.severity = 2
        valid_case_data_mock.tlp = 2
        valid_case_data_mock.pap = 1
        valid_case_data_mock.status = "Open"

        self.create_case._validate_inputs(valid_case_data_mock)

        invalid_case_data_mock = Mock(spec=CaseDataType)
        invalid_case_data_mock.title = "Invalid Title" * 100  # String muito longa
        with pytest.raises(ValueError):
            self.create_case._validate_inputs(invalid_case_data_mock)


if __name__ == "__main__":
    unittest.main()

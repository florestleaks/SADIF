import unittest
from unittest.mock import MagicMock

from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_alert import (
    Alert,
)
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_session import (
    SessionThehive,
)


class TestAlert(unittest.TestCase):
    def setUp(self):
        self.session_mock = MagicMock(spec=SessionThehive)
        self.alert = Alert(session=self.session_mock)

    def test_create(self):
        # Definindo alguns valores para os parâmetros
        alert_type = "TestType"
        source = "TestSource"
        sourceRef = "TestSourceRef"
        title = "TestTitle"
        description = "TestDescription"

        # Chame o método create com os valores definidos
        self.alert.create(
            alert_type=alert_type,
            source=source,
            sourceRef=sourceRef,
            title=title,
            description=description,
        )

        # Verifica se session.create_alert foi chamado com os parâmetros corretos
        self.session_mock.create_alert.assert_called_once_with(
            {
                "type": alert_type,
                "source": source,
                "sourceRef": sourceRef,
                "title": title,
                "description": description,
            }
        )


if __name__ == "__main__":
    unittest.main()

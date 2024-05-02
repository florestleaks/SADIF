import unittest
from unittest.mock import MagicMock

from sadif.frameworks_drivers.web.authenticator.basic_auth_strategy import BasicAuthStrategy
from sadif.frameworks_drivers.web.authenticator.bearer_auth_strategy import BearerAuthStrategy
from sadif.frameworks_drivers.web.authenticator.digest_auth_strategy import DigestAuthStrategy
from sadif.frameworks_drivers.web.session_manager import SessionManager


class TestSessionManager(unittest.TestCase):
    def test_create_session_with_basic_auth(self):
        mock_auth_strategy = MagicMock(spec=BasicAuthStrategy)
        manager = SessionManager()

        manager.create_session(mock_auth_strategy)

        # Verifique se o método authenticate foi chamado no mock da estratégia de autenticação
        mock_auth_strategy.authenticate.assert_called_once()

    def test_create_session_with_bearer_auth(self):
        mock_auth_strategy = MagicMock(spec=BearerAuthStrategy)
        manager = SessionManager()

        manager.create_session(mock_auth_strategy)

        # Verifique se o método authenticate foi chamado no mock da estratégia de autenticação
        mock_auth_strategy.authenticate.assert_called_once()

    def test_create_session_with_digest_auth(self):
        mock_auth_strategy = MagicMock(spec=DigestAuthStrategy)
        manager = SessionManager()

        manager.create_session(mock_auth_strategy)

        # Verifique se o método authenticate foi chamado no mock da estratégia de autenticação
        mock_auth_strategy.authenticate.assert_called_once()


if __name__ == "__main__":
    unittest.main()

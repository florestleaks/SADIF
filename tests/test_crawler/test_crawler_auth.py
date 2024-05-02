import unittest

from requests import Session
from requests.auth import HTTPDigestAuth

from sadif.frameworks_drivers.web.authenticator.basic_auth_strategy import BasicAuthStrategy
from sadif.frameworks_drivers.web.authenticator.bearer_auth_strategy import BearerAuthStrategy
from sadif.frameworks_drivers.web.authenticator.digest_auth_strategy import DigestAuthStrategy


class TestAuthStrategies(unittest.TestCase):
    def test_basic_auth_strategy(self):
        username = "user"
        password = "pass"  # noqa: S105
        auth_strategy = BasicAuthStrategy(username, password)

        session = Session()
        authenticated_session = auth_strategy.authenticate(session)

        self.assertEqual(authenticated_session.auth, (username, password))

    def test_bearer_auth_strategy(self):
        token = "sometoken"  # noqa: S105
        auth_strategy = BearerAuthStrategy(token)

        session = Session()
        authenticated_session = auth_strategy.authenticate(session)

        self.assertIn("Authorization", authenticated_session.headers)
        self.assertEqual(authenticated_session.headers["Authorization"], f"Bearer {token}")

    def test_digest_auth_strategy(self):
        username = "user"
        password = "pass"  # noqa: S105
        auth_strategy = DigestAuthStrategy(username, password)

        session = Session()
        authenticated_session = auth_strategy.authenticate(session)

        self.assertIsInstance(authenticated_session.auth, HTTPDigestAuth)

import unittest

from mongomock import MongoClient as MockMongoClient

from sadif.clientmanager.client_data_manager import ClientManager


class TestClientManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initial setup for all tests
        cls.mock_client = MockMongoClient()
        cls.client_manager = ClientManager(db_client=cls.mock_client)

    def test_update_module_info_not_allowed_module(self):
        """Test updating module info with a module name that is not allowed."""
        result = self.client_manager.update_module_info(
            "TestClient", "NotAllowedModule", {"info": "test"}
        )
        self.assertIn("Erro: Módulo 'NotAllowedModule' não é permitido.", result)

    # Add more tests for other methods...


if __name__ == "__main__":
    unittest.main()

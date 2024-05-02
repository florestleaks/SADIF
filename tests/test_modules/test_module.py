import unittest

import mongomock

from sadif.frameworks_drivers.modules_manager import ModuleDatabaseManager


class TestModuleDatabaseManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configuração inicial para todos os testes
        cls.mock_client = mongomock.MongoClient()
        cls.module_manager = ModuleDatabaseManager(db_client=cls.mock_client)

    def setUp(self):
        # Configuração antes de cada teste
        self.mock_client.drop_database("test_module")  # Limpar a base de dados antes de cada teste
        self.module_manager.db = self.mock_client[
            "test_module"
        ]  # Definir uma base de dados de teste

    def test_create_module_collection(self):
        # Test the creation of a module collection
        self.module_manager.create_module_collection("test_module", {"type": "object"})

        # Insert a dummy document to ensure the collection is created in mongomock
        self.module_manager.insert_document("test_module", {"dummy": "data"})

        # Verify if the collection was created successfully
        self.assertIn("module_test_module", self.module_manager.db.list_collection_names())

    def test_insert_document(self):
        # Testar a inserção de um documento
        document = {"name": "test_document", "value": 42}
        inserted_id = self.module_manager.insert_document("test_module", document)

        # Verificar se o documento foi inserido com sucesso
        self.assertIsNotNone(inserted_id)

        # Verificar se o documento pode ser encontrado na coleção
        inserted_document = self.module_manager.db["module_test_module"].find_one(
            {"name": "test_document"}
        )
        self.assertIsNotNone(inserted_document)


if __name__ == "__main__":
    unittest.main()

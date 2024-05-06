from pymongo import MongoClient
from soar.clientmanager.client_data_manager import ClientManager
from soar.utils.generete_string.random_string_generator import RandomStringGenerator

if __name__ == "__main__":
    randstr = RandomStringGenerator()
    db_real = MongoClient("")
    # Criar uma instância de ClientManager usando o mock_client
    manager = ClientManager(db_client=db_real)
    for i in range(10):
        print(
            manager.create_client_collection(
                f"{randstr.generate_string_title('caju').split()[4]}",
                "TODO",
                "TODO",
                overwrite=True,
            )
        )

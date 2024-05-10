from pymongo import MongoClient
from soar.clientmanager.client_data_manager import ClientManager
from soar.utils.generete_string.random_string_generator import RandomStringGenerator

if __name__ == "__main__":
    randstr = RandomStringGenerator()
    db_real = MongoClient(
        ""
    )
    # Criar uma instância de ClientManager usando o mock_client
    manager = ClientManager(db_client=db_real)
    # for i in client_sample:

    #    print(manager.create_client_collection(f"{i}", "TODO", 'TODO',overwrite=True))
    # lis = manager.list_all_clients()

    # manager.export_to_json('CLIENT_MONITORING')
    # manager.import_from_json(import_path=False, overwrite=True)
    # print(lis)
    # module_info = {
    #    "ativação": "2024-01-01",
    #    "versão": "1.0",
    #    "configurações": {"opção1": True, "opção2": "algum valor"},
    # }
    # print(manager.update_module_info("12345", "ModuloB", module_info))
    ## Buscar todas as informações dos módulos do cliente
    # modules_info = manager.find_client_modules("12345")
    # print("Todas as informações dos módulos:", modules_info)
#
## Acessar informações de um módulo específico, por exemplo, "ModuloA"
# modulo_a_info = modules_info.get("ModuloA")
# print("Informações do ModuloA:", modulo_a_info)
## Atualizando um módulo permitido
# print(
#    manager.update_module_info("12345", "ModuloA", {"configuração": "valor"})
# )  # Deve funcionar

# Tentando atualizar um módulo não permitido
# print(manager.update_module_info("12345", "ModuloNaoPermitido", {"configuração": "valor"}))  # Deve retornar erro
# print(manager.delete_client_collection('12345'))

from sadif.config.soar_config import SadifConfiguration
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case.update_case import (
    UpdateCase,
)
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_session import (
    SessionThehive,
)
from sadif.utils.generete_string.markdown_string_generator import MarkdownStringGenerator
from sadif.utils.generete_string.random_string_generator import RandomStringGenerator

if __name__ == "__main__":
    md_generator = MarkdownStringGenerator()
    markdown_document = md_generator.generate_markdown_document("Exemplo de Evento", 3, 5, 10)

    generator = RandomStringGenerator()
    config = SadifConfiguration()

    thehive_url = config.get_configuration("THEHIVE")
    thehive_api_key = config.get_configuration("THEHIVE_API_SERVICE")
    session = SessionThehive(base_url=thehive_url)
    session.set_api_key(thehive_api_key)
    update_case = UpdateCase(session)
    update_data = {"tags": ["new_tag"]}
    case_id = "~4235304"
    response, status = update_case.update_case(case_id, update_data)
    if status != 200:
        msg = f"Erro ao atualizar caso {case_id}: {status}"
        raise Exception(msg)

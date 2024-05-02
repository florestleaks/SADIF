import datetime

from pymongo import MongoClient
from soar.config.soar_config import SoarConfiguration
from soar.frameworks_drivers.crawler.crawler_manager import CrawlerManager
from soar.frameworks_drivers.crawler.soar_crawler import WebCrawler
from soar.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_datatype import (
    CaseDataType,
)
from soar.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case.create_case import (
    CreateCase,
)
from soar.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case_comment_template import (
    CaseCommentTemplate,
)
from soar.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case_comment_template.template_render import (
    TemplateRenderer,
)
from soar.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_session import (
    SessionThehive,
)


def current_unix_timestamp():
    # Obtendo a data e hora atual no fuso horário UTC
    data = datetime.datetime.now(datetime.UTC)
    timestamp_convertido = (
        datetime.datetime.timestamp(data) * 1000
    )  # Multiplicando por 1000 para obter milissegundos

    return timestamp_convertido


# Testando a função
if __name__ == "__main__":
    # Initialize the MongoDB client
    config = SoarConfiguration()
    db_url = config.get_configuration("MONGODB_URL")
    db_real = MongoClient(db_url)
    crawler_manager = CrawlerManager(db_real)
    crawler_without_credential_web = crawler_manager.get_all_documents_by_collection()[
        "crawler_without_credential_web"
    ]
    for crawler_run in crawler_without_credential_web:
        crawler = WebCrawler(
            db_client=db_real,
            timeout=crawler_run["timeout"],
            max_threads=crawler_run["max_threads"],
        )
        crawler.crawl(url=crawler_run["url"], depth=crawler_run["depth"])
        crawler.close_all_sessions()
        print(crawler.all_matches)

        for chamados in crawler.all_matches:
            # Create an instance of the TemplateRenderer with the CASE_MONITORING_DNS_ALERT_YARA template
            dns_alert_yara_renderer = TemplateRenderer(
                CaseCommentTemplate.CASE_MONITORING_DNS_ALERT_YARA,
                dominio_suspeito=chamados["link_match"],
                regra_deteccao=chamados["rule_name"],
                cliente=chamados["client_match"],
            )
            # Render the template
            dns_alert_yara_comment = dns_alert_yara_renderer.render()
            # Create Case Data
            case_data = CaseDataType(
                title=f"Nome da Regra: {chamados['rule_name']} | Condição YARA: {chamados['yara_match_condition']} | Correspondência de Link: {chamados['link_match']} | Cliente: {chamados['client_match']} | Tipo de Regra: {chamados['rule_type']}",
                description=dns_alert_yara_comment,
                severity=3,
                tags=[chamados["client_match"], chamados["rule_type"]],
                createdAt=current_unix_timestamp(),
                startDate=current_unix_timestamp(),
            )

            # Initialize SoarConfiguration
            config = SoarConfiguration()

            # Retrieve TheHive configurations
            thehive_url = config.get_configuration("THEHIVE")
            thehive_api_key = config.get_configuration("THEHIVE_API_SERVICE")

            # Initialize TheHive session with API key
            session = SessionThehive(base_url=thehive_url)
            session.set_api_key(thehive_api_key)

            # Create a case using TheHive API
            case_creator = CreateCase(session)
            status_code = case_creator.create(case_data)

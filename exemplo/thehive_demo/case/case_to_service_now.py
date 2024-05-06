"""from sadif.frameworks_drivers.notification.webhook import WebhookSender
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.caso_de_uso.caselist import (
    CaseLister,
)
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case.save_case import (
    MongoDBSaver,
)
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_case.update_case import (
    UpdateCase,
)
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_session import (
    SessionThehive,
)


class CaseUpdater:
    def __init__(self, thehive_session: SessionThehive):
        self.thehive_session = thehive_session

    def update_case_tag(self, case_id: str, new_tag: str):
        update_case = UpdateCase(self.thehive_session)
        update_data = {"tags": [new_tag]}
        response, status = update_case.update_case(case_id, update_data)
        if status != 200:
            msg = f"Erro ao atualizar caso {case_id}: {status}"
            raise Exception(msg)


class CaseProcessor:
    def __init__(
        self, lister: CaseLister, saver: MongoDBSaver, sender: WebhookSender, updater: CaseUpdater
    ):
        self.lister = lister
        self.saver = saver
        self.sender = sender
        self.updater = updater

    def process_cases(self, original_tag: str, new_tag: str):
        cases_with_tag = self.lister.list_cases_by_tag(original_tag)
        self.saver.save_cases(cases_with_tag)

        for case in cases_with_tag:
            self.sender.send(case)
            self.updater.update_case_tag(case["id"], new_tag)

        print("Processamento de casos concluído.")


session = SessionThehive(base_url="http://192.168.1.109:9000/api")
session.set_api_key("fLyWTXETVT1EqwD5JeSroydX7xA68aIA")
case_lister = CaseLister(session)
mongo_saver = MongoDBSaver(
    "mongodb://192.168.1.109:27017/", "your_database_name", "your_collection_name"
)
webhook_sender = WebhookSender("https://dsa.requestcatcher.com/")
case_updater = CaseUpdater(session)

case_processor = CaseProcessor(case_lister, mongo_saver, webhook_sender, case_updater)
case_processor.process_cases("caju", "service_now_processed")
"""

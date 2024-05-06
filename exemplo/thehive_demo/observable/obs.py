from sadif.config.soar_config import SadifConfiguration
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_observable import (
    Observable,
)
from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_session import (
    SessionThehive,
)

if __name__ == "__main__":
    config = SadifConfiguration()
    thehive_url = config.get_configuration("THEHIVE")
    thehive_api_key = config.get_configuration("THEHIVE_API_SERVICE")
    session = SessionThehive(base_url=thehive_url)
    session.set_api_key(thehive_api_key)
    observable_instance = Observable(session)
    data_type = ["domain", "fqdn", "hostname", "ip", "url"]
    for i in data_type:
        response = observable_instance.add_to_case(
            case_id="~4251664", data_type=i, data="example.com"
        )
        print(response)

    response = observable_instance.update_observable(
        observable_id="~4251664", data_type="domain", add_tags=["newTag1"]
    )
    print(response)

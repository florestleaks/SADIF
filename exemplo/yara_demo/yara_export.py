from soar.config.soar_config import SoarConfiguration
from soar.frameworks_drivers.soar_yara.yara_export import YaraRulesExporter

config = SoarConfiguration()
db_url = config.get_configuration("MONGODB_URL")

if __name__ == "__main__":
    exporter = YaraRulesExporter(db_url, "YaraRules", ".", auto_extract=True)
    exporter.export_rules()

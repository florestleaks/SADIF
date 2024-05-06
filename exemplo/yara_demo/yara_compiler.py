from pymongo import MongoClient
from soar.config.soar_config import SoarConfiguration
from soar.frameworks_drivers.soar_yara.yara_compiler import SoarYaraCompiler

if __name__ == "__main__":
    config = SoarConfiguration()
    db_url = config.get_configuration("MONGODB_URL")
    db_real = MongoClient(db_url)
    exporter = SoarYaraCompiler(db_real)
    a = exporter.match_text("paul.canarin@hdi.com.br")
    print(a)

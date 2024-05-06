from pymongo import MongoClient
from requests import Session

from sadif.config.soar_config import SadifConfiguration
from sadif.frameworks_drivers.crawler.soar_crawler import WebCrawler
from sadif.frameworks_drivers.web.session_manager import SessionManager


# Implementações de estratégias de autenticação
class BasicAuthStrategy:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def authenticate(self, session: Session) -> Session:
        session.auth = (self.username, self.password)
        return session


if __name__ == "__main__":
    config = SadifConfiguration()
    db_url = config.get_configuration("MONGODB_URL")
    db_real = MongoClient(db_url)

    # Supondo que você tenha credenciais válidas para um site que requer autenticação
    username = "your_username"
    password = "your_password"  # noqa: S105

    # Exemplo de uso
    basic_auth_strategy = BasicAuthStrategy(
        username, password
    )  # Assumindo que essa estratégia foi definida anteriormente

    session_manager = SessionManager()

    # Criar uma sessão com autenticação básica
    session_with_basic_auth = session_manager.create_session(basic_auth_strategy)

    # Inicializa o WebCrawler com a instância de Authenticator
    crawler = WebCrawler(db_client=db_real, timeout=50, max_threads=10)

    # Inicia o processo de crawling em um site que requer autenticação e passa a sessão autenticada
    crawler.crawl("https://example.com", depth=3, session=session_with_basic_auth)
    crawler.close_all_sessions()

    print(crawler.proxy_tor_https)
    print(crawler.visited_urls)
    print("Quantidade de match found:", len(crawler.all_matches))
    print(crawler.all_matches)
    print(len(crawler.close_all_sessions()))

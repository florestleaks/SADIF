import logging.config

from sadif.config_loader import ConfigLoader


class LogManager:
    """
    A class responsible for setting up and managing the logging system based on configuration settings.

    Methods
    -------
    setup_logging():
        Sets up logging configurations using settings from the ConfigLoader.
    get_logger(name: str) -> logging.Logger:
        Retrieves a configured logger by name.
    """

    @classmethod
    def setup_logging(cls) -> None:
        """Setup logging configurations using settings from the ConfigLoader."""
        config_loader = ConfigLoader()
        log_config = config_loader.get("logging")
        if log_config:
            logging.config.dictConfig(log_config)
        else:
            logging.basicConfig(level=logging.WARNING)
            logging.warning("Logging configuration not found, using basic configuration.")

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """Retrieve a configured logger by name.

        Parameters
        ----------
        name : str
            The name of the logger to retrieve.

        Returns
        -------
        logging.Logger
            The logger instance with the given name.
        """
        return logging.getLogger(name)


# Example usage:

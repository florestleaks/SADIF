import json
from pathlib import Path
from typing import Any, Optional

# improve the class ConfigLoader


class ConfigLoader:
    """
    A singleton class used for managing configuration settings.

    Attributes
    ----------
    _instance : Optional['Config']
        The singleton instance of the Config class.
    settings : Dict[str, Any]
        Dictionary storing the configuration settings.

    Methods
    -------
    load_config(config_file: Path)
        Loads configuration settings from a JSON file.
    get(key: str) -> Any
        Retrieves the value for a given configuration key.
    push_to_airflow()
        Pushes configuration settings to Airflow variables if in an Airflow environment.
    is_airflow_environment() -> bool
        Checks if the current environment is an Airflow environment.

    """

    _instance: Optional["ConfigLoader"] = None
    DEFAULT_CONFIG_FILE: Path = Path(__file__).resolve().parent / "default_config.json"

    def __new__(cls, config_file: Path | None = None) -> "ConfigLoader":
        """Create a new instance or return the existing one."""
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance.settings = {}
            # Ensure the config_file is a Path object
            config_path = Path(config_file) if config_file else cls.DEFAULT_CONFIG_FILE
            cls._instance.load_config(config_path)
        return cls._instance

    def load_config(self, config_file: Path) -> None:
        """Load configuration from a JSON file.

        Parameters
        ----------
        config_file : Path
            The file path to load the configuration from.
        """
        # Open the file using the Path object
        with config_file.open("r") as file:
            self.settings = json.load(file)

    def get(self, key: str) -> Any:
        """Get a configuration value by key, with optional Airflow support.

        Parameters
        ----------
        key : str
            The configuration key to retrieve.

        Returns
        -------
        Any
            The value associated with the configuration key.
        """
        if self.is_airflow_environment():
            try:
                from airflow.models import Variable

                return Variable.get(key, default_var=self.settings.get(key))
            except ImportError:
                pass
        return self.settings.get(key)

    def push_to_airflow(self) -> None:
        """Push configuration to Airflow if in an Airflow environment."""
        if self.settings:
            if self.is_airflow_environment():
                try:
                    from airflow.models import Variable

                    for key, value in self.settings.items():
                        Variable.set(key, value)
                        print(f"Configuration '{key}' sent to Airflow.")
                except ImportError:
                    print("Airflow is not installed in this environment.")
            return

        raise Exception("Configurations not loaded.")

    @staticmethod
    def is_airflow_environment() -> bool:
        """Check if the environment is an Airflow environment.
        Returns
        -------
        bool
            True if 'AIRFLOW_HOME' is in the environment variables, otherwise False.
        """
        import os

        return "AIRFLOW_HOME" in os.environ

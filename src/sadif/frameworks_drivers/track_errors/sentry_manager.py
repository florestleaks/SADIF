import sentry_sdk

from sadif.config_loader import ConfigLoader


class SentryManager:
    """
    A class responsible for setting up and managing Sentry integration for error reporting.

    Methods
    -------
    initialize_sentry():
        Initializes Sentry SDK with settings from the ConfigLoader.
    """

    @classmethod
    def initialize_sentry(cls) -> None:
        """Initializes Sentry SDK with settings from the ConfigLoader."""
        config_loader = ConfigLoader()
        # release_config_file = toml.load('../../../../pyproject.toml')
        release_version = "0"  # release_config_file['tool']['poetry']['version']
        sentry_config = config_loader.get("sentry")
        if sentry_config and "dsn" in sentry_config:
            sentry_sdk.init(
                dsn=sentry_config["dsn"],
                traces_sample_rate=sentry_config.get("traces_sample_rate", 1.0),
                environment=sentry_config.get("environment"),
                release=release_version,
            )
            return "Sentry initialized successfully."
        else:
            return "Sentry configuration not found or incomplete."

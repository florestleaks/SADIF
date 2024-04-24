"""sadif package. init"""

from sadif.frameworks_drivers.track_errors.sentry_manager import SentryManager

SentryManager.initialize_sentry()

import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.abspath(os.path.join(current_dir, os.pardir, 'build', 'logs'))
os.makedirs(log_dir, exist_ok=True)

# Log path <project>/build/logs/<app.log>
log_file = os.path.abspath(os.path.join(log_dir, 'app.log'))

# File logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    # File handler
    file_handler = TimedRotatingFileHandler(
        log_file,
        when="D",
        interval=7,         # Rotate on every 7 days
        backupCount=4,      # Keep 4 backup log file
        encoding="utf-8"
    )
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    logger.addHandler(console_handler)

    # Have the discord log connected to same file handler
    # Discord default would have console output, so no need to add console output handler
    discord_logger = logging.getLogger("discord")
    discord_logger.setLevel(logging.DEBUG)
    discord_logger.addHandler(file_handler)


__all__ = ["logger"]

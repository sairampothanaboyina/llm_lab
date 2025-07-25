import logging
import os
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

def get_logfile_name() -> str:
    configured_file_name = os.getenv("APP_CONFIG_LOGGING_FILE_NAME")
    return configured_file_name.strip() \
        if configured_file_name and configured_file_name.strip() != "" \
        else "logs.txt"

def load_env():
    load_dotenv(override=True)

def setup_logging(level: logging.INFO, log_file_name: str = None, file_size = (10 * 1024 * 1024), backup_count: int = 5, logs_dir = "logs"):
    file_name = log_file_name if (log_file_name is not None and log_file_name.strip() != "")  else get_logfile_name()
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    os.makedirs(logs_dir, exist_ok=True)
    log_file = os.path.join(logs_dir, file_name)
    file_handler = RotatingFileHandler(
        log_file, maxBytes = file_size, backupCount = backup_count
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    logging.basicConfig(level=level, handlers=[console_handler, file_handler])
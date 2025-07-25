import logging
import os
from logging import Logger

from base.config import system_config
from base.llm.secrets.const.secret_type import SecretType
from base.llm.secrets.dto.secrets import Secret


system_config.load_env()
system_config.setup_logging(level= logging.DEBUG)
logger: Logger = logging.getLogger(__name__)

def main():
    logger.info("starting app run from main module....")
    secret = Secret().get_secret(SecretType.CHATGPT)
    logger.info(f"secret is {secret}")
    logger.info(os.environ.items())
    for item in os.environ.items():
        logger.debug(f"{item[0]} = {item[1]}")

if __name__ == "__main__":
    main()
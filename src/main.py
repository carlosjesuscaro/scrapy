# TODO
# 1. Allow the user to enter a URL
# 2. Collect all hyperlinks
# 3. Parse the links between internal or external
# 4. Identify which external links are broken
# 5. Collect external links: back referrals AND non referrals
import logging
import logging.config
import os
from datetime import datetime
from dotenv import find_dotenv, load_dotenv

# find .env file in parent directory
env_file = find_dotenv()
load_dotenv()

CONFIG_DIR = "./config"
LOG_DIR = "./logs"


def setup_logging():
    """Load logging configuration"""
    log_configs = {"dev": "logging.dev.ini", "prod": "logging.prod.ini"}
    config = log_configs.get(os.environ["ENV"])
    config_path = "/".join([CONFIG_DIR, config])

    timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")

    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=False,
        defaults={"logfilename": f"{LOG_DIR}/{timestamp}.log"},
    )


def test():
    print('Testing the implementation of logging')


if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Program started")
    test()
    logger.info("Program finished")

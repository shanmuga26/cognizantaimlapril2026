import sys 
import os

#add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from conf.logger_conf import setup_logger

# Entry point of the app. This module initializes the app and starts it. It can also be used to set up any necessary configurations or dependencies before the app runs.

logger = setup_logger()

def run():
    #test logger.info("app initialized")
    logger.info("app initialized")

#handle entry-except block to catch any exceptions that may occur during the app initialization and log them using the logger.
if __name__ == "__main__":
    run()    
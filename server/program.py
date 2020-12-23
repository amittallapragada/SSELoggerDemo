"""
program.py
This script will keep adding logs to our logger file.
"""

import logging 
import time 
# create logger with log app
logger = logging.getLogger('log_app')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

#infinite while loop printing to our log file.
i = 0
while True:
    logger.info(f"log message num: {i}")
    i += 1
    time.sleep(0.3)
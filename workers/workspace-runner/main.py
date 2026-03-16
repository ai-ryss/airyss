import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

logging.info("workspace-runner started")

while True:
    time.sleep(3600)

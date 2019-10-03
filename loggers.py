import sys
import logging
from logging.handlers import RotatingFileHandler

file = "./cocktail_log"
format = "%(asctime)s | %(name)s | %(message)s"
logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format = format)


logger = logging.getLogger("my-logger")
handler = RotatingFileHandler(file,maxBytes=100000,backupCount=1)
logger.addHandler(handler)

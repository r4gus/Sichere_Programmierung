import logging

logger = logging.getLogger("Cipher")
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

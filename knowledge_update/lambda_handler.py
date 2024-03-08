import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle(event, context):
    logger.info("Received event")
    logger.info(event)

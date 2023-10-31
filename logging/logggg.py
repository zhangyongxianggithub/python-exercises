import logging


logging.basicConfig(level=logging.WARN)

logger=logging.getLogger('test')
logger.info('ddddd%s','aaa')
logger=logging.getLogger('test1')
logger.info('ddddd%s','aaa')
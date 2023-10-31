import logging
import sys
from logging import StreamHandler
from logging import INFO
from logging import Handler
from logging import Logger
from logging import Formatter

logger: Logger = logging.getLogger('clear')
logger.propagate = 0
logger.setLevel(INFO)
handler: Handler = StreamHandler(sys.stdout)
handler.setLevel(INFO)
handler.setFormatter(Formatter(
    fmt='%(asctime)s %(levelname)s %(process)d --- [%(threadName)s] %(pathname)s(%(lineno)d): %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'))
print(logger.isEnabledFor(logging.INFO))
logger.addHandler(handler)
logger.info('ddddd%s', 'aaa')
logger.info('ddddddd%s', 'aaa')

print('%(m)s' % {'m': 'xxx'})

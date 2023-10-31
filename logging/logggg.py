import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(process)d --- [%(threadName)s] %(pathname)s(%(lineno)d): %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger('test')
logger.info('ddddd%s', 'aaa')
logger = logging.getLogger('test1')
logger.info('ddddd%s', 'aaa')

print('%(m)s' % {'m': 'xxx'})

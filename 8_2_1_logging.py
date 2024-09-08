"""some text"""

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[{asctime}] #{levelname:8} {filename}:'
                    '{lineno} - {name} - {message}',
                    style='{')

logging.debug('Это лог уровня DEBUG')
logging.info('Это лог уровня INFO')
logging.warning('Это лог уровня WARNING')
logging.error('Это лог уровня ERROR')
logging.critical('Это лог уровня CRITICAL')

logger = logging.getLogger(__name__)
print(logger)
# print(dir(logger))

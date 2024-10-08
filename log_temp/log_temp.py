import logging
import logging.config
import yaml

def devide_number(dividend: int | float, devider: int | float):
    try:
        return dividend / devider
    except ZeroDivisionError:
        logger.exception('Произошло деление на 0')
        # print('Произошло деление на 0')


with open('./log_temp/log_temp_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())
logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


a, b = 12, 2
c, d = 4, 0
print(devide_number(a, b))
# print(devide_number(c, d))

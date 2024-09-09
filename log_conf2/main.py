import logging.config

#from logging_settings import logging_config
import yaml
from module_1 import main

# Загружаем настройки логирования из словаря `logging_config`
#logging.config.dictConfig(logging_config)

with open('logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

# Исполняем функцию `main` из модуля `module_1.py`
main()
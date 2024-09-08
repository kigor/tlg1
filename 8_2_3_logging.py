import logging

logger = logging.getLogger(__name__)

format = '[{asctime}] #{levelname:8} {filename}:'\
           '{lineno} - {name} - {message}'

formatter = logging.Formatter(
    fmt=format,
    style='{'
)

file_handler = logging.FileHandler('logs.log')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

print(logger.handlers)

logger.warning('Это лог с предупреждением!')

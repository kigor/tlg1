import logging

class ExcLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR'

import logging


def logging_start():
    data_format = '%(asctime)s - "%(name)s" - %(levelname)s - %(message)s'
    logging.basicConfig(
        level=logging.ERROR,
        format=data_format,
        filename='errors.txt',
        filemode='a',
        encoding='utf-8'
    )

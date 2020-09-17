# -*- coding：utf-8 -*-
# @Time   : 2020/5/30 15:12
# @Author : 田干
# @Email  : tiangan_529@163.com
# @File   : logging_handler.py

import logging,colorlog

'''
日志封装
'''
def get_logger(
        name = 'root',
        file=None,
        logger_level='DEBUG',
        stream_level='DEBUG',
        file_level='INFO',
        fmt='%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s: %(message)s'
):
    log_colors_config = {
        'DEBUG': 'white',  # cyan white
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }

    # 初始化日志收集器
    logger = logging.getLogger(name)

    # 设置日志等级
    logger.setLevel(logger_level)

    # 每次被调用后，清空已经存在handler，防止重复打印
    logger.handlers.clear()

    # 设置输出台
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_level)
    logger.addHandler(stream_handler)

    # 设置日志格式
    fmt = logging.Formatter(fmt)
    stream_handler.setFormatter(fmt)

    console_formatter = colorlog.ColoredFormatter(
        fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
        datefmt='%Y-%m-%d  %H:%M:%S',
        log_colors=log_colors_config
    )
    stream_handler.setFormatter(console_formatter)

    # 如果有文件，就输出到文件
    if file:
        file_handler = logging.FileHandler(file,encoding='utf-8')
        file_handler.setLevel(file_level)
        file_handler.setFormatter(fmt)   # 设置输出格式
        logger.addHandler(file_handler)  # 把输出台加到收集器上

    return logger
if __name__ == '__main__':

    logger = get_logger()
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
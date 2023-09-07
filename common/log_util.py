import logging
import os


def log_info(message):
    # 创建一个日志记录器
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # 日志文件路径
    os.path.join('()log', 'test.log')

    # 移除之前添加的处理器，如果存在的话
    for handler in logger.handlers:
        logger.removeHandler(handler)

    # 创建一个处理器，将日志同时写入文件和输出到控制台
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # 定义日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # 将处理器添加到日志记录器
    logger.addHandler(handler)

    # 记录日志信息
    logger.info(message)

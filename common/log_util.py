import logging
import os


def log_info(message):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    log_file_path = os.path.join('log', 'test.log')
    # 创建一个文件处理器，将日志写入到文件中

    handler = logging.FileHandler(log_file_path)
    handler.setLevel(logging.DEBUG)

    # 创建一个控制台处理器，将日志输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 定义日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # 将处理器添加到日志记录器
    logger.addHandler(handler)
    logger.addHandler(console_handler)
    logger.info(message)


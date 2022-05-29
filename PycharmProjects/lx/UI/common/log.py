import logging

def log():
    logging.basicConfig(level=logging.ERROR,
                        format="日志器名称:%(name)s日志级别:%(levelname)s-模块:%(module)s.py-第%(lineno)d行 日志内容:%(message)s")
    logger = logging.getLogger("songjianwei")
    return logger

#使用单列模式创建日志记录器
logger = log()

if __name__ == '__main__':
    logger.info("发布成功")

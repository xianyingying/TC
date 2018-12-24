# logging模块支持我们自定义封装一个新日志类
import logging
import time
import os


class Logger(object):

    def __init__(self, logger):
        """
        创建目录logs
        如果目录已存在则不创建
        如果不存在则创建
        :param logger:
        """
        try:
            File_Path ="D:/TC/H5/report/logs/"
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
        except BaseException as msg:
            print("新建存放日志的目录失败：%s" % msg)
        """
        指定保存日志的文件路径，日志级别，调用文件
        将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger(记录器)
        # 日志记录的工作主要由Logger对象来完成。在调用getLogger时要提供Logger的名称（注：多次使用相同名称 来调用getLogger，返回的是同一个对象的引用。）
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        log_path ='D:/TC/H5/report/logs/'
        #print(log_path)
        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_name = log_path + rq + '.log'  # 文件名
        # 将日志写入磁盘
        fh = logging.FileHandler(log_name,encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
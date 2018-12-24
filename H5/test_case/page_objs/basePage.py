# _*_ coding:utf-8 _*_
import os
import time

from util.Logs import Logger

mylogger = Logger(logger='=basePage').getlog()
class Page(object):
    def __init__(self, driver, base_url=u"http://m.tctest3.com"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def click(self, loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title

    #断言方法
    # 需要传入2个参数  actual  ： 实际操作结果    expected   预期结果
    def action_success(self,actual,expected):
        try:
            assert actual == expected
            mylogger.info(expected)
            #print('登录成功')
        except Exception as e:
            mylogger.info("actual",format(e))
            #print("登录失败", format(e))

    #截图方法
    def screenshot(self):
        # 生成年月日时分秒时间
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # 获取到当前文件的目录，并检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
        try:
            File_Path ="D:/TC/H5/report/image/%s/"% directory_time
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
                mylogger.info("存放图片目录的新建成功：%s" % File_Path)
                #print("目录新建成功：%s" % File_Path)
            else:
                #print("目录已存在！！！")
                mylogger.info("存放图片的目录已存在！！！")
        except BaseException as msg:
            mylogger.info("新建存放图片的目录失败：%s" % msg)
        try:
            url = self.driver.save_screenshot("D:/TC/H5/report/image/"+directory_time+"/"+picture_time+".png")
            #print("%s ：截图成功！！！" % url)
            mylogger.info("%s ：截图成功！！！" % url)
        except Exception as e:
            #print("截图失败",format(e))
            mylogger.info("截图失败",format(e))


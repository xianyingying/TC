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
            File_Path ="D:/pythonLearn/tctestpro/H5/report/image/%s/"% directory_time
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
            url = self.driver.save_screenshot("D:/pythonLearn/tctestpro/H5/report/image/"+directory_time+"/"+picture_time+".png")
            #print("%s ：截图成功！！！" % url)
            mylogger.info("%s ：截图成功！！！" % url)
        except Exception as e:
            #print("截图失败",format(e))
            mylogger.info("截图失败",format(e))

# coding=utf-8
# '''
# Created on 2016-8-13
# @author: Jennifer
# Project:基础类BasePage，封装所有页面都公用的方法，
# 定义open函数，重定义find_element，switch_frame，send_keys等函数。
# 在初始化方法中定义驱动driver，基本url，title
# WebDriverWait提供了显式等待方式。
# '''
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class BasePage(object):
#     """
#     BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
#     """
#
#     # 初始化driver、url、pagetitle等
#     # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参。
#     # __init__方法不能有返回值，只能返回None
#     # self只实例本身，相较于类Page而言。
#     def __init__(self, selenium_driver, base_url, pagetitle):
#         self.driver = selenium_driver
#         self.base_url = base_url
#         self.pagetitle = pagetitle
#
#     # 通过title断言进入的页面是否正确。
#     # 使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
#     def on_page(self, pagetitle):
#         return pagetitle in self.driver.title
#
#     # 打开页面，并校验页面链接是否加载正确
#     # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
#     def _open(self, url, pagetitle):
#         # 使用get打开访问链接地址
#         self.driver.get(url)
#         self.driver.maximize_window()
#         # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法
#         assert self.on_page(pagetitle), u"打开开页面失败 %s" % url
#
#     # 定义open方法，调用_open()进行打开链接
#     def open(self):
#         self._open(self.base_url, self.pagetitle)
#
#     # 重写元素定位方法
#     def find_element(self, *loc):
#         #        return self.driver.find_element(*loc)
#         try:
#             # 确保元素是可见的。
#             # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
#             #            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
#             # 注意：以下入参本身是元组，不需要加*
#             WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
#             return self.driver.find_element(*loc)
#         except:
#             print
#             u"%s 页面中未能找到 %s 元素" % (self, loc)
#
#     # 重写switch_frame方法
#     def switch_frame(self, loc):
#         return self.driver.switch_to_frame(loc)
#
#     # 定义script方法，用于执行js脚本，范围执行结果
#     def script(self, src):
#         self.driver.execute_script(src)
#
#     # 重写定义send_keys方法
#     def send_keys(self, loc, vaule, clear_first=True, click_first=True):
#         try:
#             loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
#             if click_first:
#                 self.find_element(*loc).click()
#             if clear_first:
#                 self.find_element(*loc).clear()
#                 self.find_element(*loc).send_keys(vaule)
#         except AttributeError:
#             print
#             u"%s 页面中未能找到 %s 元素" % (self, loc)
#     def load_data(self,fileName):
#         f = open("D:/pythonLearn/tctestpro/H5/data/%s" % fileName, encoding='utf-8') # 设置以utf - 8 解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
#         data = json.load(f)
#         return data
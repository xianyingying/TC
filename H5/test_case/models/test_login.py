import unittest
from time import sleep

from selenium import webdriver

from H5.test_case.page_objs.homePage import HP
from H5.test_case.page_objs.loginPage import LP
from H5.test_case.page_objs.readJson import readJson
from util.Logs import Logger

mylog = Logger(logger='=test_login').getlog()

class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        mobileEmulation = {'deviceName': 'iPhone X'}
        mylog.info("设置手机型号为iPhone X")
        option = webdriver.ChromeOptions()
        option.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome( options = option)
        self.base_url="http://m.tctest3.com"
        mylog.info("打开浏览器")
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
         driver=self.driver
         rj=readJson()
         data=rj.load_data("login.json")
         mylog.info("读取json文件内容")
         url=data["URL"]
         mylog.info("获取URL:%s" % data["URL"])
         username=data["userName"]
         mylog.info("获取userName:%s" % data["userName"])
         password=data["userPwd"]
         mylog.info("获取userPwd:%s" % data["userPwd"])
         LoginPage=LP(driver,url) #声明LoginPage对象
         LoginPage.gotoLoginPage()  #调用打开页面组件
         mylog.info("打开页面")
         LoginPage.input_username(username)  #调用输入用户名组件
         mylog.info("输入用户名%s" % data["userName"])
         LoginPage.input_password(password)  #调用输入密码组件
         mylog.info("输入密码%s" % data["userPwd"])
         LoginPage.click_login_btn()
         mylog.info("点击登录")
         sleep(1)
         mylog.info("休眠1秒等待截图")
         LoginPage.screenshot()
         sleep(5)
         mylog.info("休眠3秒等待加载元素")
         message = driver.find_element_by_xpath(data["messageLocate"])
         mylog.info("获取登录状态并进行断言")
         LoginPage.action_success(message.get_attribute("textContent"),data["expected"])#调用断言組件
         HomePage = HP(driver, url)
         mylog.info("跳转到首页")
         HomePage.click_message_btn()
         mylog.info("点击我知道了")
         sleep(2)
         mylog.info("休眠3秒")

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



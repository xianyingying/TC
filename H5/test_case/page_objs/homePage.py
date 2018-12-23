# _*_ coding:utf-8 _*_
from selenium.webdriver.common.by import By
from H5.test_case.page_objs.basePage import Page

class HP(Page):
    # 封装元素对象
    message_button = (By.CLASS_NAME, u"weui-btn_default")

    def __init__(self, driver, base_url="http://m.tctest3.com"):
        Page.__init__(self, driver, base_url)

    def gotoHomePage(self):
        self.driver.get(self.base_url)

    def click_message_btn(self):
        self.click(self.message_button)


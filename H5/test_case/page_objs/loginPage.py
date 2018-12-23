# _*_ coding:utf-8 _*_
from selenium.webdriver.common.by import By
from H5.test_case.page_objs.basePage import Page

class LP(Page):
    # 封装元素对象
    username_input = (By.XPATH, u'//input[@placeholder="请输入用户名/手机号"]')
    password_input = (By.XPATH,u'//input[@placeholder="请输入密码"]')
    login_button = (By.CSS_SELECTOR, u'div.login-btn')

    def __init__(self, driver, base_url="http://m.tctest3.com"):
        Page.__init__(self, driver, base_url)


    def gotoLoginPage(self):
        self.driver.get(self.base_url)

    def input_username(self, username):
        self.input_text(self.username_input, username)

    def input_password(self, password):
        self.input_text(self.password_input, password)

    def click_login_btn(self):
        self.click(self.login_button)


#!/user/bin/python
# -*-coding:utf-8-*-
import base_page
from appium import webdriver
from selenium.webdriver.common.by import By
from appium import webdriver

#"登录页面"
class wallet_page(base_page.BaseAaction):
    def __init__(self,driver):
        self.driver=driver

# 登录
    zc_loc=(By.XPATH,"//android.widget.TextView[@text='注册账号']")
    phone_loc=(By.XPATH,"// android.widget.EditText[ @ text = '请输入手机号']")
    sms=(By.XPATH,"// android.widget.EditText[ @ text = '请输入验证码']")
    def zc_click(self):
        self.click(*self.zc_loc)
    def input_pws(self,password):
        self.send_keys(password,*self.pws_loc)
    def click_btnlogin(self):
        self.click(*self.btnlogin_loc)










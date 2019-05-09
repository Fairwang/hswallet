#!user/bin/python
# coding:utf-8
# url wallet webui 元素定位
import base_page,os
from selenium.webdriver.common.by import By
file=os.path.dirname(os.path.dirname(__file__))
class webui_page(base_page.BaseAaction):
    def __init__(self,driver):
       self.driver=driver
#登录界面
    ui_username=(By.XPATH,"//*[@id='username']")
    ui_password=(By.ID,"password")
    ui_login=(By.ID,"sub")

    def input_user(self,username):
        self.send_keys(username,*self.ui_username)
    def input_passw(self,password):
        self.send_keys(password,*self.ui_password)
    def login(self):
        self.click(*self.ui_login)
##主界面
    #用户列表操作
    ui_investor=(By.LINK_TEXT,"用户管理")
    ui_investor_list = (By.LINK_TEXT, "用户列表")
    ui_investor_iframe=(By.XPATH,"//*[@contains,'/admin/investor/index.html']")


    # 交易管理操作
    #订单页面
    ui_order=(By.LINK_TEXT,"交易管理")
    ui_order_list = (By.LINK_TEXT, "订单列表")
    ui_order_iframe=(By.XPATH,"//*[contains(@src,'/admin/order/index.html')]")
    def order(self):
        self.click(*self.ui_order)
    def order_list(self):
        self.click(*self.ui_order_list)
    def order_iframe(self):
        ui_order_iframe_xpath=self.find_element(*self.ui_order_iframe)
        self.driver.switch_to.frame(ui_order_iframe_xpath)
    #补单
    ui_order_budan=(By.XPATH,"//*[contains(@onclick,'/admin/order/additionalorder.html?ids=')]")
    def order_budan(self):
        order_budans=self.find_elements(*self.ui_order_budan)
        return order_budans
    #补单界面
    ui_order_budan_iframe=(By.XPATH,"//*[contains(@src,'order/additionalorder.html?')]")
    def order_budan_iframe(self):
        order_budan_iframe_xpath=self.find_element(*self.ui_order_budan_iframe)
        self.driver.switch_to.frame(order_budan_iframe_xpath)
    #补单提交
    ui_sub=(By.ID,"sub")
    def order_budan_sub(self):
        self.click(*self.ui_sub)
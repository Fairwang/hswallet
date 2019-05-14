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
    ui_investor_iframe=(By.XPATH,"//*[contains(@src,'/admin/investor/index.html')]")

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
 #主界面
    #内容管理操作
    ui_neirong=(By.LINK_TEXT,"内容管理")
    ui_app_version=(By.LINK_TEXT,"APP发布")
    ui_app_versionpublish_iframe=(By.XPATH,"//*[contains(@src,'/admin/app_version/versionpublish.html')]")

    ui_version = (By.ID,"version")
    ui_desc = (By.ID, "desc")
    ui_apk_url = (By.ID, "apk_url")
    def neirong(self):
        self.click(*self.ui_neirong)
    def app_version(self):
        self.click(*self.ui_version)
    def app_versionpublish_iframe(self):
        self.click(*self.ui_app_versionpublish_iframe)

    def versionpublish_iframe(self):
        versionpublish_iframe_xpath=self.find_element(*self.ui_app_versionpublish_iframe)
        self.driver.switch_to.frame(versionpublish_iframe_xpath)
    def version(self,version):
        self.send_keys(version,*self.ui_version)
    def desc(self,desc):
        self.send_keys(desc,*self.ui_desc)
    def apk_url(self,apk_url):
        self.send_keys(apk_url,*self.ui_apk_url)



#!user/bin/python
# coding:utf-8
# url wallet webui 元素定位
import base_page,os
from selenium.webdriver.common.by import By
file=os.path.dirname(os.path.dirname(__file__))
class top_page(base_page.BaseAaction):
    def __init__(self,driver):
       self.driver=driver
#登录界面
    ui_username=(By.XPATH,"//*[@id='user_name']")
    ui_password=(By.ID,"password")
    ui_login=(By.CLASS_NAME,"btn-submit")

    def input_user(self,username):
        self.send_keys(username,*self.ui_username)
    def input_passw(self,password):
        self.send_keys(password,*self.ui_password)
    def login(self):
        self.click(*self.ui_login)
##主界面
    # 交易管理操作
    #订单页面
    ui_order=(By.LINK_TEXT,"订单管理")
    ui_order_list = (By.XPATH, "//*[contains(@href,'/manager_Order_index.html')]")
    ui_order_iframe=(By.XPATH,"//*[contains(@src,'/manager_Order_index.html')]")

    def order(self):
        self.click(*self.ui_order)
    def order_list(self):
        self.click(*self.ui_order_list)
    def order_iframe(self):
        ui_order_iframe_xpath=self.find_element(*self.ui_order_iframe)
        self.driver.switch_to.frame(ui_order_iframe_xpath)
        print "switch true"

    ##搜索订单导出
    ui_create_time=(By.ID,"createtime")
    ui_search=(By.CLASS_NAME,"glyphicon-search")
    ui_excelExportData=(By.ID,"export")
    #订单描述
    ui_memberid=(By.NAME,"memberid")
    def create_time(self,time):
        self.click(*self.ui_create_time)
        self.send_keys(time,*self.ui_create_time)
    def search(self):
        self.click(*self.ui_search)
    def excelExportData(self):
        self.click(*self.ui_excelExportData)
    def memberid(self):
        self.click(*self.ui_memberid)

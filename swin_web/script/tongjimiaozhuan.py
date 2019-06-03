#!user/bin/python
# coding:utf-8
from selenium import webdriver
from hswallet.swin_web.page.webui_page import webui_page
import time
driver=webdriver.Chrome()
driver.get("https://swin.herbeauty.top/admin/index/index.html")

webui_page = webui_page(driver)
user = "test"
# password=""
input_user = webui_page.input_user(user)
webui_page.input_passw("123456")
time.sleep(10)
webui_page.login()
driver.maximize_window()
webui_page.order()
webui_page.order_list()
webui_page.order_iframe()
starttime = 3
endtime = starttime+1
create_time="2019/06/"+str(starttime)+" 00:00:00 - 2019/03/"+str(endtime)+" 00:00:00"
webui_page.create_time(create_time)
webui_page.excelExportData()
time.sleep(5)
excel_path="C:\Users\\tinyw\\Downloads"



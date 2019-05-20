#!user/bin/python
# coding:utf-8
from selenium import webdriver
from hswallet.swin_web.page.wwherbeauty_top import top_page
import time
driver=webdriver.Chrome()
driver.get("https://www.herbeauty.top/manager_Login_index.html")

webui_page = top_page(driver)
user = "admin"
# password=""
input_user = webui_page.input_user(user)
# webui_page.input_passw("123456")
time.sleep(15)
webui_page.login()
driver.maximize_window()
webui_page.order()
webui_page.order_list()
webui_page.order_iframe()
starttime = 17
endtime = starttime+1
create_time="2019-05-"+str(starttime)+" 00:00:00 | 2019-05-"+str(endtime)+" 00:00:00"
webui_page.create_time(create_time)
webui_page.excelExportData()
time.sleep(5)



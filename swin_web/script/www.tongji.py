#!user/bin/python
# coding:utf-8
from selenium import webdriver
from hswallet.swin_web.page.wwherbeauty_top import top_page
from hswallet.swin_web.common.yesterday import Yesterday
import time,datetime
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
yes_time=Yesterday()
today = datetime.date.today()
create_time=str(yes_time)+" 00:00:00 | "+str(today)+" 00:00:00"
webui_page.create_time(create_time)
webui_page.memberid()
webui_page.search()
webui_page.excelExportData()
time.sleep(5)



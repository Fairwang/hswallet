#!user/bin/python
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

from hswallet.web.page.webui_page import webui_page
from hswallet.web.common.table import get_table
import  time
# import SendKeys

driver=webdriver.Chrome()
driver.get("https://wallet.herbeauty.top/admin/index/index.html")
webui_page=webui_page(driver)
user="admin"
# password=""
input_user=webui_page.input_user(user)
# input_passw=webui_page.input_passw(password)
time.sleep(10)
login=webui_page.login()
time.sleep(5)
webui_page.neirong()
webui_page.app_version()
webui_page.versionpublish_iframe()
webui_page.version("zzz")
webui_page.desc("10.2")
webui_page.apk_url("C:\Users\\tinyw\Desktop\wallet_apk\\app-develop-debug0510guoqi.apk")
webui_page.app_version_sub()
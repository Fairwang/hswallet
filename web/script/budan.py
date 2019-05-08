#!user/bin/python
# coding:utf-8
#进行补单操作
from selenium import webdriver
from selenium.webdriver.common.by import By

from hswallet.web.page.webui_page import webui_page
from hswallet.web.common.table import get_table
import  time
driver = webdriver.Chrome()
driver.get("https://wallet.herbeauty.top/admin/index/index.html")
driver.maximize_window()
webui_page = webui_page(driver)
user="admin"
# password=""
input_user=webui_page.input_user(user)
# input_passw=webui_page.input_passw(password)
time.sleep(10)
login=webui_page.login()
time.sleep(5)

webui_page.order()
webui_page.order_list()
time.sleep(1)

webui_page.order_iframe()
time.sleep(1)
get_tables = get_table(driver)
table=get_tables.get_table_content("list")
j=0
for i in table[1:]:
    print table[1][5]
    if table[1][5]==u"等待付款":
        budan=webui_page.order_budan()
        budan[j].click()
        webui_page.order_budan_iframe()
        webui_page.order_budan_sub()
    j+=1









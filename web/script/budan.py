#!user/bin/python
# coding:utf-8
#在订单列表中进行对状态为”等待付款“的订单进行补单操作
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
budans = webui_page.order_budan()
print budans
j=0
print table[1:]
for i in table[1:]:
    print i
    print i[5]
    print "hhhh"
    if i[5]==u"等待付款":
        budans[j].click()#第二次一直定位不到，因为循环一次后，没有回到补单界面
        webui_page.order_budan_iframe()
        webui_page.order_budan_sub()# 点击成功后，当前补单界面自动消失
        time.sleep(2)
        webui_page.order_iframe()#切换到补单界面后，需要再次回到订单界面
        # driver.switch_to.parent_frame()
    j+=1
    print j
    time.sleep(5)











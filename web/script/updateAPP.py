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

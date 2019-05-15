#! user/bin/env
# -*- coding: utf-8 -*-
from selenium import webdriver
from hswallet.web.page.webui_page import webui_page
import time

#denglu
class login():
    def __init__(self):
        self.driver =webdriver.Chrome()
        self.webui_page = webui_page(self.driver)

    def login(self):
        self.driver.get("https://wallet.herbeauty.top/admin/login.html")
        self.driver.maximize_window()
        user = "admin"
        # password=""
        self.webui_page.input_user(user)
        # webui_page.input_passw(password)
        time.sleep(10)
        self.webui_page.login()
        time.sleep(5)

#dengchu
    def login_out(self):
        self.driver.find_element_by_class_name("logout").click()

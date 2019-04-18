#! user/bin/env
# -*- coding: utf-8 -*-
from selenium import webdriver


#denglu
class login():
    def __init__(self):
        self.driver =webdriver.Chrome()

    def login(self):
        self.driver.get("https://wallet.herbeauty.top/admin/login.html")
        name="admin"
        passwo="123456"
        self.driver.find_element_by_name("username").send_keys(name)
        self.driver.find_element_by_name("password").send_keys(passwo)
        self.driver.find_element_by_id("sub").click()

#dengchu
    def login_out(self):
        self.driver.find_element_by_class_name("logout").click()

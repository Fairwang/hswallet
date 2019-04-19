#! user/bin/env
# -*- coding: utf-8 -*-
from selenium import webdriver
from hswallet.web.script.login import login
import unittest
import time


class invertor():
    def __init__(self):
        #denglu
        self.driver =webdriver.Chrome()
        self.driver.get("https://wallet.herbeauty.top/admin/login.html")
        self.login=login()
        self.login.login()
        #切换至用户列表
        self.driver.find_element_by_link_text("用户管理").click()
        self.driver.find_element_by_link_text("用户列表").click()
        #切换至用户列表iframe
        inverstor_iframe=self.driver.find_element_by_xpath("//*[@contains,'/admin/investor/index.html']")
        self.driver.switch_to.iframe(inverstor_iframe)

    def creat(self):
        #添加
        self.driver.find_element_by_xpath("//*[@contains,'investor/create.html']").click()
        #切换至添加管理界面
        investor_create_ifarme=self.driver.find_element_by_xpath("/admin/investor/create.html")
        self.driver.switch_to.iframe(investor_create_ifarme)
        #add invertor
        name="name"
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys(name)

        mobile=15868314566
        self.driver.find_element_by_name("mobile").clear()
        self.driver.find_element_by_name("mobile").send_keys(mobile)

        password=12568
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)

        password = 1234567899
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("sub").click()

    def susuo(self):
        self.driver.find_element_by_name("username").send_keys("15833330033")
        for i in range(100):
            print i
            self.driver.find_element_by_id("search").click()
            time.sleep(1)

aa=invertor()
aa.susuo()

#!/user/bin/python
#  -*-coding: utf-8-*-
import os
import unittest
from appium import webdriver
import time
class zhifubao(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfromVersion'] = '7.1.1'
        desired_caps['deviceName'] = '33d04c7c'
        desired_caps['appPackage'] = 'com.taobao.taobao'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def test_zhifubao(self):
        time.sleep(8)
        adb = 'adb shell input tap 834 141'
        os.system(adb)
        time.sleep(10)
        print("1")
        adb='adb shell input tap 901 1675'#zhaomaobi
        os.system(adb)
        time.sleep(10)
        adb='adb shell input tap 926 990'
        os.system(adb)
        # driver.find_element_by_xpath("//android.view.View[@text='去逛店']").click()#An element could not be located on the page using the given search parameters.
        time.sleep(20)
        adb='adb shell input tap 959 1119'
        os.system(adb)
        time.sleep(2)
        adb='adb shell input tap 562 1364'
        os.system(adb)
        # driver.find_element_by_xpath("//android.view.View[@text='开心收下']")
        # driver.find_element_by_xpath("//android.view.View[@index='0']")
        time.sleep(2)
        adb='adb shell input tap 74 142'
        os.system(adb)
        time.sleep(2)
        adb='adb shell input tap 90 287'
        os.system(adb)



    def tearDown(self):
        print ("yes")

if __name__ == "__main__":
    unittest.main()

#!/user/bin/python
# -*-coding:utf-8-*-
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
class BaseAaction():
    def __int__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        # try:
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))
        return self.driver.find_element(*loc)
        # except Exception as e:
        #     raise e
    def find_elements(self,*loc):
        # try:
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))
        return self.driver.find_elements(*loc)
        # except Exception as e:
        #     raise e

    def click(self,*loc):
        try:
            print self.find_element(*loc).text
            self.find_element(*loc).click()
        except AttributeError,e:
            raise e

    def send_keys(self,value,*loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError,e:
            raise e




# class BaseAaction():
#     def __init__(self,driver):
#         self.driver=driver
#     def find_element(self,loc):
#         try:
#             return self.driver.find_element_by_id()

#  1 class Action(object):
#  2     #初始化
#  3     def __init__(self,se_driver):
#  4         self.driver = se_driver
#  5
#  6     #重写元素定位的方法
#  7     def find_element(self,loc):
#  8         try:
#  9             return self.driver.find_element_by_id(loc)
# 10         except Exception as e:
# 11             print("未找到%s"%(self,loc))
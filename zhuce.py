#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from appium import webdriver
import MySQLdb
class query_database():
    def query_database(self,sql):
        coon = MySQLdb.connect(host='120.77.41.244', user='test', passwd='test@2019#0809', db='cl_p2p', port=3308,
                               charset='utf8')

        cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # 带有键值对的数组
        try:
            cur = cursor.execute(sql)
            rows = cursor.fetchall()
            print rows
            print type(rows)
            print rows[0]
            print rows[0]["invite_code"]
            tt=rows[0]["invite_code"]
            return tt
        except:
            print "Error: This is except:goods"
        coon.close()

class C2Cwap(unittest.TestCase):
    def setUp(self):
        self.desired_caps={}
        self.desired_caps['platformName']='Android'#测试的目标机器
        self.desired_caps['platfromVersion']='8.0.0'#目标设备的系统版本
        self.desired_caps['deviceName']='73EBB18629223414'#测试机器的名称（设备名称即可）
        # self.desired_caps['browserName']='Chrome'
        self.desired_caps['noReset']='true'
        self.desired_caps['appPackage']='com.example.wallet.dev'#被测应用的包名（只有Android测试才用）
        self.desired_caps['appActivity']='com.example.wallet.core.main.SplashActivity'
        self.desired_caps['unicodeKeyboard']='true'#支持中文输入，默认false
        self.desired_caps['resetKeyboard'] = 'true'  # 重置输入法为系统默认
        self.desired_caps['automationName'] = 'uiautomator2'

        self.desired_caps['noReset']='true'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)
        self.query_database1=query_database()


    def test_C2Cwap(self):
        sql = "SELECT * FROM `cl_investor`  ORDER BY id desc "
        invite_code=self.query_database1.query_database(sql)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='注册账号']").click()
        self.driver.find_element_by_xpath("// android.widget.EditText[ @ text = '请输入手机号']").send_keys("15868314566")
        self.driver.find_element_by_xpath("// android.widget.EditText[ @ text = '请输入验证码']").send_keys("123456")
        self.driver.find_element_by_xpath("// android.widget.EditText[ @ text = '请输入邀请码']").send_keys(invite_code)
        self.driver.find_element_by_xpath("// android.widget.EditText[ @ text = '注册']").click()




    def tearDown(self):
        self.driver.quit()

# clpay = clpay_pay(driver)
# clpay.clpay()


if __name__=='__main__':
    unittest.main()


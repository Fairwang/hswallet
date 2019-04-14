#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time,xlrd
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from appium import webdriver
import MySQLdb
import os
from hswallet.hswallet.web.LK import creat_page
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
def readExcel(file_path):
    '''''
    读取excel测试用例的函数
    :param file_path:传入一个excel文件，或者文件的绝对路径
    :return:返回这个excel第一个sheet页中的所有测试用例的list
    '''
    try:
        book = xlrd.open_workbook(file_path)  # 打开excel
    except Exception, e:
        # 如果路径不在或者excel不正确，返回报错信息
        print '路径不在或者excel不正确', e
        return e
    else:
        sheet = book.sheet_by_index(0)
        rows = sheet.nrows
        case_list = []
        for i in range(rows):
            if i != 0:
                # 把每一条测试用例添加到case_list中
                case_list.append(sheet.row_values(i))
        return case_list
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
        self.wallet=creat_page.wallet_page(self.driver)


    def test_C2Cwap(self):
        sql = "SELECT * FROM `cl_investor`  ORDER BY id desc "
        invite_code=self.query_database1.query_database(sql)
        current_file=os.path.dirname(__file__)+"zhuce.xls"
        print current_file
        xinxi0=readExcel(current_file)
        for xinxi in xinxi0:
            phone=xinxi[0]
            name=xinxi[2]
            namenum=xinxi[3]
            card=xinxi[4]
            ylphone=xinxi[5]
            self.wallet.zc_click()
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='注册账号']").click()
            self.driver.find_element_by_xpath("// android.widget.EditText[ @ text = '请输入手机号']").send_keys(phone)
            self.driver.find_element_by_xpath("// android.widget.EditText[ @ text = '请输入验证码']").send_keys("999999")
            self.driver.find_element_by_xpath("// android.widget.EditText[ @ text = '请输入邀请码']").send_keys(invite_code)
            self.driver.find_element_by_xpath("// android.widget.EditText[ @ text = '注册']").click()

            self.driver.find_element_by_xpath("//android.widget.TextView[@text='账户离线,不可接单']").click()
            self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入本人的真实姓名']").send_keys(name)
            self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入本人的身份证号码']").send_keys(namenum)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='下一步']").click()
            self.driver.find_element_by_xpath("//android.widget.EditText[@text='输入银行卡卡号']").send_keys(card)
            self.driver.find_element_by_xpath("//android.widget.EditText[@text='输入银行预留手机号码']").send_keys(ylphone)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='下一步']").click()

            self.driver.find_element_by_xpath("//android.widget.TextView[@text='发送']").click()
            self.driver.find_element_by_xpath("//android.widget.EditText[@text='输入验证码']").send_keys("999999")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='下一步']").click()
            self.driver.find_element_by_xpath("//android.widget.ImageView[@index='1']").click()#返回

            self.driver.find_element_by_xpath("//android.widget.TextView[@text='钱包']").click()
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='账户管理']").click()
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='微信']").click()

            self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入账号']").send_keys(phone)
            erweima=self.driver.find_elements_by_xpath("//android.widget.ImageView[@index='1']")#二维码
            erweima[1].click()#选择二维码
            erweima_picture=self.driver.find_elements_by_xpath("//android.view.View[@index='1']")
            erweima_picture[1].click()
            erweima[2].click()#开启账户
            self.driver.find_element_by_xpath("// android.widget.TextView[ @ text = '确认绑定']").click()
            erweima[0].click()  # 返回账户管理
            self.driver.find_element_by_xpath("//android.widget.ImageView[@index='1']").click()
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='设置']").click()
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='退出登录']").click()



    def tearDown(self):
        self.driver.quit()

# clpay = clpay_pay(driver)
# clpay.clpay()


if __name__=='__main__':
    unittest.main()


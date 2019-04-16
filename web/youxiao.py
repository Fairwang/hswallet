#!user/bin/python
# coding:utf-8
import os
import xlrd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from hswallet.web  import ll

def readExcel(file_path):
    '''''
    读取excel测试用例的函数
    :param file_path:传入一个excel文件，或者文件的绝对路径
    :return:返回这个excel第一个sheet页中的所有测试用例的list

   '''
    try :
        book=xlrd.open_workbook(file_path)
    except  Exception,e:
        print "Excel不存在",e
        return e
    else:
        sheet=book.sheet_by_index(0)
        rows=sheet.nrows
        print rows
        case_list=[]
        for i in range(rows):
            print i
            if i!=0:
                case_list.append(sheet.row_values(i))
    return case_list


print os.path.dirname(__file__)



import time ,unittest
class C2Cwap(unittest.TestCase):
    def setUp(self):
        self.desired_caps={}
        self.desired_caps['platformName']='Android'#测试的目标机器
        self.desired_caps['platfromVersion']='8.1.1'#目标设备的系统版本
        self.desired_caps['deviceName']='33d04c7c'#测试机器的名称（设备名称即可）
        # self.desired_caps['browserName']='Chrome'
        self.desired_caps['noReset']='true'
        self.desired_caps['appPackage']='com.example.wallet.dev'#被测应用的包名（只有Android测试才用）
        self.desired_caps['appActivity']='com.example.wallet.core.main.SplashActivity'
        # self.desired_caps['unicodeKeyboard']='true'#支持中文输入，默认false
        # self.desired_caps['resetKeyboard'] = 'true'  # 重置输入法为系统默认
        self.desired_caps['automationName'] = 'uiautomator2'
        self.desired_caps['noReset']='true'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)        # self.wallet=creat_page.wallet_page(self.driver)



    def test_C2Cwap(self):
        current_file = os.path.dirname(__file__) + "/youxiao.xls"
        print current_file
        xinxi0 = readExcel(current_file)
        print xinxi0
        for xinxi in xinxi0:
            phone = str(int(xinxi[0]))
            print phone
            self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入手机号']").send_keys(phone)
            self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入验证码']").send_keys('123456')
            self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='账户离线,不可接单']").click()
            time.sleep(2)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='钱包']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='设置']").click()
            time.sleep(1)
            self.pay=ll.pay()
            time.sleep(1)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='退出登录']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='确定']").click()
            time.sleep(3)



    def tearDown(self):
        self.driver.quit()

# clpay = clpay_pay(driver)
# clpay.clpay()


if __name__=='__main__':
    unittest.main()

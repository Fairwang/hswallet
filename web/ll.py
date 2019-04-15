#!user/bin/python
# coding:utf-8
import os
import xlrd
# def readExcel(file_path):
#     '''''
#     读取excel测试用例的函数
#     :param file_path:传入一个excel文件，或者文件的绝对路径
#     :return:返回这个excel第一个sheet页中的所有测试用例的list
#     '''
#     try:
#         book = xlrd.open_workbook(file_path)  # 打开excel
#     except Exception, e:
#         # 如果路径不在或者excel不正确，返回报错信息
#         print '路径不在或者excel不正确', e
#         return e
#     else:
#         sheet = book.sheet_by_index(0)
#         rows = sheet.nrows
#         print rows
#         case_list = []
#         for i in range(rows):
#             print i
#             if i != 0:
#                 # 把每一条测试用例添加到case_list中
#                 case_list.append(sheet.row_values(i))
#     return case_list
#
# print os.path.dirname(__file__)
# current_file = os.path.dirname(__file__) + "/zhuce.xls"
#
# xinxi0= readExcel(current_file)
# print xinxi0
# for xinxi in xinxi0:
#     phone = str(xinxi[0])
#     for i in phone:
#         print i
#     print type(phone)
#     name = xinxi[1]
#     print type(name)
#     namenum = xinxi[2]
#     print type(namenum)
#     card = xinxi[3]
#     print type(card)
#     ylphone =int(xinxi[4])
#     print type(ylphone)
#     print phone,name,namenum,card,ylphone

# for i in range(6):
#     print i
#     i += 1

from selenium.webdriver.support.ui import Select

from selenium  import webdriver
import time
def dr():
    dr = webdriver.Chrome()
    dr.get("https://wallet.herbeauty.top/admin/index/index.html")
    dr.find_element_by_name("username").clear()
    dr.find_element_by_name("username").send_keys("admin")
    dr.find_element_by_name("password").clear()
    dr.find_element_by_name("password").send_keys("123456")
    dr.find_element_by_id("sub").click()
    dr.maximize_window()
    dr.find_element_by_link_text(u"交易管理").click()
    time.sleep(2)
    dr.find_element_by_link_text(u"充值记录").click()
    time.sleep(2)
    recharge_iframe=dr.find_element_by_xpath("//*[contains(@src,'investor_recharge/index.html')]")
    dr.switch_to.frame(recharge_iframe)
    dr.find_element_by_id("search").click()
    shehe=dr.find_elements_by_xpath("//*[contains(@onclick,'审核')]")
    shehe[-1].click()
    check_iframe=dr.find_element_by_xpath("//*[contains(@src,'investor_recharge/check.html?')]")
    dr.switch_to.frame(check_iframe)
    dr.find_element_by_name("order_no").send_keys("111111")
    dr.find_element_by_name("total_fee").send_keys(10000)
    dr.find_element_by_id("sub").click()
def pay():
    driver = webdriver.Chrome()
    driver.get("https://wallet.herbeauty.top/index/demo")
    driver.find_element_by_name("price").clear()
    driver.find_element_by_name("price").send_keys(100)
    pay_type = Select(driver.find_element_by_id("pay_type"))
    driver.find_element_by_id("pay_type").click()
    pay_type.select_by_value("2")  # 微信
    # pay_type.select_by_value("1")  # 支付宝
    driver.find_element_by_id("pay").click()
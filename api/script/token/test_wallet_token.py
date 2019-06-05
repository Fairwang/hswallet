#! user/bin/env
# -*- coding: utf-8 -*-
import json
from selenium import webdriver
import requests, time
import os,unittest,re
from hswallet.api.common .database_module import  query_database
from hswallet.api.common.doexcel import doexcel

class request(unittest.TestCase):
    # def __init__(self):
    #     self.query_database = query_database()
    def setUp(self):
        self.query_database = query_database()
    def test_acase(self):
    #执行所有的测试用例
        # try:
        #
        #     flist = []
        #     filename = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "\\cases\\token\\"        # print name
        #     print (filename)
        #     for dir, folde, file in os.walk(filename):
        #         for i in file:
        #             t = "%s%s" % (dir, i)
        #             if (re.match('wallet_*', i)) != None:
        #                 flist.append(t)
        #     print (flist)
        #
        # except IndexError as e:
        #     print ('Please enter a correct testcase! \n')
        # else:
        #     excel_case = doexcel()
        #     for i in flist:
        #
        #         cases = excel_case.readExcel(i)
        #         print(cases)
        #         self.requsets_result(cases, i)
        # print ('success!')
# 执行特定的测试用例
            try:
                # filename = sys.argv[1]
                filename = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/cases/token/" + "wallet_test_wallet_forgot_pwd.xls"
            except IndexError as e:
                print ('Please enter a correct testcase! \n e.x: python gkk.py wallet_0x05_user_info.xls')
            else:
                excel_case = doexcel()
                cases = excel_case.readExcel(filename)
                print (cases)
                self.requsets_result(cases,filename)
            print ('success!')

    def requsets_result(self,cases, file_path):
        excel_case = doexcel()
        res_flags = []
        # 存测试结果的list
        request_urls = []
        # 存请求报文的list
        responses = []
        # 存返回报文的list
        start_time = time.strftime("%m%d%H%M%S", time.localtime())
        #获取token
        sql_token = "SELECT * FROM `cl_investor` where mobile=15833330035;"
        sql_token2 = self.query_database.sql_token(sql_token)
        headers = {"Content-Type": "application/json"}
        headers["token"] = sql_token2
        time.sleep(2)

        for case in cases:
            ''''' 
            先遍历excel中每一条case的值，然后根据对应的索引取到case中每个字段的值 
            '''
            time.sleep(2)
            if case["method"].upper() == 'GET':
                if case["param"] == '':
                    new_url = case["url"]  # 请求报文
                    request_urls.append(new_url)
                else:

                    data=eval(case["param"])
                    a_list = []
                    for i in data:
                        a_list.append("%s=%s" % (i, data[i]))
                    data = '&'.join(a_list)
                    # new_url = url + '?' + urlParam(param2)  # 请求报文
                    new_url = case["url"] + '?' + data # 请求报文
                    request_urls.append(new_url)
                results = requests.get(new_url,data=data,headers=headers).text

                # if len(results)>1000:
                #     # A=results.split("<title>")[1].split('</title>')[0]
                #     # print "a%s"%A
                #     a=results.split("<h2>")
                #     print "c%s"%a
                #     c=a[1]
                #     print c
                #     responses.append(c)
                # else:
                #     responses.append(results)
                responses.append(results)
                res = case["readRes"](results, case["res_check"])
            else:

                if case["param"]=='':
                    results = requests.post(case["url"], headers=headers).text
                else:
                    data = eval(case["param"])
                    results = requests.post(case["url"],json=data,headers=headers).text
                    if "pay_url" in results:
                        aa=json.loads(results)
                        driver=webdriver.Chrome()
                        driver.get(aa["data"]["pay_url"])
                if len(results)>1000:
                    A=results.split("<title>")[1].split('</title>')[0]
                    a=results.split("<h2>")[1]
                    c=A+"\n"+a+"\n"
                    responses.append(c)
                else:
                    responses.append(results)

                request_urls.append(case["url"])
                res = excel_case.readRes(results, case["res_check"])


            if 'pass' in res:
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                # writeBug(case_id, interface_name, new_url, results, res_check)
        end_time = time.strftime("%m%d%H%M%S", time.localtime())
        print (float(end_time)-float(start_time))
        excel_case.copy_excel(file_path, res_flags, request_urls, responses)
    def tearDown(self):
        pass
# if __name__ == '__main__':
#
#     try:
#
#         flist = []
#         filename = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/cases/token/"        # print name
#         for dir, folde, file in os.walk(filename):
#             for i in file:
#                 t = "%s%s" % (dir, i)
#                 if (re.match('wallet_*', i)) != None:
#                     flist.append(t)
#         print (flist)
#
#     except IndexError as e:
#         print ('Please enter a correct testcase! \n')
#     else:
#
#         for i in flist:
#             readExcel(i)
#     print ('success!')
#
#     try:
#         # filename = sys.argv[1]
#         filename = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/cases/token/" + "wallet_test_wallet_forgot_pwd.xls"
#     except IndexError as e:
#         print ('Please enter a correct testcase! \n e.x: python gkk.py wallet_0x05_user_info.xls')
#     else:
#         excel_case = doexcel()
#         cases = excel_case.readExcel(filename)
#         print (cases)
#         requsets_result(cases,filename)
#     print ('success!')
#! user/bin/env
# -*- coding: utf-8 -*-
import json
from selenium import webdriver
import requests, xlrd, time
from xlutils import copy
import os,urllib,urllib2
import sys
# reload(sys)
# sys.setdefaultencoding('utf')
from hswallet.api.common import wallet_login_module
from hswallet.api.common.doexcel import doexcel

#登录后获取token 组成公共参数headers
login=wallet_login_module.login_module()
phone="15833330035"
verify_codes=login.verify_code(phone)
headers=verify_codes[0]
verify_code=verify_codes[1]

def requsets_result(case, file_path):
    excel_case = doexcel()

    res_flags = []
    # 存测试结果的list
    request_urls = []
    # 存请求报文的list
    responses = []
    # 存返回报文的list
    start_time = time.strftime("%m%d%H%M%S", time.localtime())
    time.sleep(2)
    for case in cases:

        if case["method"].upper() == 'GET':
            if param == '':
                new_url = case["url"]  # 请求报文
                request_urls.append(new_url)
            else:
                param=eval(param)
                a_list = []
                for i in param:
                    a_list.append("%s=%s" % (i, param[i]))
                param2 = '&'.join(a_list)
                # new_url = url + '?' + urlParam(param2)  # 请求报文
                new_url = case["url"] + '?' + param2 # 请求报文
                request_urls.append(new_url)
            results = requests.get(new_url,data=param,headers=headers).text
            responses.append(results)
            res = case["readRes"](results,case["res_check"] )
        else:

            if param=='':
                results = requests.post(case["url"], headers=headers).text
            else:
                data = eval(param)
                if "real_name" in data.items():
                    # 把字典中的汉字取出来编码试试
                    data=urllib.urlencode(data)
                    response1=urllib2.Request(case["url"],data,headers)
                    response1 = urllib2.urlopen(response1)
                    results=response1.read()
                    print ("kkkk%s"%results)
                    # results = requests.post(url,json=data,headers=headers).text
                if "pay_url" in results:
                    print ("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
                    aa=json.loads(results)
                    print (aa["data"]["pay_url"])
                    driver=webdriver.Chrome()
                    driver.get(aa["data"]["pay_url"])
            if len(results)>1000:
                A=results.split("<title>")[1].split('</title>')[0]
                print ("a%s"%A)
                a=results.split("<h2>")[1]
                print ("c%s"%a)
                c=A+"\n"+a+"\n"
                print (c)
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



if __name__ == '__main__':

    # try:
    #
    #     flist = []
    #     filename = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/cases/token/"        # print name
    #     for dir, folde, file in os.walk(filename):
    #         for i in file:
    #             t = "%s%s" % (dir, i)
    #             if (re.match('wallet_*', i)) != None:
    #                 flist.append(t)
    #     print flist
    #
    # except IndexError, e:
    #     print 'Please enter a correct testcase! \n'
    # else:
    #
    #     for i in flist:
    #         readExcel(i)
    # print 'success!'

    try:
        # filename = sys.argv[1]
        filename = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/cases/alone/" + "wallet_test_wallet_bank_card_create.xls"
    except IndexError as e:
        print('Please enter a correct testcase!%s' % filename)
    else:
        excel_case = doexcel()
        cases = excel_case.readExcel(filename)
        print(cases)
        requsets_result(cases, filename)
print('success!')
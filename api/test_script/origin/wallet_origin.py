#!/user/bin/python
# -*- coding:utf-8 -*-
import requests, xlrd, time, sys
from xlutils import copy
import os
from hswallet.api.common.doexcel import doexcel
def aaa(cases, file_path):
    excel_case = doexcel()
    for case in cases:
        res_flags = []
        # 存测试结果的list
        request_urls = []
        # 存请求报文的list
        responses = []
        print case["case_id"]
        if case["method"].upper() == 'GET':
            if case["param"] == '':
                new_url = case["url"]  # 请求报文
                request_urls.append(new_url)
            else:
                new_url = case["url"] + '?' + excel_case.urlParam(case["param"])  # 请求报文
                request_urls.append(new_url)
            results = requests.get(new_url).text
            responses.append(results)
            res = excel_case.readRes(results, case["res_check"])
        else:
            headers = {"Content-Type": "application/json"}
            print type(case["param"])
            print  case["param"]

            if case["param"] == '':
                results = requests.post(case["url"], headers=headers).text
            else:
                data = eval(case["param"])
                results = requests.post(case["url"], json=data, headers=headers).text
            print len(results)
            # if len(results)>1000:
            #     responses.append(results.split("title")[1])
            # else:
            #
            responses.append(results)
            print results

            request_urls.append(case["url"])
            res = excel_case.readRes(results, case["res_check"])

        if 'pass' in res:
            res_flags.append('pass')
        else:
            res_flags.append('fail')
            # writeBug(case_id, interface_name, new_url, results, res_check)
            excel_case.copy_excel(file_path, res_flags, request_urls, responses)
if __name__ == '__main__':
    # try:
    #
    #     flist = []
    #     filename = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/cases/origin/"        # print name
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
        filename=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+"/cases/origin/"+"wallet_x01_v1_sms_phone.xls"
    except IndexError, e:
        print 'Please enter a correct testcase! \n e.x: python gkk.py wallet_x01_v1_sms_phone.xls'
    else:
        # readExcel(filename)
        excel_case = doexcel()
        print filename
        print os.path.dirname(__file__)
        cases = excel_case.readExcel(filename)
        aaa(cases,filename)
        print"this is cases%s " %cases
    print 'success!'
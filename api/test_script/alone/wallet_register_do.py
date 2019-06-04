#! user/bin/env
# -*- coding: utf-8 -*-
import json
import requests, xlrd, time
from xlutils import copy
import os
from hswallet.api.common import wallet_login_module
from hswallet.api.common.doexcel import doexcel

#登录后获取token 组成公共参数headers
login=wallet_login_module.login_module()
phone="15833330035"
verify_codes=login.verify_code(phone)
headers=verify_codes[0]
verify_code=verify_codes[1]
#登陆成功后，获取设置支付密码时短信验证码

def requsets_result(cases, file_path):
    excel_case = doexcel()
    res_flags = []
    # 存测试结果的list
    request_urls = []
    # 存请求报文的list
    responses = []
    # 存返回报文的list
    start_time = time.strftime("%m%d%H%M%S", time.localtime())
    for case in cases:
        print (case)
        ''''' 
        先遍历excel中每一条case的值，然后根据对应的索引取到case中每个字段的值 
'''
        #获取短信验证码
        time.sleep(2)
        print (case)
        if case["method"].upper() == 'GET':
            if case["param"] == '':
                new_url =case["url"]   # 请求报文
                request_urls.append(new_url)
            else:
                new_url = case["url"] + '?' + case["urlParam"](case["param"])  # 请求报文
                request_urls.append(new_url)
            results = requests.get(new_url,headers=headers).text
            responses.append(results)
            res = case["readRes"](results,case["res_check"] )
        else:# POST

            if case["param"] =='':
                results = requests.post( case["url"] , headers=headers,json=login.code_msg(phone)).text
            else:
                data=eval(case["param"])
                data["verify_code"] = verify_code
                # data=json.dumps(data1)
                print (case["url"])
                results = requests.post(case["url"],json=data,headers=headers).text
            if len(results)>1000:
                responses.append(results.split("<title>")[1])

            else:
                pass

            responses.append(results)
            # print results
            ##??git
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
    try:
        # filename = sys.argv[1]
        filename=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+"/cases/alone/"+"wallet_0x07_set_pay_passwd.xls"
    except IndexError as e:
        print ('Please enter a correct testcase!%s' %filename)
    else:
        excel_case = doexcel()
        cases = excel_case.readExcel(filename)
        print (cases)
        requsets_result(cases,filename)
    print ('success!')
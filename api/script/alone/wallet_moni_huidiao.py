#! user/bin/env
# -*- coding: utf-8 -*-
import requests, xlrd, time
from xlutils import copy
import os
from selenium import webdriver
from hswallet.api.common import database_module
from hswallet.api.common import wallet_sign
from selenium.webdriver.support.ui import Select
from hswallet.api.common import wallet_login_module
from hswallet.api.common.doexcel import doexcel

#登录后获取token 组成公共参数headers
login=wallet_login_module.login_module()
phone="15833330035"
verify_codes=login.verify_code(phone)
headers=verify_codes[0]

#登陆成功后，获取设置支付密码时短信验证码

def requsets_result(cases, file_path):
    query_database1 = database_module.query_database()
    wallet_sign1 = wallet_sign.wallet_sign()
    excel_case = doexcel()
    # headers = login()
    res_flags = []
    # 存测试结果的list
    request_urls = []
    # 存请求报文的list
    responses = []
    # 存返回报文的list
    start_time = time.strftime("%m%d%H%M%S", time.localtime())

    for case in cases:
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
            sql_token="SELECT * FROM `cl_investor` where mobile=17682308681;"
            # sql_token="SELECT * FROM `cl_investor` where mobile=15868314566;"
            sql_token2=query_database1.sql_token(sql_token)
            # sql_token2=str(sql_token2)
            headers = {"Content-Type": "application/json"}
            headers["token"]=sql_token2

            data=eval(case["param"])

            # if case_id < 23:
            #     # for key, value in data.items():
            #     #     if key == "mark":
            #     #         data[key] = data[key].encode("utf-8")
            #     continue#伪造订单
            #
            #     # sign=wallet_sign1.wallet_sign(**data)
            #     # data["sign"]=sign
            #     # print data
            # else:
            #获取Mark==数据库goods
            driver=webdriver.Chrome()
            driver.get("https://wallet.herbeauty.top/index/demo")
            driver.find_element_by_name("mch_id").clear()
            driver.find_element_by_name("mch_id").send_keys(data["20001"])
            driver.find_element_by_name("price").clear()
            driver.find_element_by_name("price").send_keys(data["money"])
            pay_type = Select(driver.find_element_by_id("pay_type"))
            driver.find_element_by_id("pay_type").click()
            pay_type.select_by_value("2")#微信
            # pay_type.select_by_value("1")  # 支付宝
            driver.find_element_by_id("pay").click()
            time.sleep(5)
            goods_sql="SELECT goods FROM cl_order order by id desc limit 1 ;"
            goods=query_database1.query_database(goods_sql)
            data["mark"]=goods

            #构造dt
            # t=time.time()
            # data["dt"]=format(int(round(t * 1000)))
            data["dt"]=int(time.time())
            print (type(data))
            print (data)
            # 价格Mark的Unicode改为utf-8，并调用sign
            for key, value in data.items():
                if key == "mark":
                    data[key] = data[key].encode("utf-8")
            sign=wallet_sign1.wallet_sign(**data)
            data["sign"]=sign
            print ("data%s"%data)
            print (type(data))

            print (case["url"],data,headers)
            results = requests.post(case["url"],json=data,headers=headers).text
            print (results)
            print (len(results))
            # time.sleep(100)
            if len(results)>1000:
                responses.append(results.split("<title>")[1])

            else:
                pass

            responses.append(results)
            request_urls.append(case["url"])
            res = excel_case.readRes(results, case["res_check"])

        if 'pass' in res:
            res_flags.append('pass')
        else:
            res_flags.append('fail')
            # writeBug(case_id, interface_name, new_url, results, res_check)
    end_time = time.strftime("%m%d%H%M%S", time.localtime())
    excel_case.copy_excel(file_path, res_flags, request_urls, responses)



if __name__ == '__main__':
    try:
        # filename = sys.argv[1]
        filename=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+"/cases/alone/"+"wallet_0x23_moni_huidiao.xls"
    except IndexError as e:
        print('Please enter a correct testcase!%s' % filename)
    else:
        excel_case = doexcel()
        cases = excel_case.readExcel(filename)
        print(cases)
        requsets_result(cases, filename)
print('success!')
#! user/bin/env
# -*- coding: utf-8 -*-
import requests, xlrd, time
from xlutils import copy
import os
from selenium import webdriver
from hswallet.common.database_module import query_database
from hswallet.common.wallet_sign import wallet_sign
from selenium.webdriver.support.ui import Select


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
        interfaceTest(case_list, file_path)

query_database1=query_database()
wallet_sign1=wallet_sign()
# login_module=login_module()
def interfaceTest(case_list, file_path):
    # headers = login()
    res_flags = []
    # 存测试结果的list
    request_urls = []
    # 存请求报文的list
    responses = []
    # 存返回报文的list
    start_time = time.strftime("%m%d%H%M%S", time.localtime())

    for case in case_list:

        ''''' 
        先遍历excel中每一条case的值，然后根据对应的索引取到case中每个字段的值 
        '''
        # time.sleep(2)
        try:
            # 项目，提bug的时候可以根据项目来提
            product = case[0]
            # 用例id，提bug的时候用
            case_id = case[1]
            # 接口名称，也是提bug的时候用
            interface_name = case[2]
            # 用例描述
            case_detail = case[3]
            # 请求方式
            method = case[4]
            # 请求url
            url = case[5]
            print url
            # 入参
            param = case[6]
            # 预期结果
            res_check = case[7]
            # 测试人员
            tester = case[10]
            beuzhu = case [12]
            print type(product)
        except Exception, e:
            return '测试用例格式不正确！%s' % e
        print case_id
        #获取短信验证码
        # time.sleep(2)

        if method.upper() == 'GET':
            if param == '':
                new_url = url  # 请求报文
                request_urls.append(new_url)
            else:
                new_url = url + '?' + urlParam(param)  # 请求报文
                request_urls.append(new_url)
            print new_url,
            results = requests.get(new_url,).text
            responses.append(results)
            res = readRes(results, res_check)
        else:# POST
            sql_token="SELECT * FROM `cl_investor` where mobile=17682308681;"
            # sql_token="SELECT * FROM `cl_investor` where mobile=15868314566;"
            sql_token2=query_database1.sql_token(sql_token)
            # sql_token2=str(sql_token2)
            print "sql_token2  %s" %sql_token2
            headers = {"Content-Type": "application/json"}
            headers["token"]=sql_token2
            print type(param)
            print  param
            data=eval(param)

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
            print type(data)
            print data
            # 价格Mark的Unicode改为utf-8，并调用sign
            for key, value in data.items():
                if key == "mark":
                    data[key] = data[key].encode("utf-8")
            sign=wallet_sign1.wallet_sign(**data)
            data["sign"]=sign
            print "data%s"%data
            print type(data)

            print url,data,headers
            results = requests.post(url,json=data,headers=headers).text
            print results
            print len(results)
            # time.sleep(100)
            if len(results)>1000:
                responses.append(results.split("<title>")[1])

            else:
                pass

            responses.append(results)
            request_urls.append(url)
            res = readRes(results, res_check)

        if 'pass' in res:
            res_flags.append('pass')
        else:
            res_flags.append('fail')
            # writeBug(case_id, interface_name, new_url, results, res_check)
    end_time = time.strftime("%m%d%H%M%S", time.localtime())
    print float(end_time)-float(start_time)
    copy_excel(file_path, res_flags, request_urls, responses)


def readRes(res, res_check):
    '''''
    :param res: 返回报文
    :param res_check: 预期结果
    :return: 通过或者不通过，不通过的话会把哪个参数和预期不一致返回
    '''
    res = res.replace('":"', "=").replace('":', "=")
    res_check = res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            print '错误，返回参数和预期结果不一致' + str(s)
            return '错误，返回参数和预期结果不一致' + str(s)
    return 'pass'


def urlParam(param):
    return param.replace(';', '&')


def copy_excel(file_path, res_flags, request_urls, responses):
    '''''
    :param file_path: 测试用例的路径
    :param res_flags: 测试结果的list
    :param request_urls: 请求报文的list
    :param responses: 返回报文的list
    :return:
    '''
    book = xlrd.open_workbook(file_path)
    new_book = copy.copy(book)
    sheet = new_book.get_sheet(0)
    i = 1
    for request_url, response, flag in zip(request_urls, responses, res_flags):
        sheet.write(i, 8, u'%s' % request_url)
        sheet.write(i, 9, u'%s' % response)
        sheet.write(i, 11, u'%s' % flag)
        i += 1
        # 写完之后在当前目录下(可以自己指定一个目录)保存一个以当前时间命名的测试结果，time.strftime()是格式化日期
    name1=time.strftime('%Y%m%d%H%M%S')+"wallet_moni_huidiao.xls"
    name=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+"/report/"+name1
    new_book.save(name)

if __name__ == '__main__':
    try:
        # filename = sys.argv[1]
        filename=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+"/cases/alone/"+"wallet_0x23_moni_huidiao.xls"
    except IndexError, e:
        print 'Please enter a correct testcase!%s'%filename
    else:
        readExcel(filename)
    print 'success!'
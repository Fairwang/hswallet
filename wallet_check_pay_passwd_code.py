#! user/bin/env
# -*- coding: utf-8 -*-
import requests,json


import requests, xlrd, time
from xlutils import copy
import os
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
#登录后获取token 组成公共参数headers
def login():
    headers = {"Content-Type": "application/json"}
    url_dcode = "https://wallet.herbeauty.top/api/v1/sms/"
    phone = "13736048207"
    # "13695884887"
    url_dcode2 = url_dcode + phone
    results = requests.post(url_dcode2, ).text
    results = json.loads(results)
    dcode = results["data"]["code"]
    print dcode
    # 获取token
    url_login = "https://wallet.herbeauty.top/api/v1/login.do"
    data = {"phone_num": phone, "code": dcode}
    results_login = requests.post(url_login,
                                  data).text  # {"code":0,"msg":"登录成功","data":{"token":"dc4581b61c7b82691e14b8028f0148fa","username":"测试4","account_id":2,"mobile":"13736048207"}}
    print results_login
    results_login = json.loads(results_login)
    token = results_login["data"]["token"]
    username = results_login["data"]["username"]
    headers["token"] = str(token)
    print headers
    return headers

#获取code
def code_msg():
    time.sleep(1)
    url_passwd_sms = "https://wallet.herbeauty.top/api/v1/sms/"
    phone_passwd_sms = "13736048207"
    # "13695884887"
    url_passwd_sms = url_passwd_sms + phone_passwd_sms
    results_passwd_sms = requests.post(url_passwd_sms, ).text
    results_passwd_sms = json.loads(results_passwd_sms)
    print "hhh%s" % results_passwd_sms
    dcode_passwd_sms = results_passwd_sms["data"]["code"]
    print dcode_passwd_sms
    # 验证设置支付密码时的验证码.. 传入短信验证码 ，输出verify_code
    dcode_passwd_sms = {"code": dcode_passwd_sms}  # 验证码是否与登录验证码共用
    print dcode_passwd_sms
    return dcode_passwd_sms


def interfaceTest(case_list, file_path):
    headers = login()

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
        time.sleep(2)
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
        time.sleep(2)
        if method.upper() == 'GET':
            if param == '':
                new_url = url  # 请求报文
                request_urls.append(new_url)
            else:
                new_url = url + '?' + urlParam(param)  # 请求报文
                request_urls.append(new_url)
            print new_url,headers
            results = requests.get(new_url,headers=headers).text
            responses.append(results)
            res = readRes(results, res_check)
        else:# POST
            print type(param)
            print  param
            if param=='':
                print url,param,headers
                results = requests.post(url, headers=headers,json=code_msg()).text
            else:
                data=eval(param)
                # data=json.dumps(data1)
                print data
                print type(data)
                print url,data,headers
                results = requests.post(url,json=data,headers=headers).text
            print len(results)
            if len(results)>1000:
                A=results.split("<title>")[1]
                a=results.split("</h2>")[1]
                b=results.split("<h1>")[1]
                c=A+a+b
                responses.append(c)
            # else:
            #
            responses.append(results)
            # print results
            ##??git
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
    name="wallet_check_pay_passwd_code.xls"
    filename = os.path.dirname(__file__) + "/report/" + name
    new_book.save('%s_' % time.strftime('%Y%m%d%H%M%S')+filename)



if __name__ == '__main__':
    try:
        # filename = sys.argv[1]
        filename=os.path.dirname(__file__)+"/cases/"+"wallet_check_pay_passwd_code.xls"
        print filename
    except IndexError, e:
        print 'Please enter a correct testcase! \n e.x: python gkk.py test_case.xls'
    else:
        readExcel(filename)
    print 'success!'
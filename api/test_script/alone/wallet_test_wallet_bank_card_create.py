#! user/bin/env
# -*- coding: utf-8 -*-
import json
from selenium import webdriver
import requests, xlrd, time
from xlutils import copy
import os,urllib,urllib2
from hswallet.api.common import wallet_login_module
import sys

reload(sys)

sys.setdefaultencoding('utf')
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


def interfaceTest(case_list, file_path):
    res_flags = []
    # 存测试结果的list
    request_urls = []
    # 存请求报文的list
    responses = []
    # 存返回报文的list
    start_time = time.strftime("%m%d%H%M%S", time.localtime())
    login_token=wallet_login_module()
    headers = login_token.login()
    time.sleep(2)
    for case in case_list:

        ''''' 
        先遍历excel中每一条case的值，然后根据对应的索引取到case中每个字段的值 
        '''
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
        except Exception, e:
            return '测试用例格式不正确！%s' % e
        print case_id
        time.sleep(2)
        if method.upper() == 'GET':
            if param == '':
                new_url = url  # 请求报文
                request_urls.append(new_url)
            else:
                param=eval(param)
                a_list = []
                for i in param:
                    a_list.append("%s=%s" % (i, param[i]))
                param2 = '&'.join(a_list)
                print param2
                # new_url = url + '?' + urlParam(param2)  # 请求报文
                new_url = url + '?' + param2 # 请求报文
                request_urls.append(new_url)
            print new_url,headers
            results = requests.get(new_url,data=param,headers=headers).text
            print results
            responses.append(results)
            res = readRes(results, res_check)
        else:
            print type(param)
            print  param

            if param=='':
                results = requests.post(url, headers=headers).text
            else:
                data = eval(param)
                print data
                if "real_name" in data.items():


                #把字典中的汉字取出来编码试试
                data=urllib.urlencode(data)
                response1=urllib2.Request(url,data,headers)
                response1 = urllib2.urlopen(response1)
                results=response1.read()
                print "kkkk%s"%results
                # results = requests.post(url,json=data,headers=headers).text



                if "pay_url" in results:
                    print "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
                    aa=json.loads(results)
                    print aa["data"]["pay_url"]
                    driver=webdriver.Chrome()
                    driver.get(aa["data"]["pay_url"])
            print results
            if len(results)>1000:
                A=results.split("<title>")[1].split('</title>')[0]
                print "a%s"%A
                a=results.split("<h2>")[1]
                print "c%s"%a
                c=A+"\n"+a+"\n"
                print c
                responses.append(c)
            else:
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
        print s
        print res
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
    file_path2=file_path.split("/")[-1]
    name1=time.strftime('%Y%m%d%H%M%S')+"_"+file_path2
    name=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+"/report/"+name1
    new_book.save(name)



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
        print filename
    except IndexError, e:
        print 'Please enter a correct testcase! \n e.x: python gkk.py wallet_test_wallet_bank_card_create.xls'
    else:
        readExcel(filename)
    print 'success!'
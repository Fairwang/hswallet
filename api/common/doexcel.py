#!/user/bin/python
# -*- coding:utf-8 -*-
import xlrd, time,os
from xlutils import copy
class doexcel():
    #读取Excel文件
    def readExcel(self,file_path):
        '''''
        读取excel测试用例的函数
        :param file_path:传入一个excel文件，或者文件的绝对路径
        :return:返回这个excel第一个sheet页中的所有测试用例的list
        '''
        try:
            book = xlrd.open_workbook(file_path)  # 打开excel
        except Exception as e:
            # 如果路径不在或者excel不正确，返回报错信息
            print ('路径不在或者excel不正确', e)
            return e
        else:
            sheet = book.sheet_by_index(0)#读取第一个sheet文件
            rows = sheet.nrows
            case_list = []
            for i in range(rows):
                if i != 0:
                    # 把每一条测试用例添加到case_list中
                    case_list.append(sheet.row_values(i))
        return self.interfaceTest(case_list, file_path)
    #将文件内容和测试用例元素对应
    def interfaceTest(self,case_list, file_path):
        testss=[]
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
                testss.append({"product":product,"case_id":case_id,"interface_name":interface_name,"case_detail":case_detail,"method":method,"url":url,"param":param,"res_check":res_check,"tester":tester,"beuzhu":beuzhu})

            except Exception as e:
                return '测试用例格式不正确！%s' % e
        return testss

    #对比实际结果和预期结果
    def readRes(self,res, res_check):
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
                print ('错误，返回参数和预期结果不一致' + str(s))
                return '错误，返回参数和预期结果不一致' + str(s)
        return 'pass'


    def urlParam(self,param):
        return param.replace(';', '&')

    #保存新测试报告
    def copy_excel(self,file_path, res_flags, request_urls, responses):
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
        excel_name=file_path.split("/")[-1]
        report_time=time.strftime('%Y%m%d%H%M%S')+"_"+excel_name
        name=os.path.dirname(os.path.dirname(__file__))+"\\report\\"+report_time
        new_book.save(name)

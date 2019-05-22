#!/user/bin/python
# -*- coding:utf-8 -*-

#登录后台，查询订单，下载Excel，对数据进行统计，
#需要修改查询时间和修改Excel的名称和第一行的内容

import xlrd,xlwt,os
from hswallet.swin_web.common.yesterday import Yesterday
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
        print '啊啊啊路径不在或者excel不正确', e
        return e
    else:
        sheet = book.sheet_by_index(0)
        rows = sheet.nrows
        case_list = []
        for i in range(rows):
            if i != 0:
                # 把每一条测试用例添加到case_list中
                case_list.append(sheet.row_values(i))
        print case_list
        fenxiexcel(case_list)

def fenxiexcel(case_list):
    #笔数和金额统计
    all_zhuanka_pens=0
    success_zhuanka_pens=0
    fail_zhuanka_pens=0
    all_zhuanka_price=0
    success_zhuanka_price=0

    all_wangyin_pens=0
    success_wangyin_pens=0
    fail_wangyin_pens=0
    all_wangyin_price=0
    success_wangyin_price=0

    all_zhipay_pens = 0
    success_zhipay_pens = 0
    fail_zhipay_pens = 0
    all_zhipay_price = 0
    success_zhipay_price = 0

    for case in case_list:
        ''''' 
        先遍历excel中每一条case的值，然后根据对应的索引取到case中每个字段的值 
        '''
        try:
            #金额，渠道，交易状态
            price=case[4]
            type=case[9]
            status=case[11]
        except Exception, e:
            return '测试用例格式不正确！%s' % e
        if type==u"米营支付(转卡)-json":
            all_zhuanka_price=all_zhuanka_price+price
            all_zhuanka_pens+=1
            if u"成功" in status:
                success_zhuanka_pens+=1
                success_zhuanka_price=success_zhuanka_price+price
            else:
                fail_zhuanka_pens+=1
        if type == u"米营网银支付-json":
            all_wangyin_price = all_wangyin_price + price
            all_wangyin_pens += 1
            if u"成功" in status :
                success_wangyin_pens += 1
                success_wangyin_price = success_wangyin_price + price
            else:
                fail_wangyin_pens += 1

        if type == u"智支付-json":
            all_zhipay_price = all_zhipay_price + price
            all_zhipay_pens += 1
            if u"成功" in status:
                success_zhipay_pens += 1
                success_zhipay_price = success_zhipay_price + price
            else:
                fail_zhipay_pens += 1

    tongji_time=Yesterday()
    print tongji_time
    success_zhuanka=format(float(success_zhuanka_pens)/float(all_zhuanka_pens),".3f")
    success_wangyin=format(float(success_wangyin_pens)/float(all_wangyin_pens),".3f")
    success_zhipay = format(float(success_zhipay_pens) / float(all_zhipay_pens), ".3f")
    workbook=xlwt.Workbook(encoding="utf-8")
    worksheet=workbook.add_sheet("zhuanka")
    worksheet.write(1, 0, tongji_time)
    worksheet.write(1,1,all_zhuanka_pens)
    worksheet.write(1,2,all_zhuanka_price)
    worksheet.write(1,3, success_zhuanka_price)
    worksheet.write(1,4,success_zhuanka_pens)
    worksheet.write(1,5,fail_zhuanka_pens)
    worksheet.write(1,7,success_zhuanka)
    #wangyintongji
    worksheet.write(2, 0, tongji_time)
    worksheet.write(2, 1, all_wangyin_pens)
    worksheet.write(2, 2, all_wangyin_price)
    worksheet.write(2, 3, success_wangyin_price)
    worksheet.write(2, 4, success_wangyin_pens)
    worksheet.write(2, 5, fail_wangyin_pens)
    worksheet.write(2, 7, success_wangyin)
    #zhipaytongji
    worksheet.write(3, 0, tongji_time)
    worksheet.write(3, 1, all_zhipay_pens)
    worksheet.write(3, 2, all_zhipay_price)
    worksheet.write(3, 3, success_zhipay_price)
    worksheet.write(3, 4, success_zhipay_pens)
    worksheet.write(3, 5, fail_zhipay_pens)
    worksheet.write(3, 7, success_zhipay)
    workbook.save("datatongji.xls")


if __name__ == '__main__':
    try:
        path=r"C:\Users\tinyw\Downloads"
        excel_paths=os.listdir(path)
        for i in excel_paths:
            if "EXCEL" in i:
                excel_path=path+"\\"+i
                print excel_path
    except IndexError, e:
        print 'Please enter a correct file path'
    else:
        readExcel(excel_path)
    print 'success!'
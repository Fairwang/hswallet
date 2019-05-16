#!/user/bin/python
# -*- coding:utf-8 -*-

#登录后台，查询订单，下载Excel，对数据进行统计，
#需要修改查询时间和修改Excel的名称和第一行的内容

import xlrd,xlwt

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
        print '111路径不在或者excel不正确', e
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
    all_wechat_pens=0
    success_wechat_pens=0
    fail_wechat_pens=0
    all_wechat_price=0
    all_sum=0
    success_wechat_price=0
    yichang_wechat_pens=0

    all_ali_pens=0
    success_ali_pens=0
    fail_ali_pens=0
    all_ali_price=0
    success_ali_price=0
    yichang_ali_pens=0

    for case in case_list:
        ''''' 
        先遍历excel中每一条case的值，然后根据对应的索引取到case中每个字段的值 
        '''
        try:
            #金额，方式，交易状态,交易副状态
            price=case[3]
            type=case[4]
            status=case[5]
            status1=case[6]
        except Exception, e:
            return '测试用例格式不正确！%s' % e
        all_sum=all_sum+price
        if type==u"微信":
            all_wechat_price=all_wechat_price+price
            all_wechat_pens+=1
            if status==u"付款成功":
                success_wechat_pens+=1
                success_wechat_price=success_wechat_price+price
                if status1==u"异常完成":
                    yichang_wechat_pens+=1
            else:
                fail_wechat_pens+=1
    print all_wechat_pens
    success=format(float(success_wechat_pens)/float(all_wechat_pens),".3f")
    yichangbili=format(float(yichang_wechat_pens)/float(all_wechat_pens),".3f")


    workbook=xlwt.Workbook(encoding="utf-8")
    worksheet=workbook.add_sheet("wechat")
    worksheet.write(1,0,all_wechat_pens)
    worksheet.write(1,1,all_sum)
    worksheet.write(1,3,all_wechat_price)
    worksheet.write(1,4, success_wechat_price)
    worksheet.write(1,5,success_wechat_pens)
    worksheet.write(1,6,fail_wechat_pens)
    worksheet.write(1,7,yichang_wechat_pens)
    worksheet.write(1,8,success)
    worksheet.write(1,9,yichangbili)




    # print all_wechat_pens,all_wechat_price,success_wechat_pens,fail_wechat_pens,yichang_wechat_pens,success,yichangbili
    workbook.save("1111.xls")

if __name__ == '__main__':
    try:
        # filename = sys.argv[1]
        # excel_path=os.path.dirname(__file__)+"/订单019.xls"
        # print excel_path
        excel_path=r"F:\shujutongji\0515.xls"
    except IndexError, e:
        print 'Please enter a correct testcase! \n e.x: python gkk.py wallet_x01_v1_sms_phone.xls'
    else:
        readExcel(excel_path)
    print 'success!'
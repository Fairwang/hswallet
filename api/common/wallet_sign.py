#!user/bin/python
# coding:utf-8
import hashlib,json
class wallet_sign():

    def wallet_sign(self,**kw):

    # 判断参数param中是否含有sign值，有则删除，重新添加
    # 将paramlist重新排序，将排序后的的值取出后，使用= 将key和values连接
    # 将连接好后的list中的[a=1,b=2]连接成字符串a=1&b+2,将商户秘钥连接上去
    # 使用md5将字符串进行
    #     kw = json.loads(kw)
    #     print "param 类型%s" % type(kw)
        if 'sign' in kw:
            del kw['sign']
        key = '2bHg2U@nAG7q$4Fh'  # 商户密钥
        # keys=kw
        keys = sorted(kw,reverse=True)  # 排序 得出list
        for i in kw:
            if i=="userids" or i =="money" or i=="mark":
                kw[i]=hashlib.md5(kw[i]).hexdigest()
        a_list = []
        for i in keys:
            a_list.append("%s=%s" % (i, kw[i]))
        b_list = a_list[:]
        b_list[0] = a_list[1]
        b_list[1] = a_list[0]

        print ('%s' % b_list)  #[a=b,c=d]
        sign_str2 = '&'.join(b_list) + key
        print ("Sign Str : "+sign_str2) #a=b&c=d&key=XXX
        md5_sign = hashlib.md5(sign_str2).hexdigest()
        print ("Sign : "+ md5_sign)
        return md5_sign

# aa=wallet_sign()
# cc={'money': '1.00', 'dt': 1554098687, 'useids': '4', 'type': 'alipay', 'mark': u'\u63ed\u5c0f\u7ea2=\u5357\u4eac(\u67e0\u6aac\u7ef8\u827212/21)'}##unicode 编码不能无法haxi
# {'mark': '\u63ed\u5c0f\u7ea2=\u5357\u4eac(\u67e0\u6aac\u7ef8\u827212/21)'}可以成功
# "{"mark":"沉亮=乌鲁木齐(中蓝07/21)"}可以成功
#
# for key,value in cc.items():
#     if key=="mark":
#         cc[key]=cc[key].encode("utf-8")##将其改为utf-8
# print "CC%s"%cc
#
# bb=aa.wallet_sign(**cc)

bb=wallet_sign()
cc={"type":"wechat","userids":"63","money":"100.00","mark":"T1518123354","dt":"1555485666"}
dd=bb.wallet_sign(**cc)
print (dd)
#! user/bin/env
# -*- coding: utf-8 -*-

# import urllib2
# data={
#     "real_name": "张茂春",
#     "id_type": "idcard",
#     "card_no": "6222031203007165761",
#     "credential_no": "51372319890310666",
#     "mobile": "15057357997"
# }
# url="https://wallet.herbeauty.top/api/v1/bank_card/create"
# header={'token': 'e08c4feaa6a9ebe78b2792cade152486', 'Content-Type': 'application/json'}
# req = urllib2.Request(url, data, header)
# response = urllib2.urlopen(req)
# print response.read()


# a=['code=-1',2]
# b='{"code=-1,"msg=姓名不能为空","data={}}'
# if a in b:
#     print 11
print str("中文")
print type(str("中文"))
import MySQLdb
class query_database():
    def query_database(self,sql):
        coon = MySQLdb.connect(host='120.77.41.244', user='test', passwd='test@2019#0809', db='cl_p2p', port=3308,
                               charset='utf8')

        cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # 带有键值对的数组
        try:
            cur = cursor.execute(sql)
            rows = cursor.fetchall()
            print rows
            print type(rows)
            print rows[0]
            print rows[0]["invite_code"]
            tt=rows[0]["invite_code"]
            return tt
        except:
            print "Error: This is except:goods"
        coon.close()
query_database1=query_database()
sql="SELECT * FROM `cl_investor`  ORDER BY id desc "
c=query_database1.query_database(sql)
print c

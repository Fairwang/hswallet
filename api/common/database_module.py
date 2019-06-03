#!/user/bin/python
#  -*-coding: utf-8-*-
import MySQLdb
# class qrocde_url():
class query_database():
    def query_database(self,sql):
        coon = MySQLdb.connect(host='120.77.41.244', user='test', passwd='test@2019#0809', db='cl_p2p', port=3308,
                               charset='utf8')

        cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # 带有键值对的数组
        try:
            cur = cursor.execute(sql)
            rows = cursor.fetchall()
            print (rows)
            print (type(rows))
            print (rows[0])
            print (rows[0]["goods"])
            tt=rows[0]["goods"]
            return tt
        except:
            print ("Error: This is except:goods")
        coon.close()

    def sql_token(self,sql):
        coon = MySQLdb.connect(host='120.77.41.244', user='test', passwd='test@2019#0809', db='cl_p2p', port=3308,
                               charset='utf8')

        cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # 带有键值对的数组
        try:
            cur = cursor.execute(sql)
            rows = cursor.fetchall()
            print (rows)
            print (type(rows))
            print (rows[0])
            print (rows[0]["token"])
            token=rows[0]["token"]
            return token
        except:
            print ("Error: This is except  sql_token")
        coon.close()
# sql="SELECT goods FROM cl_order order by id desc limit 1 ;"
# aa=query_database(sql)
# print aa
# aa=query_database()
# sql="SELECT * FROM `cl_investor` where "
# aa.sql_token(sql)
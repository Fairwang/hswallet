#!/user/bin/python
#  -*-coding: utf-8-*-
import MySQLdb
# class qrocde_url():
def query_database(sql):
    #
    # coon = MySQLdb.connect(host='cpaytest.tinywan.com', user='root', passwd='123456', db='cpay', port=3306,
    #                        charset='utf8')
    # cursor = coon.cursor()
    # coon = MySQLdb.connect(host='103.93.252.181', user='root', passwd='6WUmY1Py', db='cl_cpay', port=3306,
    #                        charset='utf8')
    coon = MySQLdb.connect(host='120.77.41.244', user='test', passwd='test@2019#0809', db='cl_p2p', port=3308,
                           charset='utf8')

    cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # 带有键值对的数组
    try:
        cur = cursor.execute(sql)
        print cur
        rows = cursor.fetchall()
        print rows
    except:
        print "Error: This is except"
        # coon.commit()
    coon.close()


sql="SELECT * FROM cl_order order by id desc limit 1 ;"
aa=query_database(sql)

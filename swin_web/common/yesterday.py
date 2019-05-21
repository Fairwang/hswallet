#!/user/bin/python
# -*- coding:utf-8 -*-
import time,re
import datetime
def Yesterday():
    nowtime = time.asctime(time.localtime())
    print nowtime
    today = datetime.date.today()
    if re.match("Mon", nowtime) != None:
        oneday=datetime.timedelta(days=2)
    else:
        oneday=datetime.timedelta(days=1)
    Yesterday=today-oneday
    return Yesterday
print Yesterday()
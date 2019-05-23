#!/user/bin/python
# -*- coding:utf-8 -*-
import time,re,sched
import datetime,os
def Yesterday():
    nowtime = time.asctime(time.localtime())
    print nowtime
    today = datetime.date.today()
    if re.match("Mon", nowtime) != None:
        oneday=datetime.timedelta(days=2)
    else:
        oneday=datetime.timedelta(days=1)
    Yesterday=today-oneday
    print Yesterday
    return Yesterday
#
# import os,sched
# s=sched.scheduler(time.time,time.sleep) #初始化sched模块
# def execture_command(cmd,delay):
#     os.system(cmd)
#     s.enter(delay,0,execture_command,(cmd,delay))#添加任务:延迟、优先级、函数、以tuple形式传递的触发函数的参数
#     s.run()#执行任务
# execture_command("ping www.baidu.com -t",1)
#

#
# from threading import Timer
# def aa():
#     print "125"
# Timer(3,aa).start()
# # aa()
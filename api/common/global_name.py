#!/user/bin/python
# -*- coding:utf-8 -*-
import requests, xlrd, time, sys
from xlutils import copy
class global_name():
    # 项目，提bug的时候可以根据项目来提
    global product
    # 用例id，提bug的时候用
    global case_id
    # 接口名称，也是提bug的时候用
    global interface_name
    # 用例描述
    global case_detail
    # 请求方式
    global method
    # 请求url
    global url
    # 入参
    global param
    # 预期结果
    global res_check
    # 测试人员
    global tester
    global beuzhu
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
a=['code=-1',2]
b='{"code=-1,"msg=姓名不能为空","data={}}'
if a in b:
    print 11

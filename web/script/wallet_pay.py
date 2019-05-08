#!user/bin/python
# coding:utf-8
import os
import random
from selenium import webdriver
from hswallet.web.common  import dr_pay
wallet_common=dr_pay.wallet_common()

i=1
while i <100:
    id=random.randint(40,100)
    print id
    pay = wallet_common.pay(id)
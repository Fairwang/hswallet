# user/bin/env
# coding:utf-8
import time
from selenium import webdriver
from hswallet.web.common.dr_pay import wallet_common
wallet=wallet_common()
driver=webdriver.Chrome()
id=range(51,152)
for i in id :
    if id<101:
        web_socket="https://wallet.herbeauty.top/index/demo/websocket?id="
        web_socket_url=web_socket+str(i)
        driver.get(web_socket_url)
    time.sleep(1)
    wallet.pay(id)
    time.sleep(10)



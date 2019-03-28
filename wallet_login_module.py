#! user/bin/env
# -*- coding: utf-8 -*-
import  requests
import json,time
class login_module():

    # 登录后获取token 组成公共参数headers

    def login(self):
        headers = {"Content-Type": "application/json"}
        url_dcode = "https://wallet.herbeauty.top/api/v1/sms/"
        phone = "15868314566"
        # "13695884887"
        url_dcode2 = url_dcode + phone
        results = requests.post(url_dcode2, ).text
        results = json.loads(results)
        dcode = results["data"]["code"]
        print dcode
        # 获取token
        url_login = "https://wallet.herbeauty.top/api/v1/login.do"
        data = {"phone_num": phone, "code": dcode}
        results_login = requests.post(url_login,
                                      data).text  # {"code":0,"msg":"登录成功","data":{"token":"dc4581b61c7b82691e14b8028f0148fa","username":"测试4","account_id":2,"mobile":"13736048207"}}
        print results_login
        results_login = json.loads(results_login)
        token = results_login["data"]["token"]
        username = results_login["data"]["username"]
        headers["token"] = str(token)
        print "Login%s"%headers
        return headers


    def code_msg(self):
        time.sleep(1)
        url_passwd_sms = "https://wallet.herbeauty.top/api/v1/sms/"
        phone_passwd_sms = "15868314566"
        # "13695884887"
        url_passwd_sms = url_passwd_sms + phone_passwd_sms
        results_passwd_sms = requests.post(url_passwd_sms, ).text
        results_passwd_sms = json.loads(results_passwd_sms)
        print "hhh%s" % results_passwd_sms
        dcode_passwd_sms = results_passwd_sms["data"]["code"]
        print dcode_passwd_sms
        # 验证设置支付密码时的验证码.. 传入短信验证码 ，输出verify_code
        dcode_passwd_sms = {"code": dcode_passwd_sms}  # 验证码是否与登录验证码共用
        print dcode_passwd_sms
        return dcode_passwd_sms

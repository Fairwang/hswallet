#! user/bin/env
# -*- coding: utf-8 -*-
#获取token和验证码
import  requests
import json,time
class login_module():

    # 登录后获取token 组成公共参数headers
    def login_token(self,phone):
        #获取验证码
        headers = {"Content-Type": "application/json"}
        dcode = self.code_msg(phone)
        # 获取token
        url_login = "https://wallet.herbeauty.top/api/v1/login.do"
        data = {"phone_num": phone, "code": dcode}
        results_login = requests.post(url_login,
                                      data).text  # {"code":0,"msg":"登录成功","data":{"token":"dc4581b61c7b82691e14b8028f0148fa","username":"测试4","account_id":2,"mobile":"13736048207"}}
        results_login = json.loads(results_login)
        token = results_login["data"]["token"]
        username = results_login["data"]["username"]
        headers["token"] = str(token)
        return headers

    def code_msg(self,phone):
        time.sleep(1)
        url_passwd_sms = "https://wallet.herbeauty.top/api/v1/sms/"
        url_passwd_sms = url_passwd_sms + phone
        results_passwd_sms = requests.post(url_passwd_sms, ).text
        results_passwd_sms = json.loads(results_passwd_sms)
        dcode_passwd_sms = results_passwd_sms["data"]["code"]
        # 验证设置支付密码时的验证码.. 传入短信验证码 ，输出verify_code
        dcode_passwd_sms = {"code": dcode_passwd_sms}  # 验证码是否与登录验证码共用
        return dcode_passwd_sms

    def verify_code(self,phone):
        time.sleep(2)
        dcode_passwd_sms =self.code_msg(phone)
        # 验证设置支付密码时的验证码.. 传入短信验证码 ，输出verify_code
        url__passwd_code = "https://wallet.herbeauty.top/api/v1/user/check_pay_passwd_code"
        results = requests.post(url__passwd_code, headers=self.login_token(phone), json=dcode_passwd_sms).text
        results = json.loads(results)
        verify_code = results["data"]["verify_code"]
        return self.login_token(phone),verify_code


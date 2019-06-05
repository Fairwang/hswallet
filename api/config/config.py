#! user/bin/env
# -*- coding: utf-8 -*-
import configparser,os
class config():
    print (os.path.dirname(__file__))
    def config(self):
        config=configparser.ConfigParser()
        config.read("config.ini")
        try:
            config.add_section("phones")#添加节
            config.set("phones","phone","15833330035")
            # config.add_section("phones")#添加节
            # config.set("phone","15833330035")

        except configparser.DuplicateSectionError:
            print ("section phones already exists")

        config.write(open("config.ini","w"))

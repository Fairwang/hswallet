#!/user/bin/python
#  -*-coding: utf-8-*-
import unittest
from unittest import defaultTestLoader
import os




if __name__=='__main__':
    # unittest.main()
    test_dir1 = '.\\script\\token\\'
    print (test_dir1)
    print (os.getcwd())
    test_dir=r"F:\Users\tinyw\PycharmProjects\untitled\hswallet\api\script\token"
    discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py', top_level_dir=None)
    print (discover)
    runner = unittest.TextTestRunner()
    runner.run(discover)
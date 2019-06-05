#! user/bin/env
# -*- coding: utf-8 -*-
from hswallet.api.common.doexcel import doexcel
import os,re
class searchcases():
    def searchcases(self,wenjian):
        try:

            flist = []
            filename =os.path.dirname(os.path.dirname(__file__)) + "\\cases\\"+wenjian+"\\"        # print name
            print (filename)
            for dir, folde, file in os.walk(filename):
                for i in file:
                    t = "%s%s" % (dir, i)
                    if (re.match('wallet_*', i)) != None:
                        flist.append(t)
            print (flist)

        except IndexError as e:
            print ('Please enter a correct testcase! \n')
        else:
            excel_case = doexcel()
            for i in flist:

                cases = excel_case.readExcel(i)
                print(cases)
                self.requsets_result(cases, i)
        print ('success!')
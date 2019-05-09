#!user/bin/python
# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
"""
根据table的id属性和table中的某一个元素定位其在table中的位置
table包括表头，位置坐标都是从1开始算
tableId：table的id属性
queryContent：需要确定位置的内容
tr：【行 td：列
"""
class get_table():
    def __init__(self,driver):
        self.driver=driver
    def get_table_content(self,tableId):#传入tableID
        # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
        table_tr_list = self.driver.find_element(By.ID, tableId).find_elements(By.TAG_NAME, "tr")
        table_list = []  # 存放table数据
        for tr in table_tr_list:  # 遍历每一个tr
            # 将每一个tr的数据根据td查询出来，返回结果为list对象
            table_td_list = tr.find_elements(By.TAG_NAME, "td")
            row_list = []
            # print(table_td_list)
            for td in table_td_list:  # 遍历每一个td
                row_list.append(td.text)  # 取出表格的数据，并放入行列表里
            table_list.append(row_list)
        # print str(table_list).decode("string_escape")
        return table_list
        # 循环遍历table数据，确定查询数据的位置
        # for i in range(len(table_list)):
        #     for j in range(len(table_list[i])):
        #         # if queryContent == table_list[i][j]:
        #         #     print("%r坐标为(%r,%r)" % (queryContent, i + 1, j + 1))
        #         if td==i and tr==j:
        #             print table_list[i][j]
        #             return table_list[i][j]

# -*- coding：utf-8 -*-
# @Time   : 2020/5/30 13:18
# @Author : 田干
# @Email  : tiangan_529@163.com
# @File   : excel_handler.py

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


class ExcelHandler():
    '''excel 操作封装'''

    def __init__(self, file_path):
        self.file_path = file_path

    # 打开文件
    def open_file(self):
        workbook = openpyxl.load_workbook(self.file_path)
        self.workbook = workbook
        return workbook

    # 获取表单
    def get_sheet(self, sheet_name):
        workbook = self.open_file()
        return workbook[sheet_name]

    def read_file(self,sheet_name):
        '''读取数据'''
        sheet:Worksheet = self.get_sheet(sheet_name)
        rows = list(sheet.rows)
        data = []
        for row in rows:
            lst = []
            for cell in row:
                lst.append(cell.value)
            data.append(lst)
        keys = data[0]
        cases = []
        for values in data[1:]:
            case_dict = dict(zip(keys,values))
            cases.append(case_dict)
            self.close()
        return cases

    def write(self,sheet_name,row,column,data):
        '''写入、修改数据'''
        sheet:Worksheet = self.get_sheet(sheet_name)
        sheet.cell(row,column).value = data
        self.save()
        self.close()

    def save(self):
        self.workbook.save(self.file_path)

    def close(self):
        self.workbook.close()


if __name__ == '__main__':
    pass
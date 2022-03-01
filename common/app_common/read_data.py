# -*- coding: utf-8 -*-

import xlrd

from datetime import date, datetime

def read_excel():
    ExcelFile = xlrd.open_workbook(r'D:\Program Files\JetBrains\PyCharm Community Edition 2020.2\py-appium\data\1.xls')
# 获取目标EXCEL文件sheet名
#     print(ExcelFile.sheet_names())
# sheet2_name=ExcelFile.sheet_names()[1]
# sheet=ExcelFile.sheet_by_index(1)
    sheet = ExcelFile.sheet_by_name('Sheet2')

# 打印sheet的名称，行数，列数
#     print(sheet.name, sheet.nrows, sheet.ncols)
    rows = sheet.nrows
# 获取整行或者整列的值
#     rows = sheet.row_values(3)  # 第三行内容
#     cols = sheet.col_values(2)  # 第二列内容
#     print(cols, rows)

# 获取单元格内容
#     print(sheet.cell(1, 0).value)
#     print(sheet.cell_value(1, 2))
    for i in range(rows-1):
        # 返回第一列的数据
        return sheet.row(i)[0].value

# 打印单元格内容格式
    print(sheet.cell(1, 0).ctype)

if __name__ == '__main__':
    read_excel()
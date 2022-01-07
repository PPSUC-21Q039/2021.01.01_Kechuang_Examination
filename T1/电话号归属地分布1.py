import xlsxwriter
import xlsxreader
import xlrd
import pandas as pd
import numpy as np
from collections import Counter
from openpyxl import load_workbook
import time
import os
def address_repeat(df_address1, df_address2):
    workbook = xlsxwriter.Workbook(r'C:/Users/90550/Desktop/高发电话号归属地.xlsx')
    worksheet = workbook.add_worksheet('statistics')
    bold_format = workbook.add_format({'bold': True})
    # 将二行二列设置宽度为15(从0开始)
    worksheet.set_column(1, 1, 10)
    # 用符号标记位置，例如：A列1行
    worksheet.write('A1', '电话号归属地', bold_format)
    worksheet.write('B1', '人数', bold_format)
    row = 1
    col = 0
    for address1 in (df_address1):
        worksheet.write(row, col, address1)
        row += 1
    row = 1
    for number in (df_address2):
        worksheet.write(row, col+1, number)
        row += 1

    # --------生成图表并插入到excel---------------
    # 创建一个柱状图(column chart)
    chart_col = workbook.add_chart({'type': 'column'})

    # 配置系列数据
    chart_col.add_series({
        'name': '=statistics!$B$1',
        'categories': '=statistics!$A$2:$A$71',
        'values': '=statistics!$B$2:$B$71',
        'line': {'color': 'red'},
    })
    # 设置图表的title 和 x，y轴信息
    chart_col.set_title({'name': '报案电话号归属地分布'})
    chart_col.set_x_axis({'name': '电话号归属地'})
    chart_col.set_y_axis({'name': '人数'})

    # 设置图表的风格
    chart_col.set_style(1)

    # 把图表插入到worksheet以及偏移
    worksheet.insert_chart('A15', chart_col, {'x_offset': 25, 'y_offset': 10})

    workbook.close()

if __name__ == "__main__":
    # 访问文件

    reader = xlrd.open_workbook(r'C:/Users/90550/Desktop/数据结果.xls')
    sheet = reader.sheet_by_name("Sheet1")

    column2 = sheet.col_values(5)  # 统计文件中的第6列数据
    # print(column1)
    # 统计评分个数
    result = {}
    for i in set(column2):
        result[i] = column2.count(i)
    del result['非法号码']
    del result['归属地']
    data = result
    # print(data)
    # 新建列表储存图书信息Book score和Quantity信息
    addressdic = []

    for key in data:
        bookdata = {"电话号归属地": key, "人数": data[key]}
        addressdic.append(bookdata)
    df_address = pd.DataFrame(addressdic)
    df_address = df_address.sort_values('人数', ascending=False)

    a = df_address['电话号归属地'].to_string(header=False, index=False).split('\n')
    b = df_address['人数'].to_string(header=False, index=False).split('\n')
    a = [x.strip(' ') for x in a]
    b = [x.strip(' ') for x in b]
    #a = list(map(int, a))
    b = list(map(int, b))


    print(a)
    print(b)
    address_repeat(a, b)










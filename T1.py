# 第一题题目：
# 根据所给出的事故双方的当事人的身份证号，判断其身份证号是否合法，并对身份证号、电话号码进行解析（ id_validator，phonenumber）获取其年龄、户籍、目前通讯地址（电话号码所在地）。通过统计身份证号，以及所给人员的信息，对事故多发人员的户籍地、年龄、居住社区，并进行可视化，对高发事故人员画像。
# 
# 注释要求：函数的第一行描述函数功能，第二行写作者，第三行描述具体思路，第四行分点完成具体实现

import phone
from id_validator import validator
import xlrd, xlwt
import openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

##################################################################################
# 函数功能：电话号码归属地查询（即目前通讯地址）
# 作者：胡文强
# 主要思路：通过 phone 库来获得电话号码信息并且提取、格式化输出为所需归属地信息
# 具体实现：
# 1. 函数获取 input_phone_number, 并将使用 phone.Phone().find() 获取具体信息，将返回值存储在 returned_phone_info 中
#    样式：{'phone': '180xxxxxxxx', 'province': '四川', 'city': 'xx', 'zip_code': 'xxxxxx', 'area_code': 'xxxx', 'phone_type': '电信'}
# 2. 之后将获取格式化的信息转为 string 类型，避免类型错误
# 3. 之后用 split 以 ',' 将返回值分隔成多个部分，取第 2 部分 (从零开始计算，故取 1): 'province': '四川', 与第 3 部分：'city': 'xx',
# 4. 分别用 split 处理得到参数的具体值并去除单引号（replace()）和空格（strip()），然后相加得到最终需要的归属地信息
def get_phone_information_address(input_phone_number):
    returned_phone_info = phone.Phone().find(input_phone_number)
    returned_phone_info_address = str(returned_phone_info).split(',')[1].split(':')[1].replace("'","").strip() + str(returned_phone_info).split(',')[2].split(':')[1].replace("'","").strip()
    return returned_phone_info_address
##################################################################################

##################################################################################
# 函数功能：根据身份证号查询年龄
# 作者：胡文强
# 主要思路：通过 id_validator 库获取身份证号码信息并且提取、格式化为所需的年龄信息（暂时强制转换为 str 类型的数值，按需修改）
# 具体实现：
# 1. 首先使用 validator.is_valid() 验证身份证号是否合法（valid)，不合法的话直接返回 -1 异常值
# 2. 通过 validator.get_info() 得到身份证号具体信息，将返回值存储在 returned_id_info 中
#    样式：{'address_code': 'xxxxxx', 'abandoned': 0, 'address': '四川省xxx', 'address_tree': ['四川省', 'xxx', 'xx'], 'age': 19, 'birthday_code': '2003-08-08', 'constellation': '狮子座', 'chinese_zodiac': '未羊', 'sex': 1, 'length': 18, 'check_bit': '0'}
# 3. 之后将 returned_id_info 强制转换为 string 型变量，通过 split() 使用','对字符串进行分隔，取第7部分（由0开始计算，故值为6）
# 4. 然后将提出出来的值再次 split()，取第二部分，并通过 strip() 去除空格，之后返回 string 类型的年龄值
def get_id_information_age(input_id_number):
    if validator.is_valid(str(input_id_number)):
        returned_id_info = validator.get_info(str(input_id_number))
        returned_id_info_age = str(returned_id_info).split(',')[6].split(':')[1].strip()
        return str(returned_id_info_age)
    else:
        return -1
##################################################################################

##################################################################################
# 函数功能：根据身份证号查询户籍地址
# 作者：胡文强
# 主要思路：通过 id_validator 库获取身份证号码信息并且提取、格式化为所需的户籍信息（暂时强制转换为 str 类型的数值，按需修改）
# 具体实现：
# 1. 首先使用 validator.is_valid() 验证身份证号是否合法（valid)，不合法的话直接返回 -1 异常值
# 2. 通过 validator.get_info() 得到身份证号具体信息，将返回值存储在 returned_id_info 中
#    样式：{'address_code': 'xxxxxx', 'abandoned': 0, 'address': '四川省xxx', 'address_tree': ['四川省', 'xxx', 'xx'], 'age': 19, 'birthday_code': '2003-08-08', 'constellation': '狮子座', 'chinese_zodiac': '未羊', 'sex': 1, 'length': 18, 'check_bit': '0'}
# 3. 之后将 returned_id_info 强制转换为 string 型变量，通过 split() 使用','对字符串进行分隔，取第3部分（由0开始计算，故值为2）
# 4. 然后将提出出来的值再次 split()，取第二部分，由于数值存在单引号，故使用 replace() 将其替换为 NULL，并通过 strip() 去除空格，之后返回 string 类型的户籍地址
def get_id_information_address(input_id_number):
    if validator.is_valid(str(input_id_number)):
        returned_id_info = validator.get_info(str(input_id_number))
        returned_id_info_address = str(returned_id_info).split(',')[2].split(':')[1].replace("'","").strip()
        return returned_id_info_address
    else:
        return -1
##################################################################################

# 以下为废代码

# 函数功能：获取一整列的值（主要用于身份证号提取）
# 作者：胡文强
# 主要思路：用 xlrd 循环获取该列信息
# 具体实现：略
# def get_excel_column_data(input_excel_name, input_excel_workbook, input_excel_column, input_excel_start_row):
#     data = xlrd.open_workbook(input_excel_name)
#     table = data.sheet_by_index(input_excel_workbook)
#     excel_column_data = [str(table.cell_value(i, input_excel_column)) for i in range(input_excel_start_row, table.nrows)]
#     return excel_column_data

# if __name__ == "__main__":
#     id = get_excel_column_data('考试数据.xls', 0, 7, 1)
#     for extract in id:
#         id_address = str(id_address) + str(get_id_information_address(str(extract)))
#     print(id_address)

# if __name__ == "__main__":
#     id_number = ''
#     print(get_id_information_address(id_number))
#     print(get_id_information_age(id_number))

##################################################################################
# 函数功能：提取某一特定区域的值（主要提取身份证号码和电话号）
# 作者：孟昊阳
# 主要思路：
# 具体实现
###################################### 为保证美观，被胡文强提到首行了
# import openpyxl
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from pandas import Series, DataFrame
######################################

if __name__ == "__main__": # 被胡文强提到了主函数里面
    # 引入考试数据
    df = pd.read_excel("./考试数据.xls") # 被胡文强改为了相对路径
    # 对身份证一列进行数据提取
    ID_get = df['Unnamed: 7'].to_string(header=False, index=False).split('\n')
    ID_get = ID_get[1:]
    AGE_list = pd.DataFrame() # 建造一个空列表
    # 将身份证提取并作年龄处理
    for ID in (ID_get):
        if (get_id_information_age(ID) != '-1'):
            AGE = get_id_information_age(ID)
        else:
            AGE = 'error!'
        AGE_list = AGE_list.append(pd.DataFrame({'Age': [AGE]}), ignore_index=True)

    #######################################################################
    # #将年龄的字符串放入空列表中，并创建数组写入excel
    # result_excel = pd.read_excel('./数据结果.xls') # 被胡文强改为了相对路径
    # AGE_list.to_excel(result_excel)
    # result_excel.save()
    #######################################################################

    # 2022.01.03 将以上部分替换为了以下的
    #将年龄的字符串放入空列表中，并创建数组写入excel
    AGE_list.to_excel(r'./数据结果.xls', index = False, header=True)

##################################################################################
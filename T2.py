# 第二题题目：
# 根据标注地点从地图API获取其具体坐标

import urllib
import json
from requests.api import request

# from bs4 import BeautifulSoup
# import re
# import json
# import pycurl
# from io import BytesIO
# import requests

##################################################################################
# 函数功能：调取高德地图API获得信息
# 作者：胡文强
# 主要思路：通过获取的数据，构造URL并通过requests库向高德地图 API 访问得到返回值，再进行数据处理得到有效信息
# 具体实现：
# 1. 获取值：
#   1. returned_information_format: 返回信息的类型：json 还是 xml，我觉得json更分别分析
#   2. input_x, input_y: 输入的 GPS 的 X、Y 坐标
#   3. input_key: 用户 Key
#   4. result_radius: 查询的半径
#   5. returned_information_kind: 是返回所有的结果（all）还是单个（base）
# 2. 通过 urllib 的 request 来调取API得到返回值，如果正常则返回 string 类型的 returned_result，如果有异常则返回 string 类型的 '-1'
# 3. 将返回值给别的函数（get_processed_location）处理，得到所需数据
# 备注：通过孟浩阳的高德地图账号申请到 key 为：aad49afa17b46e85e060bbe252f25a80
def get_location(returned_information_format, input_x, input_y, input_key, returned_information_kind):
    # Url example: https://restapi.amap.com/v3/geocode/regeo?output=xml&location=116.310003,39.991957&key=<用户的key>&radius=1000&extensions=all (all/base)
    url = 'https://restapi.amap.com/v3/geocode/regeo?output=' + str(returned_information_format).strip() + 'xml&location=' + str(input_x).strip() + ',' + str(input_y).strip() + '&key=' + str(input_key).strip() + '&radius=1000' + '&extensions=' + str(returned_information_kind).strip()
    try:
        returned_result = urllib.request.urlopen(url).read()
        returned_result = returned_result.decode()
        returned_result = str(returned_result)
        return returned_result
    except:
        return '-1'
    #############################################################
    # try:
    #     # returned_result = requests.get(url, timeout=300)
    #     returned_result = urllib3.urlopen(url)
    #     return returned_result
    # except:
    #     return -1
    # with urllib.request.urlopen(url) as response:
    #     returned_result = response.read()
    #     returned_result.encode(encoding='utf-8',errors='strict')
    #     return returned_result
    #############################################################
    #############################################################
    # 以下可行但是会乱码
    # try:
    #     returned_result = pycurl.Curl()
    #     returned_result.setopt(pycurl.URL, url) 
    #     returned_result.setopt(pycurl.SSL_VERIFYPEER, False)
    #     returned_result.perform()
    #     returned_result.encode(encoding='utf-8',errors='strict')
    #     #returned_result.encode('gb2312') 
    #     return returned_result
    # except:
    #     return -1
    #############################################################
##################################################################################

##################################################################################
# 函数功能：处理通过地图API获取到的json信息得到地址输出
# 作者：胡文强
# 主要思路：先进行校验，若收录则对信息进行处理，若无法得到任何结果则返回 “未收录”
# 具体实现：
# 1. 进行校验，若 return_result 不为 -1 （即网络正常，可访问）则开始处理：
#   1. 将 returned_result 转为json数据
#   2. 从中提取出 regeocode 中的 formatted_address 项，如果失败返回 “error: 坐标有误！”
# 2. 若为 -1 则返回结果 “error: 网络错误！”
def get_processed_location(returned_result):
    if (returned_result != '-1'):
        try:
            temp = json.loads(returned_result)
            processed_location = temp["regeocode"]["formatted_address"]
            return processed_location
        except:
            return 'error: 坐标有误！'
    else:
        return 'error: 网络错误！'


if __name__ == "__main__":
    result = get_location('json', '119.944296584982', '30.097262635875', 'aad49afa17b46e85e060bbe252f25a80', 'base')
    print(get_processed_location(result))
    
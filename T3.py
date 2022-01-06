import re
import urllib
import json
from requests.api import request

# 函数功能：向高德地图发送请求，得到反馈
# 函数的返回值：完整的返回的 json 格式的数据
# 孟昊阳高德地图申请到的 Key：aad49afa17b46e85e060bbe252f25a80
def get_path(start_gps_x, start_gps_y, end_gps_x, end_gps_y, user_key):
    # URL Example: https://restapi.amap.com/v3/direction/driving?origin=116.481028,39.989643&destination=116.465302,40.004717&extensions=all&output=xml&key=<用户的key>
    if (str(start_gps_x).strip() != 'NaN' and str(start_gps_y).strip() != 'NaN' and str(end_gps_y).strip() != 'NaN' and str(end_gps_y).strip() != 'NaN'):
        url = 'https://restapi.amap.com/v3/direction/driving?origin=' + str(start_gps_x).strip() + ',' + str(start_gps_y).strip() + '&destination=' + str(end_gps_x).strip() + ',' + (end_gps_y).strip() + '&extensions=all&output=json&key=' + str(user_key).strip()
        try:
            returned_result = urllib.request.urlopen(url).read()
            returned_result = returned_result.decode()
            returned_result = str(returned_result)
            return returned_result
        except:
            return '-1'
    else:
        return '-2'

# 函数功能：处理返回的 json 格式数据，得到路程时间
# 函数的返回值：字符串类型的所需时间
def time_cost(returned_result):
    if (returned_result != '-1' and returned_result != '-2'):
        temp = json.loads(returned_result)
        processed_path_time = temp["route"]["paths"]
        duration = str(processed_path_time).split(',')[1].split(":")[1].strip()
        return str(duration)
    elif (returned_result == '-1'):
        return 'error: 网络错误!'
    elif (returned_result == '-2'):
        return 'error: 输入坐标不全!'

# 具体思路：本次处警后，如果没有警情就待着，有的话就朝新的警情开进，如果中途有了新的警情，不理会；到目的地后，开始处理，如果有多个新警情，优先赶往最近的。
def path_processing():
    return 

if __name__ == "__main__":
    result = get_path('119.944296584982','30.097262635875','119.945421709799','30.045358805853','aad49afa17b46e85e060bbe252f25a80')
    print(time_cost(result))
    global_time = 0

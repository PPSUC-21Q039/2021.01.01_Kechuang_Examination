import urllib
import json
from requests.api import request

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
    
def time_cost(returned_result):
    if (returned_result != '-1' and returned_result != '-2'):
        temp = json.loads(returned_result)
        processed_path_time = temp["route"]["paths"]["duration"]
        return processed_path_time
    elif (returned_result == '-1'):
        return 'error: 网络错误!'
    elif (returned_result == '-2'):
        return 'error: 输入坐标不全!'

def process_path(returned_result):
    if (returned_result != '-1' and returned_result != '-2'):
        temp = json.loads(returned_result)
        processed_path_origin = temp["route"]["paths"]
        return 
    elif (returned_result == '-1'):
        return 'error: 网络错误!'
    elif (returned_result == '-2'):
        return 'error: 输入坐标不全!'


if __name__ == "__main__":
    result = get_path('119.944296584982','30.097262635875','119.945421709799','30.045358805853','aad49afa17b46e85e060bbe252f25a80')
    result_path = process_path(result)
    print(result_path)
    print(str(time_cost(result_path)))
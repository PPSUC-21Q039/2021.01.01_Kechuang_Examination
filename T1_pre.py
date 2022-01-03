# from bs4.element import ResultSet
# from id_validator import validator
# import requests
# from bs4 import  BeautifulSoup

# def getHTMLText(url):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return  r.text
#     except Exception as err:
#         print(err)

# def parsePhoneData(html):
#     soup = BeautifulSoup(html, "html.parser")
#     table = soup.find('table',attrs={'style':'border-collapse: collapse'})
#     phoneInfoList = []  # 用于存放电话信息

#     for td in table.find_all('td',attrs={'class':'tdc2'}):
#         rst = td.getText()\
#             .replace('\xa0','&&')\
#             .replace(' 测吉凶(新)','')\
#             .replace(' 更详细的..','')
 
#         if '移动' in rst:
#             rst = '中国移动'
#         elif '联通' in rst:
#             rst = '中国联通'
#         elif '电信' in rst:
#             rst = '中国电信'
#         phoneInfoList.append(rst)
#     return phoneInfoList

# def get_phone_number_information(input_phone_number):
#     url = "http://www.ip138.com:8080/search.asp?mobile=" + input_phone_number + "&action=mobile"
#     html = getHTMLText(url)
#     result = parsePhoneData(html)
#     return result.append(result)

#def id_number_validation(input_id_number):
    

# if __name__ == "__main__":
#     results = get_phone_number_information('18095052066')
#     print(results)
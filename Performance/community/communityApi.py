import requests
import json
from Config.Confagent import mainConfig
from Config.JsonAgent import Getjsondata
'''
调用接口，去拿后台统计信息
'''
# 直接可以用开始时间、结束时间拿到所有要的信息
def community_backend_api(params,configpath):
    config = mainConfig(configpath)
    url_json_path = config.Getconfig('Web-config','community_backend_url_jsonpath')
    cookie_json_path = config.Getconfig('Web-config','community_backend_cookie_jsonpath')
    header_json_path = config.Getconfig('Web-config','community_backend_Header_jsonpath')

    Url = Getjsondata('floor-stats-url',url_json_path)
    cookies = Getjsondata('cookies',cookie_json_path)
    Headers = Getjsondata('floor-stats-headers',header_json_path)
    Params = params
    # 获取接口返回信息：错误点1
    response = requests.get(url=Url, params=Params, headers=Headers, cookies=cookies)
    jsdata = json.loads(response.text)
    return jsdata


if __name__ == '__main__':
    # params = {'starttime':'2023-08-23',
    #           'endtime':'2023-09-01'}
    params = {'actionUrl': 'chanjet/floor-stats',
              'order':'asc',
              'offset':0,
              'limit':20,
              'startdata':'',
             'enddata':'',
              'engineer':'熊嘉颖'}
    configpath = 'D:\Project-support\config.ini'
    res = community_backend_api(params,configpath)
    print(res)
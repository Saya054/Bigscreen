import requests
import json
from Config.Confagent import mainConfig
from Config.JsonAgent import Getjsondata
'''
调用接口，去拿后台统计信息
'''
# 直接可以用开始时间、结束时间拿到所有要的信息
def webim_backend_api(configpath,payload):
    config = mainConfig(configpath)
    url_json_path = config.Getconfig('Web-config','webim_url_jsonpath')
    head_json_path = config.Getconfig('Web-config','webim_Header_jsonpath')
    # person_id = config.Getconfig('Web-config','hotline_person_jsonpath')
    Url = Getjsondata('url',url_json_path)
    print("url",Url)
    Headers = Getjsondata('headers',head_json_path)
    Params = {"source":"CS",
              "token":"izZ75JUa_ssWdsdZk69t",
              "lang":"zh-cn"}
    print("header", Headers)
    # 获取接口返回信息：错误点1
    response = requests.post(url=Url, params=Params, headers=Headers,data = payload)
    jsdata = json.loads(response.text)
    return jsdata


if __name__ == '__main__':

    payload ='''{  "ids": [ 1610834],
              "statAt": ["2023-10-27 00:00:00","2023-10-27 23:59:59"],
              "permission": ["all","queue","order","opinion"],
              "orderField": null,
              "orderType": "none",
              "pageNum": 1,
              "pageSize": 20,
              "displayForbiddenAgent": 0,
              "timeStrategy":"work"
              }'''
    configpath = 'D:\Bigscreen\config.ini'
    a =webim_backend_api(configpath,payload)
    b = "呼入：快速路由满意度-不满意评价数"
    # ["rows"][0]
    # ["cc_agent_callin__callin_answered_count"].replace(',','')
    print(a)

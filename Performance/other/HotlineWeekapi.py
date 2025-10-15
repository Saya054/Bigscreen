import requests
import json
from Config.Confagent import mainConfig
from Config.JsonAgent import Getjsondata


def hotlineweek_backend_api(configpath,payload):
    config = mainConfig(configpath)
    head_json_path = config.Getconfig('Web-config','hotline_Header_jsonpath')
    # person_id = config.Getconfig('Web-config','hotline_person_jsonpath')
    Url = "https://cbi.udesk.cn/backend/report/cc_queue_callin"
    Headers = Getjsondata('headers',head_json_path)
    Params = {"source":"CS",
              "callType":"openlinapp",
              "token":"izZ75JUa_ssWdsdZk69t",
              "lang":"zh-cn"}
    # 获取接口返回信息：错误点1
    response = requests.post(url=Url, params=Params, headers=Headers,data = payload)
    jsdata = json.loads(response.text)
    return jsdata


if __name__ == '__main__':

    payload ='''{  "ids": [],
                    "statAt": ["2023-10-25 00:00:00","2023-10-25 23:59:59"],
                    "permission": ["all","queue","ivr"],
                     "orderField": null,
                     "orderType": "none",
                     "pageNum": 1,
                      "pageSize": 20,
                      "displayForbiddenAgent": 0
              }'''
    configpath = 'D:\Project-support\config.ini'
    a =hotlineweek_backend_api(configpath,payload)
    b = "呼入：快速路由满意度-不满意评价数"
    # ["rows"][0]
    # ["cc_agent_callin__callin_answered_count"].replace(',','')
    print(a)
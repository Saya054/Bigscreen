import requests
import json
from Config.Confagent import mainConfig
from Config.JsonAgent import Getjsondata


def webimweek_backend_api(configpath,payload):
    config = mainConfig(configpath)
    head_json_path = config.Getconfig('Web-config','webim_week_jsonpath')
    # person_id = config.Getconfig('Web-config','hotline_person_jsonpath')
    Url = "https://cbi.udesk.cn/backend/report/im_queue_workload"
    Headers = Getjsondata('headers',head_json_path)
    Params = {"source":"CS",
              "token":"izZ75JUa_ssWdsdZk69t",
              "lang":"zh-cn"}
    # 获取接口返回信息：错误点1
    response = requests.post(url=Url, params=Params, headers=Headers,data = payload)
    jsdata = json.loads(response.text)
    return jsdata



if __name__ == '__main__':

    payload =''' {"ids": ["queue_company_35190_group_1504684","queue_company_35190_group_1504384","queue_company_35190_group_1504394","queue_company_35190_group_1504574","queue_company_35190_group_1504414","queue_company_35190_group_1504594","queue_company_35190_group_1504604","queue_company_35190_group_1504624"],
                                 "statAt": ["2023-11-03 00:00:00","2023-11-03 23:59:59"],
                                "permission": ["all","queue","order","opinion"],
                                 "orderField": null,
                                 "orderType": "none",
                                 "pageNum": 1,
                                  "pageSize": 20,
                                  "displayForbiddenAgent": 0,
                                 "timeStrategy":"work"
                              }'''
    configpath = 'D:\\bigdata\\config.ini'
    a =webimweek_backend_api(configpath,payload)["data"]["rows"]
    # ["rows"]
    # ["data"]["header"]["dimensions"]
    # ["rows"][0]
    # ["cc_agent_callin__callin_answered_count"].replace(',','')
    print(a)
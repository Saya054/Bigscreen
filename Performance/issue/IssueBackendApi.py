import requests
import json
from Config.Confagent import mainConfig
from Config.JsonAgent import Getjsondata
'''
调用接口，去拿后台统计信息
'''
# 直接可以用开始时间、结束时间拿到所有要的信息
def issue_backend_api(params,configpath,model):
    config = mainConfig(configpath)
    url_json_path = config.Getconfig('Web-config', 'issue_backend_url_jsonpath')
    cookie_json_path = config.Getconfig('Web-config', 'issue_backend_cookie_jsonpath')
    header_json_path = config.Getconfig('Web-config', 'issue_backend_Header_jsonpath')

    Url = Getjsondata(model+'-url',url_json_path)
    cookies = Getjsondata('cookies',cookie_json_path)
    Headers = Getjsondata(model+'-headers',header_json_path)
    Params = params
    # 获取接口返回信息：错误点1
    response = requests.get(url=Url, params=Params, headers=Headers, cookies=cookies)
    jsdata = json.loads(response.text)
    return jsdata


if __name__ == '__main__':
    # params = {'starttime':'2023-08-23',
    #           'endtime':'2023-09-01'}
    model = 'supporter-statics'
    params = {'actionUrl':'/stats-serviceplat/supporter-statics',
                'support_org':'5a40954db154952db179f45c',
              'supporter':'5e0d4a5d90fa1924b908803d',
              'startday':'2023-09-13',
             'endday':'2023-10-13',
              'page':1}
    model = 'support-scores'
    params = {'actionUrl': '/stats/support-scores',
              'order' :'asc',
              'offset':0,
              'limit':10,
              'org_id': '5a40954db154952db179f45c',
              'support_id': '5e0d4a5d90fa1924b908803d',
              'startdate': '2023-09-13',
              'enddate': '2023-10-13'}
    configpath = 'D:\Project-support\config.ini'
    res = issue_backend_api(params,configpath,model)
    print(res)
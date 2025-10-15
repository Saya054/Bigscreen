import requests
import json
from Config.Confagent import mainConfig
from Config.JsonAgent import Getjsondata

'''
调用接口，去拿问题信息
'''
# 直接可以用开始时间、结束时间拿到所有要的信息
def issue_charse(params,configpath):
    config = mainConfig(configpath)
    support_json_path = config.Getconfig('Web-config','issue_func_jsonpath')
    Url = Getjsondata('url',support_json_path)
    cookies = Getjsondata('cookies',support_json_path)
    Headers = Getjsondata('headers',support_json_path)
    Params = params
    # 获取接口返回信息：错误点1
    response = requests.get(url=Url, params=Params, headers=Headers, cookies=cookies)
    jsdata = json.loads(response.text)
    return jsdata


if __name__ == '__main__':
    # params = {'starttime':'2023-08-23',
    #           'endtime':'2023-09-01'}
    params = {'desc': '支持网'}
    configpath = 'I:\Project-support\config.ini'
    res = issue_charse(params,configpath)
    print(res)
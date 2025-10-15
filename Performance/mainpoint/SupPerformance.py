import time

from Performance.issue.IssueBackendApi import issue_backend_api
from Performance.issue.IssueBackendProcessing import IssueBackendData
from Performance.hotline.hotlineApi import hotline_backend_api
from Performance.hotline.hotlineProcesing import HotlineData
from Performance.other.HotlineWeekapi import hotlineweek_backend_api
from Performance.other.HotlineWeekProcessing import Hotlineweek
from Performance.other.WebIMWeekapi import webimweek_backend_api
from Performance.other.WebIMWeekProcessing import Webimweek
from Performance.webim.webimApi import webim_backend_api
from Performance.webim.webimProcessing import WebimData
from Performance.community.communityApi import community_backend_api
from Performance.community.communityProcesing import CommunityData

from Config.JsonAgent import Getjsondata,Getjsonkey
from Config.Confagent import mainConfig
from Base.Basefun.basicfunc import get_current_week,get_current_season

class ChanjetSupporterPerformance(object):
    def __init__(self,name,starttime,endtime,configpath):
        self._name = name
        self._sttime = starttime
        self._edtime = endtime
        self._cfpath = configpath
    def GetIssueCountPerformance(self):
        model = 'support-works'
        config = mainConfig(self._cfpath)
        person_json_path = config.Getconfig('Web-config', 'issue_backend_person_jsonpath')
        supportinfo= Getjsondata(self._name,person_json_path)
        support_org = supportinfo["support_org"]
        supporter = supportinfo["supporter"]
        params = {'actionUrl': '/stats/support-works',
                  "order":"asc",
                  "offset":0,
                  "limit":10,
                  'startdate': f'{self._sttime}' + " 00:00:00",
                  'enddate': f'{self._edtime}' + " 23:59:59",
                  'org_id': f'{support_org}',
                  'support_id': f'{supporter}'}
        jsondata = issue_backend_api(params,self._cfpath,model)
        infos =  IssueBackendData(jsondata)
        isscper =[infos.GetbasicCountdata()[0],infos.GetbasicCountdata()[1][0]]
        return isscper
    def GetIssueScorePerformance(self):
        model = 'support-scores'
        config = mainConfig(self._cfpath)
        person_json_path = config.Getconfig('Web-config', 'issue_backend_person_jsonpath')
        supportinfo = Getjsondata(self._name, person_json_path)
        support_org = supportinfo["support_org"]
        supporter = supportinfo["supporter"]
        params = {'actionUrl': '/stats/support-scores',
                  'order': 'asc',
                  'offset': 0,
                  'limit': 10,
                  'org_id': f'{support_org}',
                  'support_id': f'{supporter}',
                  'startdate': f'{self._sttime}',
                  'enddate': f'{self._edtime}'}
        jsondata = issue_backend_api(params, self._cfpath, model)
        print(jsondata)
        infos = IssueBackendData(jsondata)
        isssper = [infos.GetbasicScoredata()[0], infos.GetbasicScoredata()[1][0]]
        return isssper
    def GetHotLinePerformance(self):
        config = mainConfig(self._cfpath)
        person_json_path = config.Getconfig('Web-config', 'hotline_person_jsonpath')
        supporterid = str(Getjsondata(self._name, person_json_path))
        time_st = str(self._sttime) +' 00:00:00'
        time_ed = str(self._edtime)+' 23:59:59'
        if supporterid != "None":
            payload ='{'+f'''"ids": [{supporterid}],
                          "statAt": ["{time_st}","{time_ed}"],
                          "permission": ["all","queue","ivr"],
                          "orderField": null,
                          "orderType": "none",
                          "pageNum": 1,
                          "pageSize": 20,
                          "displayForbiddenAgent": 0
                       '''+'}'
            jsondata = hotline_backend_api(self._cfpath,payload)
            infos = HotlineData(jsondata)
            hotper = [infos.Getbasicdata()[0], infos.Getbasicdata()[1][0]]
        else:
            hotper = [['工程师','呼入数','呼入接通数','不满意评价数','满意评价数'], [self._name,"0","0","0","0"]]
        return hotper
    def GetHotlineWeekPer(self):
        config = mainConfig(self._cfpath)
        weekdays= get_current_week()
        weekinfors = []
        for i in weekdays:
            time_st = str(i) + ' 00:00:00'
            time_ed = str(i) + ' 23:59:59'
            payload = '{' + f'''"ids": [],
                                 "statAt": ["{time_st}","{time_ed}"],
                                 "permission": ["all","queue","ivr"],
                                 "orderField": null,
                                 "orderType": "none",
                                 "pageNum": 1,
                                 "pageSize": 20,
                                 "displayForbiddenAgent": 0
                              ''' + '}'
            jsondata = hotlineweek_backend_api(self._cfpath, payload)
            # print('jsondata',jsondata)
            weekinfors.append(Hotlineweek(jsondata).Getbasicdata())
            time.sleep(1)
        hotper = [weekdays,weekinfors]
        # print('hotper',hotper)
        return hotper
    def GetWebimPerformance(self):
        config = mainConfig(self._cfpath)
        person_json_path = config.Getconfig('Web-config', 'webim_person_jsonpath')
        supporterid = str(Getjsondata(self._name, person_json_path))
        # print("supportid",supporterid,type(supporterid))
        if supporterid != "None":
            time_st = str(self._sttime) + ' 00:00:00'
            time_ed = str(self._edtime) + ' 23:59:59'
            payload = '{' + f'''"ids": [{supporterid}],
                            "statAt": ["{time_st}","{time_ed}"],
                            "permission": ["all","queue","order","opinion"],
                            "orderField": null,
                            "orderType": "none",
                            "pageNum": 1,
                            "pageSize": 20,
                            "displayForbiddenAgent": 0,
                            "timeStrategy":"work"
                         ''' + '}'
            jsondata = webim_backend_api(self._cfpath, payload)
            infos = WebimData(jsondata)
            hotper = [infos.Getbasicdata()[0], infos.Getbasicdata()[1][0]]
        else:
            hotper = [['工程师','总对话量','有效对话数'],[self._name,"0","0"]]
        return hotper
    def GetWebimWeekPer(self):
        config = mainConfig(self._cfpath)
        weekdays= get_current_week()
        weekinfors = []
        jsonpath = config.Getconfig("Web-config", "webim_weekproduct_jsonpath")
        productlist = Getjsonkey(jsonpath)
        productkey = [Getjsondata(p, jsonpath) for p in productlist]
        productparams = str(productkey).replace("'", '"').replace(' ','')
        for i in weekdays:
            time_st = str(i) + ' 00:00:00'
            time_ed = str(i) + ' 23:59:59'
            payload = '{' + f'''"ids": {productparams},
                                 "statAt": ["{time_st}","{time_ed}"],
                                "permission": ["all","queue","order","opinion"],
                                 "orderField": null,
                                 "orderType": "none",
                                 "pageNum": 1,
                                  "pageSize": 20,
                                  "displayForbiddenAgent": 0,
                                 "timeStrategy":"work"
                              ''' + '}'
            jsondata = webimweek_backend_api(self._cfpath, payload)
            weekinfors.append(Webimweek(jsondata).Getbasicdata())
            time.sleep(1)
        hotper = [weekdays,weekinfors]
        # print('hotper',hotper)
        return hotper
    def GetComPerformance(self):
        config = mainConfig(self._cfpath)
        person_json_path = config.Getconfig('Web-config', 'community_backend_person_jsonpath')
        supporterid = str(Getjsondata(self._name, person_json_path))
        time_st = str(self._sttime) + ' 00:00:00'
        time_ed = str(self._edtime) + ' 23:59:59'
        # print("supportid", supporterid, type(supporterid))
        if supporterid != "None":
            params = {'actionUrl': 'chanjet/floor-stats',
                      'order': 'asc',
                      'offset': 0,
                      'limit': 20,
                      'startdata': f'{time_st}',
                      'enddata': f'{time_ed}',
                      'engineer': f'{supporterid}'}
            jsondata = community_backend_api(params,self._cfpath)
            # print(jsondata)
            infos = CommunityData(jsondata)
            comper = [infos.Getbasicdata()[0], infos.Getbasicdata()[1][0]]
        else:
            comper = [['工程师', '楼层数', '问题数'], [self._name, "0", "0"]]
        return comper


if __name__ =='__main__':
    configpath = 'D:\\bigdata\\config.ini'
    name = '黄雪婷'
    starttime = '2023-11-06'
    endtime ='2023-11-06'
    p = ChanjetSupporterPerformance(name,starttime,endtime,configpath)
    print(p.GetComPerformance())




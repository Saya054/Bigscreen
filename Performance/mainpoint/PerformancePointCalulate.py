from Performance.mainpoint.SupPerformance import ChanjetSupporterPerformance
from Performance.community.communityPerformance import CommunityPoint
from Performance.issue.IssueBackPerformance import IssueBackPoint
from Performance.webim.webimPerformance import WebimPoint
from Performance.hotline.hotlinePerformance import HotlinePoint
from Base.Basefun.basicfunc import get_current_season
from Config.Confagent import mainConfig
from Config.JsonAgent import Getjsondata

def GetSeasonPerformance(configpath,name):
    # 基础信息（公用的）
    config = mainConfig(configpath)
    startdate = get_current_season()[1]
    enddate = get_current_season()[2]
    quarter = 'Q'+str(get_current_season()[0])
    otherperson = config.Getconfig("Other-config","other_person_jsonpath")
    otherjson = config.Getconfig("Other-config","otherbase_jsonpath")+'\\'+quarter+'\\'+'otherperformance.json'
    # 获取总的实例
    mainPerformance= ChanjetSupporterPerformance(name, startdate, enddate, configpath)
    #计算社区
        # 总的社区floors
    floors = mainPerformance.GetComPerformance()[1][1]
    Compoint = CommunityPoint(floors)
    #计算支持网
    issues = mainPerformance.GetIssueCountPerformance()[1][2]
        # 5分数
    good = mainPerformance.GetIssueScorePerformance()[1][2]
        #2\1分数
    bad  = int(mainPerformance.GetIssueScorePerformance()[1][5])+int(mainPerformance.GetIssueScorePerformance()[1][6])
    Isspoint = IssueBackPoint(issues,good,bad)
    # 计算热线
    hotlines = mainPerformance.GetHotLinePerformance()[1][2]
    good = mainPerformance.GetHotLinePerformance()[1][4]
    bad = mainPerformance.GetHotLinePerformance()[1][3]
    Hotpoint = HotlinePoint(hotlines,good,bad)
    # 计算社群
        #获取人名
    othername = Getjsondata(name,otherperson)
        #获取每日绩效数
    otherperday = int(Getjsondata(othername,otherjson)["每日绩效要求"])
    othercomwechat = int(Getjsondata(othername,otherjson)["企业微信值班天数"])
    Wecompoint = otherperday * othercomwechat
    #回拨
    Huibopoint = int(Getjsondata(othername,otherjson)["回拨加分"])
    #商机
    Shangjipoint =  int(Getjsondata(othername,otherjson)["商机加分"])
    #培训
    Uptnpoint = int(Getjsondata(othername, otherjson)["UP提能加分"])
    Insidefnpoint = int(Getjsondata(othername, otherjson)["内部赋能加分"])
    Partnerfnpoint = int(Getjsondata(othername, otherjson)["伙伴赋能加分"])
    #案例
    Examplepoint = int(Getjsondata(othername, otherjson)["案例加分"])
    #语料
    Yuliaopoint = int(Getjsondata(othername, otherjson)["语料加分"])
    #其他加分
    Kaoshipoint = int(Getjsondata(othername, otherjson)["季度考试加分"])
    Chutipoint = int(Getjsondata(othername, otherjson)["出题加分"])
    Otherpluspoint  = int(Getjsondata(othername, otherjson)["其他加分"])
    # 其他扣分
    Otherreducepoint = int(Getjsondata(othername, otherjson)["其他扣分"])
    # 计算总分
    MainPoint = Compoint + Isspoint + Hotpoint + Wecompoint + Huibopoint + Shangjipoint + Uptnpoint + Insidefnpoint + Partnerfnpoint + Examplepoint + Yuliaopoint + Kaoshipoint + Chutipoint + Otherpluspoint- Otherreducepoint
    # 计算完成度
    workday = int(Getjsondata(othername, otherjson)["工作日"])
    mainpercent = round(MainPoint/(otherperday*workday),2)
    title = ["工程师","绩效总分","绩效完成度"]
    dataframe = [name,MainPoint,mainpercent]
    return [title,dataframe]

def GetSeasonPerformanceDateFrame(configpath,name):
    # 基础信息（公用的）
    config = mainConfig(configpath)
    startdate = get_current_season()[1]
    enddate = get_current_season()[2]
    quarter = 'Q'+str(get_current_season()[0])
    season =str(get_current_season()[0])
    otherperson = config.Getconfig("Other-config","other_person_jsonpath")
    otherjson = config.Getconfig("Other-config","otherbase_jsonpath")+'\\'+quarter+'\\'+'otherperformance.json'
    # 获取总的实例
    mainPerformance= ChanjetSupporterPerformance(name, startdate, enddate, configpath)
    #计算社区
        # 总的社区floors
    floors = mainPerformance.GetComPerformance()[1][1]
    Compoint = CommunityPoint(floors)
    # 计算社区IM
    validata = mainPerformance.GetWebimPerformance()[1][2]
    IMpoint = WebimPoint(validata)
    #计算支持网
    issues = mainPerformance.GetIssueCountPerformance()[1][2]
        # 5分数
    good = mainPerformance.GetIssueScorePerformance()[1][2]
        #2\1分数
    bad  = int(mainPerformance.GetIssueScorePerformance()[1][5])+int(mainPerformance.GetIssueScorePerformance()[1][6])
    Isspoint = IssueBackPoint(issues,good,bad)
    # 计算热线
    hotlines = mainPerformance.GetHotLinePerformance()[1][2]
    good = mainPerformance.GetHotLinePerformance()[1][4]
    bad = mainPerformance.GetHotLinePerformance()[1][3]
    Hotpoint = HotlinePoint(hotlines,good,bad)
    # 计算社群
        #获取人名
    othername = Getjsondata(name,otherperson)
        #获取每日绩效数
    otherperday = int(Getjsondata(othername,otherjson)["每日绩效要求"])
    othercomwechat = int(Getjsondata(othername,otherjson)["企业微信值班天数"])
    Wecompoint = otherperday * othercomwechat
    #回拨
    Huibopoint = int(Getjsondata(othername,otherjson)["回拨加分"])
    #商机
    Shangjipoint =  int(Getjsondata(othername,otherjson)["商机加分"])
    #培训
    Uptnpoint = int(Getjsondata(othername, otherjson)["UP提能加分"])
    Insidefnpoint = int(Getjsondata(othername, otherjson)["内部赋能加分"])
    Partnerfnpoint = int(Getjsondata(othername, otherjson)["伙伴赋能加分"])
    #案例
    Examplepoint = int(Getjsondata(othername, otherjson)["案例加分"])
    #语料
    Yuliaopoint = int(Getjsondata(othername, otherjson)["语料加分"])
    #其他加分
    Kaoshipoint = int(Getjsondata(othername, otherjson)["季度考试加分"])
    Chutipoint = int(Getjsondata(othername, otherjson)["出题加分"])
    Otherpluspoint  = int(Getjsondata(othername, otherjson)["其他加分"])
    # 其他扣分
    Otherreducepoint = int(Getjsondata(othername, otherjson)["其他扣分"])
    # 计算总分
    MainPoint = Compoint + Isspoint +IMpoint+ Hotpoint + Wecompoint + Huibopoint + Shangjipoint + Uptnpoint + Insidefnpoint + Partnerfnpoint + Examplepoint + Yuliaopoint + Kaoshipoint + Chutipoint + Otherpluspoint- Otherreducepoint
    # 计算完成度
    workday = int(Getjsondata(othername, otherjson)["工作日"])
    mainpercent = round(100*(MainPoint/(otherperday*workday)),2)
    OtherTTpoint = Huibopoint+Shangjipoint+Uptnpoint+Insidefnpoint+Partnerfnpoint+Examplepoint+Yuliaopoint+Kaoshipoint+Chutipoint+Otherpluspoint-Otherreducepoint
    desirepoint = int(workday) *int(otherperday)
    title = ["工程师","绩效总分","绩效完成度"]
    dataframe = [name,season,otherperday,workday,Isspoint,IMpoint,Hotpoint,Compoint,Wecompoint,OtherTTpoint,MainPoint,desirepoint,mainpercent]
    return [title,dataframe]
def GetSeasonOtherDateFrame(configpath,name):
    # 基础信息（公用的）
    config = mainConfig(configpath)
    startdate = get_current_season()[1]
    enddate = get_current_season()[2]
    quarter = 'Q'+str(get_current_season()[0])
    season =str(get_current_season()[0])
    otherperson = config.Getconfig("Other-config","other_person_jsonpath")
    otherjson = config.Getconfig("Other-config","otherbase_jsonpath")+'\\'+quarter+'\\'+'otherperformance.json'
    # 获取总的实例
    # 计算社群
        #获取人名
    othername = Getjsondata(name,otherperson)
        #获取每日绩效数
    otherperday = int(Getjsondata(othername,otherjson)["每日绩效要求"])
    #回拨
    Huibopoint = int(Getjsondata(othername,otherjson)["回拨加分"])
    #商机
    Shangjipoint =  int(Getjsondata(othername,otherjson)["商机加分"])
    #培训
    Uptnpoint = int(Getjsondata(othername, otherjson)["UP提能加分"])
    Insidefnpoint = int(Getjsondata(othername, otherjson)["内部赋能加分"])
    Partnerfnpoint = int(Getjsondata(othername, otherjson)["伙伴赋能加分"])
    #案例
    Examplepoint = int(Getjsondata(othername, otherjson)["案例加分"])
    #语料
    Yuliaopoint = int(Getjsondata(othername, otherjson)["语料加分"])
    #其他加分
    Kaoshipoint = int(Getjsondata(othername, otherjson)["季度考试加分"])
    Chutipoint = int(Getjsondata(othername, otherjson)["出题加分"])
    Otherpluspoint  = int(Getjsondata(othername, otherjson)["其他加分"])
    # 其他扣分
    Otherreducepoint = int(Getjsondata(othername, otherjson)["其他扣分"])
    # 计算总分
    MainPoint =  Huibopoint + Shangjipoint + Uptnpoint + Insidefnpoint + Partnerfnpoint + Examplepoint + Yuliaopoint + Kaoshipoint + Chutipoint + Otherpluspoint- Otherreducepoint
    # 计算完成度
    workday = int(Getjsondata(othername, otherjson)["工作日"])
    mainpercent = round(MainPoint/(otherperday*workday),2)
    OtherTTpoint = Huibopoint+Shangjipoint+Uptnpoint+Insidefnpoint+Partnerfnpoint+Examplepoint+Yuliaopoint+Kaoshipoint+Chutipoint+Otherpluspoint-Otherreducepoint
    desirepoint = int(workday) *int(otherperday)
    title = ["工程师","绩效总分","绩效完成度"]
    dataframe = [name,season,Huibopoint,Shangjipoint,Uptnpoint,Insidefnpoint,Partnerfnpoint,Examplepoint,Yuliaopoint,Kaoshipoint,Chutipoint,Otherpluspoint,Otherreducepoint,OtherTTpoint]
    return [title,dataframe]

if __name__ =="__main__":
    name = '刘昊'
    configpath = "D:\BigScreen\config.ini"
    z =  GetSeasonPerformance(configpath,name)
    print(z)
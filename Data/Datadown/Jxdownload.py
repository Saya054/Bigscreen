from Data.Datadriver.mysqldriver import SQLDBdriver
from DCharts.DataApi import HotlineGet,IssueGet,ComGet,WebimGet,HotlineweekGet,WebimweekGet
from Base.Basefun.basicfunc import get_current_day
from Performance.mainpoint.PerformancePointCalulate import GetSeasonPerformanceDateFrame,GetSeasonOtherDateFrame
from Base.Basefun.basicfunc import tuple2list

def GetNames(host,uname,upwd,basedb):
    try:
        conn = SQLDBdriver(host, uname, upwd, basedb)
        sql = 'select pname from jx_person'
        res =conn.Query(sql)
        rs = tuple2list(res)
        return rs
    except Exception as e:
        print(e)
        return False


def UpdateHotline(host,uname,upwd,basedb,name,configpath):
    startdate = get_current_day()
    enddate = get_current_day()
    cfpath = configpath
    Hotlinedata = HotlineGet(startdate,enddate,name,cfpath)[1]
    try:
        conn = SQLDBdriver(host,uname,upwd,basedb)
        sql = f"""update jx_hotline set callin ='{Hotlinedata[1]}',callans='{Hotlinedata[2]}',callgood='{Hotlinedata[4]}',callbad = '{Hotlinedata[3]}' 
        where ipsn_id = (select id from jx_person where pname='{name}')"""
        res = conn.Exec(sql)
        print(sql)
        return True
    except Exception as e:
        print(e)
        return False

def UpdateIssue(host,uname,upwd,basedb,name,configpath):
    startdate = get_current_day()
    enddate = get_current_day()
    cfpath = configpath
    Issuedata = IssueGet(startdate,enddate,name,cfpath)[1]
    try:
        conn = SQLDBdriver(host,uname,upwd,basedb)
        sql = f"""update jx_issue set issueans ='{Issuedata[2]}'
        where ipsn_id = (select id from jx_person where pname='{name}')"""
        res = conn.Exec(sql)
        return True
    except Exception as e:
        print(e)
        return False
def UpdateCommunity(host,uname,upwd,basedb,name,configpath):
    startdate = get_current_day()
    enddate = get_current_day()
    cfpath = configpath
    Comdata = ComGet(startdate,enddate,name,cfpath)[1]
    try:
        conn = SQLDBdriver(host,uname,upwd,basedb)
        sql = f"""update jx_community set floors ='{Comdata[1]}'
        where ipsn_id = (select id from jx_person where pname='{name}')"""
        res = conn.Exec(sql)
        return True
    except Exception as e:
        print(e)
        return False

def UpdateWebim(host,uname,upwd,basedb,name,configpath):
    startdate = get_current_day()
    enddate = get_current_day()
    cfpath = configpath
    Webimdata = WebimGet(startdate,enddate,name,cfpath)[1]
    try:
        conn = SQLDBdriver(host,uname,upwd,basedb)
        sql = f"""update jx_webim set imvalidans ='{Webimdata[1]}'
        where ipsn_id = (select id from jx_person where pname='{name}')"""
        res = conn.Exec(sql)
        return True
    except Exception as e:
        print(e)
        return False

def UpdateJxTotal(host,uname,upwd,basedb,name,configpath):
    cfpath = configpath
    JxMaindata = GetSeasonPerformanceDateFrame(cfpath,name)[1]
    try:
        conn = SQLDBdriver(host,uname,upwd,basedb)
        sql = f"""update jx_statistics set season ='{JxMaindata[1]}',daypoint = '{JxMaindata[2]}',workday ='{JxMaindata[3]}',issuepoint='{JxMaindata[4]}',impoint='{JxMaindata[5]}',
        hotlinepoint = '{JxMaindata[6]}',communitypoint = '{JxMaindata[7]}',wecompoint='{JxMaindata[8]}',otherpoint = '{JxMaindata[9]}',totalpoint = '{JxMaindata[10]}',desirepoint='{JxMaindata[11]}',
        compercent = '{JxMaindata[12]}'
        where ipsn_id = (select id from jx_person where pname='{name}')"""
        res = conn.Exec(sql)
        return True
    except Exception as e:
        print(e)
        return False

def UpdateJxOther(host,uname,upwd,basedb,name,configpath):
    cfpath = configpath
    Jxotherdata = GetSeasonOtherDateFrame(cfpath,name)[1]
    try:
        conn = SQLDBdriver(host,uname,upwd,basedb)
        sql = f"""update jx_otherstat set season ='{Jxotherdata[1]}',huibopoint = '{Jxotherdata[2]}',shangjipoint ='{Jxotherdata[3]}',uptnpoint='{Jxotherdata[4]}',insidefnpoint='{Jxotherdata[5]}',
        partnerfnpoint = '{Jxotherdata[6]}',examplepoint = '{Jxotherdata[7]}',yuliaopoint='{Jxotherdata[8]}',kaoshipoint = '{Jxotherdata[9]}',chutipoint = '{Jxotherdata[10]}',opluspoint='{Jxotherdata[11]}',
        oreducepoint = '{Jxotherdata[12]}',sumpoint = '{Jxotherdata[12]}'
        where ipsn_id = (select id from jx_person where pname='{name}')"""
        res = conn.Exec(sql)
        return True
    except Exception as e:
        print(e)
        return False

def UpdateHotlineweek(host,uname,upwd,basedb,name,configpath):
    cfpath = configpath
    stdate = get_current_day()
    eddate = get_current_day()
    Hotlineweekframe = HotlineweekGet(stdate,eddate,name,cfpath)
    count = len(Hotlineweekframe[0])
    hotweekinsertdata = [[i+1,Hotlineweekframe[0][i],Hotlineweekframe[1][i][1][1],Hotlineweekframe[1][i][1][2],Hotlineweekframe[1][i][1][3].replace('%','')] for i in range(0,count)]
    try:
        for weekdayinfo in hotweekinsertdata:
            conn = SQLDBdriver(host,uname,upwd,basedb)
            sql = f"""update jx_hotlineweek  set hot_date='{weekdayinfo[1]}',callin = '{weekdayinfo[2]}',callans='{weekdayinfo[3]}',callpercent='{weekdayinfo[4]}'
            where id_day ='{weekdayinfo[0]}' 
            """
            res = conn.Exec(sql)
            print(sql)
        return True
    except Exception as e:
        print(e)
        return False
def UpdateWebIMweek(host,uname,upwd,basedb,name,configpath):
    cfpath = configpath
    stdate = get_current_day()
    eddate = get_current_day()
    WebimFrame = WebimweekGet(stdate,eddate,name,cfpath)
    count = len(WebimFrame[0])
    webimweekinsertdata = [[i+1,WebimFrame[0][i],WebimFrame[1][i][1][1],WebimFrame[1][i][1][2],WebimFrame[1][i][1][3]] for i in range(0,count)]
    try:
        for weekdayinfo in webimweekinsertdata:
            conn = SQLDBdriver(host,uname,upwd,basedb)
            sql = f"""update jx_webimweek  set im_date='{weekdayinfo[1]}',dialogcount = '{weekdayinfo[2]}',validcount='{weekdayinfo[3]}',validpercent='{weekdayinfo[4]}'
            where id_day ='{weekdayinfo[0]}' 
            """
            res = conn.Exec(sql)
            print(sql)
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    cfpath ='D:\\bigdata\\config.ini'
    host = '127.0.0.1'
    port = '3306'
    uname = 'root'
    upwd = 'root'
    name = ''
    basedb = 'jxbigdata'
    z = UpdateWebIMweek(host, uname, upwd, basedb,name,cfpath)
    print(z)

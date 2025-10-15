from Data.Datadriver.mysqldriver import SQLDBdriver
from Config.Confagent import mainConfig
from Base.Basefun.basicfunc import tuplesqldata2list
import datetime


def QueryHotline(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select cpsn_name,callin,callans,callgood,callbad from jx_hotline where callans<>'0' order by callans ASC"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            x_data = [h[0] for h in rs]
            y_data1 = [h[1] for h in rs]
            y_data2 = [h[2] for h in rs]
            y_data3 = [h[3] for h in rs]
            y_data4 = [h[4] for h in rs]
            return[x_data,y_data2,y_data3,y_data4]
        except:
            return [[],[],[],[]]
    else:
        return [[],[],[],[]]

def QueryIssue(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select cpsn_name,issueans from jx_issue where issueans<>'0' order by issueans DESC LIMIT 5"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            return rs
        except:
            return [[],[],[],[],[]]
    else:
        return [[],[],[],[],[]]
def QueryWebim(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select cpsn_name,imvalidans from jx_webim where imvalidans<>'0' order by imvalidans DESC LIMIT 5"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            return rs
        except:
            return [[],[],[],[],[]]
    else:
        return [[],[],[],[],[]]
def QueryCommunity(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select cpsn_name,floors from jx_community where floors<>'0' order by floors DESC LIMIT 5"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            return rs
        except:
            return [[],[],[],[],[]]
    else:
        return [[],[],[],[],[]]
def QueryHotlineweek(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select hot_date,callin,callans,callpercent from jx_hotlineweek  order by id_day ASC"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            fmt = lambda x: datetime.datetime.strftime(x, "%Y-%m-%d")
            x_data = [fmt(h[0]) for h in rs]
            y_data1 = [h[1] for h in rs]
            y_data2 = [h[2] for h in rs]
            y_data3 = [h[3] for h in rs]
            return[x_data,y_data1,y_data2,y_data3]
        except:
            return [[],[],[],[]]
    else:
        return [[],[],[],[]]
def QueryWebimweek(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select im_date,dialogcount,validcount,validpercent from jx_webimweek  order by id_day ASC"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            fmt = lambda x: datetime.datetime.strftime(x, "%Y-%m-%d")
            x_data = [fmt(h[0]) for h in rs]
            y_data1 = [h[1] for h in rs]
            y_data2 = [h[2] for h in rs]
            y_data3 = [h[3] for h in rs]
            return[x_data,y_data1,y_data2,y_data3]
        except:
            return [[],[],[],[]]
    else:
        return [[],[],[],[]]



def QueryKpi(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select cpsn_name,totalpoint,compercent from jx_statistics where cpsn_name not in ('徐日','曾庆慧') order by compercent DESC"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            return rs
        except:
            return [[],[],[],[],[]]
    else:
        return [[],[],[],[],[]]

def QueryTopkpi(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select cpsn_name,totalpoint,desirepoint,compercent from jx_statistics  order by compercent DESC limit 1"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            return rs
        except:
            return [[]]
    else:
        return [[]]

def QueryTophotline(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select cpsn_name,callans,callin,callgood from jx_hotline  order by callans DESC limit 1"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            return rs
        except:
            return [[]]
    else:
        return [[]]

def QueryTopissue(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select cpsn_name,issueans from jx_issue order by issueans DESC limit 1"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            return rs
        except:
            return [[]]
    else:
        return [[]]

def QueryTopwebim(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select cpsn_name,imvalidans from jx_webim order by imvalidans DESC limit 1"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            return rs
        except:
            return [[]]
    else:
        return [[]]
def QueryTopcommunity(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select cpsn_name,floors from jx_community order by floors DESC limit 1"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            return rs
        except:
            return [[]]
    else:
        return [[]]
def QueryTopstudy(cfpath):
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config", "host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    # 链接数据库:
    conn = SQLDBdriver(host, uname, upwd, basedb)
    if conn.SQLcon():
        try:
            sql ="select cpsn_name,sumpoint from jx_otherstat order by sumpoint DESC limit 1"
            res = conn.Query(sql)
            rs = tuplesqldata2list(res)
            return rs
        except:
            return [[]]
    else:
        return [[]]
if __name__=='__main__':
    cfpath = 'D:\\bigdata\\config.ini'
    a = QueryTopkpi(cfpath)
    print(a)
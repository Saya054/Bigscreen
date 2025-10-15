from Data.Datadown.Jxdownload import *
from Data.Datadriver.mysqldriver import SQLDBdriver
import schedule
from Config.Confagent import mainConfig
import logging, os
import time

def DataupdateNow(cfpath):
    print("开始测试连接...")
    # 测试链接
    config = mainConfig(cfpath)
    host = config.Getconfig("SQL-config","host")
    uname = config.Getconfig("SQL-config", "name")
    upwd = config.Getconfig("SQL-config", "password")
    basedb = config.Getconfig("SQL-config", "basedb")
    #链接数据库:
    conn = SQLDBdriver(host,uname,upwd,basedb)
    if conn.SQLcon():
        print("Mysql链接成功，开始更新信息...")
    #获取人员
        print("开始获取人员信息...")
        personlist = GetNames(host,uname,upwd,basedb)
        if personlist:
            print(f'获取人员信息成功，人员名单:{personlist}')
        #先同步热线
            print(f'开始同步信息...')
            for p in personlist:
                try:
                    hotupdate = UpdateHotline(host,uname,upwd,basedb,p,cfpath)
                    print(f"同步{p}的热线成功")
                    issupdate = UpdateIssue(host,uname,upwd,basedb,p,cfpath)
                    print(f"同步{p}的支持网成功")
                    commupdate = UpdateCommunity(host,uname,upwd,basedb,p,cfpath)
                    print(f"同步{p}的社区成功")
                    imupdate = UpdateWebim(host,uname,upwd,basedb,p,cfpath)
                    print(f"同步{p}的IM成功")
                    hotweekupdate = UpdateHotlineweek(host,uname,upwd,basedb,p,cfpath)
                    print(f"同步热线周接听成功")
                    webimweekupdate = UpdateWebIMweek(host,uname,upwd,basedb,p,cfpath)
                    print(f"同步Webim周回复成功")
                    otherjxupdate = UpdateJxOther(host,uname,upwd,basedb,p,cfpath)
                    print(f"同步{p}的学习成长成功")
                    mainjxupdate = UpdateJxTotal(host,uname,upwd,basedb,p,cfpath)
                    print(f"同步{p}的总绩效成功")
                except Exception as e:
                    print(f"同步{p}的信息失败，失败原因是{e}")
                    pass
            print("全部同步成功")
        else:
            print("人员信息丢失")
            return False
    else:
        print("mysql链接失败")
        return False




if __name__=="__main__":
    # 设置日志
    print("日志初始化")
    file_path = os.path.dirname(os.path.realpath(__file__))
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)s:%(levelname)s:%(message)s',
                        datefmt='%F %A %T',
                        handlers=[logging.FileHandler(os.path.join(file_path, 'log.txt'), encoding='utf-8', mode='a+'),
                                  logging.StreamHandler()]  ##到标准输出
                        )
    print("日志初始化完成，开始同步数据")
    cfpath = "D:\\bigdata\\config.ini"
    while True:
        DataupdateNow(cfpath)
        time.sleep(180)

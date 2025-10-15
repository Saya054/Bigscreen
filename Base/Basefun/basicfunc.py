from datetime import datetime
import os
import datetime
from datetime import timedelta

def get_current_day():
    fmt = lambda x: datetime.datetime.strftime(x, "%Y-%m-%d")
    today = datetime.date.today()
    today = fmt(today)
    return today
def get_current_week():
    fmt = lambda x: datetime.datetime.strftime(x, "%Y-%m-%d")
    today = datetime.date.today()
    monday = today - timedelta(days=today.weekday())
    weeklist = [fmt(monday + timedelta(days=i)) for i in range(7)]
    return weeklist[0:5]
# 列表按哪个元素排序(呼入接通数)
def get_current_season():
    fmt = lambda x: datetime.datetime.strftime(x, "%Y-%m-%d")
    today = datetime.date.today()
    quarter = (today.month-1)//3+1
    startmonth = 3*(quarter-1)+1
    startdate = datetime.date(today.year,startmonth,1)
    enddate = startdate.replace(month=startmonth+2)+timedelta(days = 30)
    startdate = fmt(startdate)
    enddate = fmt(enddate)
    return [quarter,startdate,enddate]
def float2persent(f):
    a = 100*f
    return str(a)+' %'
# 获取人员姓名用
# 类型转换2：把tuple转换到list
def tuple2list(Lst):
    newLst = []
    if isinstance(Lst,list):
        for a in Lst:
            if isinstance(a, tuple):
                newLst.append(a[0])
        return newLst
    else:
        return []
def tuplesqldata2list(Lst):
    newLst = []
    if isinstance(Lst, list):
        for a in Lst:
            if isinstance(a, tuple):
                eachlist = []
                for i in a:
                    eachlist.append(i)
                newLst.append(eachlist)
        return newLst
    else:
        return []

def sort_key_fun(element):
    """
    传入列表容器的元素, 返回该元素的一个表达式, 也就是按照什么规则进行排序
    按照该元素的第 1 个元素进行排序
    :param element: 列表元素
    :return:    列表元素排序依据
    """
    return element[2]
def quit_hotline_zero_key(lst):
    res = []
    for i in lst:
        if str(i[2])!='0':
            res.append(i)
    return res
def quit_issue_zero(lst):
    res = []
    for i in lst:
        if str(i[2]) != "0":
            res.append(i)
    return res
def quit_webim_zero(lst):
    res = []
    for i in lst:
        if str(i[2]) != "0":
            res.append(i)
    return res
def quit_community_zero(lst):
    res = []
    for i in lst:
        if str(i[1]) != "0":
            res.append(i)
    return res
def quit_main_zero(lst):
    res = []
    for i in lst:
        if str(i[1]) != "0":
            res.append(i)
    return res
def getToday():
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d")
    return date_str
def getListdic(lst,inx,value):
    realdic = ['T+、T1产品伙伴', '0', '0', '0', '0']
    for dic in lst:
        if str(dic[inx]) == value:
            realdic=dic
    return realdic
def Per2int(lst):
    newl = []
    for i in lst:
        i = float(str(i).replace('%',''))
        newl.append(i)
    return newl

'''
IM专用函数
'''
def combine_lst(lst):
    product = '伙伴业务支持部'
    totalaccount = 0
    valiadaccount = 0
    cusaccount = 0
    for i in lst:
        totalaccount += int(i[1])
        valiadaccount += int(i[2])
        cusaccount += int(i[3])
    valipercent = Validper(valiadaccount,totalaccount)
    newlst = [product,totalaccount,valiadaccount,valipercent,cusaccount]
    return newlst
def Validper(c1,c2):
    if c2==0:
        return 0
    else:
        return round((100*int(c1)/c2),2)
'''
对文件操作
'''
# 创建文件路径（没有就创建）
def mkdir(path):
    path = repath(path)
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        try:
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            # print("---  目录生成中...  ---")
            # print("---  OK  ---")
            return 'Create file Success'
        except Exception as e:
            # print('非法的目录名')
            return 'Invalid FileName'
    else:
        # print(f"---  {path}目录已存在！  ---")
        return 'Exists'
'''
变更名字
'''
def repath(path):
    newpath = path.replace('/','\\')
    return newpath

if __name__ =="__main__":
    a = get_current_season()
    print(a)


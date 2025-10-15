from datetime import datetime
import time
'''
基础类通用函数
'''
# 时间格式函数
def timeformat(timeint):
    ti_shift1 = datetime.fromtimestamp(timeint)
    t1_return = ti_shift1.strftime("%Y-%m-%d %H:%M")
    return t1_return
# 计算时间差的函数
def caculatetime(timeint):
    # ti_shift1 = datetime.fromtimestamp(timeint)
    timelist = convert_seconds(timeint)
    timeresult = str(timelist[0]) + '天' + str(timelist[1]) + '时' + str(timelist[2]) + '分' + str(timelist[3]) + '秒'
    return timeresult
# 根据时间秒数来计算时间数值
def convert_seconds(seconds):
    days = seconds // 86400
    hours = (seconds - days * 86400) // 3600
    minutes = (seconds - days * 86400 - hours * 3600) // 60
    seconds = seconds - days * 86400 - hours * 3600 - minutes * 60
    return [days, hours, minutes, seconds]
# 按小时来计算时间
def convert_hours(seconds):
    hours = round((seconds / 3600), 2)
    return hours

# 校验开始时间和结束时间哪个大
def compare_time(stime,etime):
    stime_int = int(datetime.strptime(stime, "%Y-%m-%d").timestamp())
    etime_int = int(datetime.strptime(etime, "%Y-%m-%d").timestamp())
    if stime_int > etime_int:
        return False
    else:
        return True
# 获取工程师答复小时
def caculate_engineer_time(timeint):
    hours = convert_hours(timeint)
    timeresult = str(hours) + '小时'
    return timeresult
# 获取创建时间（按格式来修复时间状态）
def create_time_formate(create_time):
    nowtime = int(time.time())
    if '前' not in create_time:
        return create_time
    else:
        if '秒' in create_time:
            time_degree = int(str(create_time).replace('秒前',''))
            return timeformat(nowtime-time_degree)
        elif '分钟' in create_time:
            time_degree = int(str(create_time).replace('分钟前', ''))
            return timeformat(nowtime - time_degree*60)
        elif '小时' in create_time:
            time_degree = int(str(create_time).replace('小时前', ''))
            return timeformat(nowtime - time_degree*3600)
        else:
            return create_time
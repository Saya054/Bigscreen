import time

from Config.JsonAgent import Getjsonkey
from Config.Confagent import mainConfig
from Base.Basefun.basicfunc import quit_hotline_zero_key,quit_issue_zero,quit_webim_zero,quit_community_zero,quit_main_zero,Per2int
from Performance.mainpoint.SupPerformance import ChanjetSupporterPerformance
from Performance.mainpoint.PerformancePointCalulate import GetSeasonPerformance
from pyecharts import options as opts
from pyecharts.charts import Bar,Line

#基础取数函数
# 热线
def HotlineGet(stdate,eddate,name,confpath):
    p = ChanjetSupporterPerformance(name, stdate, eddate, confpath)
    hotlineinfo= p.GetHotLinePerformance()
    time.sleep(0.5)
    return hotlineinfo
def HotlineweekGet(stdate,eddate,name,confpath):
    p = ChanjetSupporterPerformance(name, stdate, eddate, confpath)
    hotlineweekinfo = p.GetHotlineWeekPer()
    time.sleep(0.5)
    return hotlineweekinfo

def WebimweekGet(stdate,eddate,name,confpath):
    p = ChanjetSupporterPerformance(name, stdate, eddate, confpath)
    webimweekinfo = p.GetWebimWeekPer()
    time.sleep(0.5)
    return webimweekinfo
# 支持网答题数量
def IssueGet(stdate,eddate,name,confpath):
    p = ChanjetSupporterPerformance(name, stdate, eddate, confpath)
    issueinfo = p.GetIssueCountPerformance()
    time.sleep(0.5)
    return issueinfo
# 社区
def ComGet(stdate,eddate,name,confpath):
    p = ChanjetSupporterPerformance(name, stdate, eddate, confpath)
    cominfo = p.GetComPerformance()
    time.sleep(0.5)
    return cominfo
# IM
def WebimGet(stdate,eddate,name,confpath):
    p = ChanjetSupporterPerformance(name, stdate, eddate, confpath)
    webiminfos= p.GetWebimPerformance()
    time.sleep(0.5)
    return webiminfos
# 总绩效
def MainPointGet(stdate,eddate,name,confpath):
    p = ChanjetSupporterPerformance(name, stdate, eddate, confpath)
    cominfo = p.GetComPerformance()
    time.sleep(0.5)
    return cominfo
# 图标拿数据的函数(柱状图+折线图）
def HotlineFrame(stdate,eddate,confpath)-> Bar:
    conf = mainConfig(confpath)
    # 拿到人员列表
    path = conf.Getconfig("Web-config","hotline_person_jsonpath")
    persons = Getjsonkey(path)
    print(persons)
    # 获取排序的数据
    hlinfolist= [HotlineGet(stdate,eddate,i,confpath)[1] for i in persons]
    hlinfolist= quit_hotline_zero_key(hlinfolist)
    hlinfolist.sort(key=lambda x: int(x[2]))
    x_data = [h[0] for h in hlinfolist]
    y_data0 = [h[2] for h in hlinfolist]
    y_data1 = [h[4] for h in hlinfolist]
    y_data2 = [h[3] for h in hlinfolist]
    # 绘图
    return [x_data,y_data0,y_data1,y_data2]

def IssuecountFrame(stdate,eddate,confpath)-> Bar:
    conf = mainConfig(confpath)
    # 拿到人员列表
    path = conf.Getconfig("Web-config","issue_backend_person_jsonpath")
    persons = Getjsonkey(path)
    print(persons)
    # 获取排序的数据
    infolist= [IssueGet(stdate,eddate,i,confpath)[1] for i in persons ]
    infolist= quit_issue_zero(infolist)
    infolist.sort(key=lambda x: int(x[2]))
    x_data = [h[0] for h in infolist]
    y_data = [h[2] for h in infolist]
    # 绘图
    return [x_data,y_data]
def HotlineWeekFrame(stdate,eddate,confpath):
    conf = mainConfig(confpath)
    # 拿到人员列表
    path = conf.Getconfig("Web-config", "hotline_person_jsonpath")
    person = Getjsonkey(path)[0]
    # 获取排序的数据
    hlinfolist = HotlineweekGet(stdate, eddate, person, confpath)
    # print("hlinfolist[1]",hlinfolist[1])
    x_data =  hlinfolist[0]
    y_data0 = [h[1][1] for h in hlinfolist[1]]
    y_data1 = [h[1][2] for h in hlinfolist[1]]
    y_data2 = [h[1][3] for h in hlinfolist[1]]
    # # 绘图
    return [x_data, y_data0, y_data1, y_data2]
def WebimFrame(stdate,eddate,confpath):
    conf = mainConfig(confpath)
    # 拿到人员列表
    path = conf.Getconfig("Web-config", "webim_person_jsonpath")
    persons = Getjsonkey(path)
    print(persons)
    # 获取排序的数据
    infolist = [WebimGet(stdate, eddate, i, confpath)[1] for i in persons]
    infolist = quit_webim_zero(infolist)
    infolist.sort(key=lambda x: int(x[2]))
    x_data = [h[0] for h in infolist]
    y_data = [h[2] for h in infolist]
    # 绘图
    return [x_data, y_data]
def ComFrame(stdate,eddate,confpath):
    conf = mainConfig(confpath)
    # 拿到人员列表
    path = conf.Getconfig("Web-config", "community_backend_person_jsonpath")
    persons = Getjsonkey(path)
    print(persons)
    # 获取排序的数据
    infolist = [ComGet(stdate, eddate, i, confpath)[1] for i in persons]
    infolist = quit_community_zero(infolist)
    infolist.sort(key=lambda x: int(x[1]))
    x_data = [h[0] for h in infolist]
    y_data = [h[1] for h in infolist]
    # 绘图
    return [x_data, y_data]
# 当季度总绩效
def MainFrame(confpath):
    conf = mainConfig(confpath)
    # 拿到人员列表
    path = conf.Getconfig("Other-config", "other_person_jsonpath")
    persons = Getjsonkey(path)
    print(persons)
    # 获取排序的数据
    infolist = [GetSeasonPerformance(confpath,i)[1] for i in persons]
    infolist = quit_main_zero(infolist)
    infolist.sort(key=lambda x: int(x[1]))
    x_data = [h[0] for h in infolist]
    y_data = [h[1] for h in infolist]
    y_data2 = [h[2] for h in infolist]
    # 绘图
    return [x_data, y_data,y_data2]


def HotlineBar(stdate,eddate,confpath):
    hot_infos = HotlineFrame(stdate, eddate, confpath)
    hot_columns = hot_infos[0]
    hot_bar = Bar().add_xaxis(xaxis_data=hot_columns)
    # bar.height = '1800px'  # 设置高度
    # bar.width = '1800px'
    hot_data1 = hot_infos[1]
    hot_data2 = hot_infos[2]
    hot_data3 = hot_infos[3]
    hot_bar.add_yaxis(series_name="呼入接通量", y_axis=hot_data1, label_opts=opts.LabelOpts(is_show=True,color="white"))
    hot_bar.add_yaxis(series_name="满意数量", y_axis=hot_data2, label_opts=opts.LabelOpts(is_show=True,color="white"))
    hot_bar.add_yaxis(series_name="不满意数量", y_axis=hot_data3, label_opts=opts.LabelOpts(is_show=True,color="white"))
    hot_bar.set_global_opts(yaxis_opts=opts.AxisOpts(interval=0,axislabel_opts=opts.LabelOpts(rotate=0,color="white",font_size=20),
                                                     ),
                            xaxis_opts=opts.AxisOpts(interval=10,
                                                     axislabel_opts=opts.LabelOpts(rotate=0,color="white",font_size=20),
                                                     axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="white"))),
                                                    legend_opts = opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white",font_size=20))
                                                     )
    hot_bar.set_series_opts(label_opts=opts.LabelOpts(color="white",font_size=20))
    hot_bar.reversal_axis()
    return hot_bar

def HotWeeklineBar(stdate,eddate,confpath):
    hot_week_info = HotlineWeekFrame(stdate, eddate, confpath)
    # x_index
    hot_week_columns = hot_week_info[0]
    # ydata1
    hot_week_data1 = hot_week_info[1]
    hot_week_data2 = hot_week_info[2]
    hot_week_data3 = Per2int(hot_week_info[3])
    bar = (
        Bar()
        .add_xaxis(hot_week_columns)
        # 第一个y轴的值、标签、颜色
        .add_yaxis(
            "呼入量",
            hot_week_data1,
            yaxis_index=0,
            color="#5793f3",
            label_opts = opts.LabelOpts(color="white",font_size=20)
        )

        # 第二个y轴的值、标签、颜色
        .add_yaxis(
            "呼入接通量",
            hot_week_data2,
            yaxis_index=1,
            color="#FF0000",
            label_opts=opts.LabelOpts(color="white",font_size=20)
        )

        # 右纵坐标
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="电话量",
                type_="value",
                min_=0,
                max_=500,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#000000")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}",color="white",font_size=20),

            )
        )
        # 纵坐标
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="接通率",
                min_=0,
                max_=100,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} %",color="white",font_size=20),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
        .set_global_opts(
            xaxis_opts= opts.AxisOpts(interval=0, axislabel_opts=opts.LabelOpts(rotate=0,color="white",font_size=14)),
            yaxis_opts=opts.AxisOpts(
                name="电话量",
                min_=0,
                max_=500,
                position="left",
                offset=0,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#000000")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}",color="white",font_size=20),
            ),
            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white", font_size=20)),
            title_opts=opts.TitleOpts(title=""),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
        )
    )

    line = (
        Line()
        .add_xaxis(hot_week_columns)
        .add_yaxis(
            "接通率",
            hot_week_data3,
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=True,color="white",font_size=20),
            z=2
        )
    )
    bar.overlap(line)
    return bar
def IssueCountBar(stdate, eddate, confpath):
    issue_count_info = IssuecountFrame(stdate, eddate, confpath)
    issue_columns = issue_count_info[0]
    issue_bar = Bar().add_xaxis(issue_columns)
    # bar.height = '1800px'  # 设置高度
    # bar.width = '1800px'
    issue_data = issue_count_info[1]
    issue_bar.add_yaxis(series_name="答复数量", y_axis=issue_data, label_opts=opts.LabelOpts(is_show=True,color="white"))
    issue_bar.set_global_opts(xaxis_opts=opts.AxisOpts(interval=10,
                                                     axislabel_opts=opts.LabelOpts(rotate=0,color="white",font_size=20),
                                                     axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="white"))),
                                                    legend_opts = opts.LegendOpts( textstyle_opts=opts.TextStyleOpts(color="white",font_size=20)),
                              datazoom_opts=opts.DataZoomOpts(is_show=True,orient="vertical", pos_right="right"),
                              yaxis_opts=opts.AxisOpts(interval=0,axislabel_opts=opts.LabelOpts(rotate=0,color="white",font_size=20),
                                                     ))
    issue_bar.reversal_axis()
    return issue_bar
def IssueIMBar(stdate, eddate, confpath):
    webim_infos = WebimFrame(stdate, eddate, confpath)
    webim_columns = webim_infos[0]
    webim_bar = Bar().add_xaxis(webim_columns)
    # bar.height = '1800px'  # 设置高度
    # bar.width = '1800px'
    webim_data1 = webim_infos[1]
    webim_bar.add_yaxis(series_name="有效会话数", y_axis=webim_data1, label_opts=opts.LabelOpts(is_show=True,font_size=20))
    webim_bar.set_global_opts(yaxis_opts=opts.AxisOpts(interval=0, axislabel_opts=opts.LabelOpts(rotate=0,color="white",font_size=20),
                                                     axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="white"))),
                                                    legend_opts = opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white",font_size=20)),
                              xaxis_opts=opts.AxisOpts(interval=10, axislabel_opts=opts.LabelOpts(rotate=0,color="white",font_size=18)))
    webim_bar.reversal_axis()
    return webim_bar

def CommunityBar(stdate, eddate, confpath):
    community_infos = ComFrame(stdate, eddate, confpath)
    community_columns = community_infos[0]
    community_bar = Bar().add_xaxis(community_columns)
    # bar.height = '1800px'  # 设置高度
    # bar.width = '1800px'
    community_data1 = community_infos[1]
    community_bar.add_yaxis(series_name="楼层数", y_axis=community_data1, label_opts=opts.LabelOpts(is_show=True,font_size=20))
    community_bar.set_global_opts(yaxis_opts=opts.AxisOpts(interval=0, axislabel_opts=opts.LabelOpts(rotate=0,color="white",font_size=20),
                                                     axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="white"))),
                                                    legend_opts = opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white",font_size=20)),
                                  xaxis_opts=opts.AxisOpts(interval=50,max_=250,axislabel_opts=opts.LabelOpts(rotate=0,color="white",font_size=18)))
    community_bar.reversal_axis()
    return community_bar

def MainPointRank(confpath):
    Main_infos = MainFrame(confpath)
    first_name  = Main_infos[0][-1]
    first_point = Main_infos[1][-1]
    first_persent = Main_infos[2][-1]
    first = [first_name,first_point,first_persent]
    second_name = Main_infos[0][-2]
    second_point = Main_infos[1][-2]
    second_persent = Main_infos[2][-2]
    second = [second_name,second_point,second_persent]
    third_name = Main_infos[0][-3]
    third_point = Main_infos[1][-3]
    third_persent = Main_infos[2][-3]
    third = [third_name, third_point,third_persent]
    return [first,second,third]
from Base.Datafunc.timefunction import create_time_formate,timeformat,caculate_engineer_time
from datetime import datetime

class IssueData(object):
    def __init__(self,alldata):
        self.data = alldata
    def Getbasicdata(self):
        data_title =  ['提问人','公司名称','问题号','产品分类','产品线','产品版本','产品模块','问题状态','处理工程师','问题类型','数据库类型','答复方式','数据方式','提问时间','首次回复时间','首次回复耗时','首次响应时间','首次响应耗时','首次转研发时间','是否转研发','是否需要工程师掌握','最后的答复时间','最后的问题状态值','最后问答次数']
        data_frame =[[i["creator"]["name"],i["raise_org"]["name"],i["issueno"],i["product"],'软件包',i["pverion"],i["pmodule"],i["state"],i["supporter"]["name"],i["qtype"],i["dbtype"],i["replytype"],i["data_source"],i["created_at"],self.get_first_reply_time(i),self.get_first_reply_take_time(i),self.get_first_reflection(i),self.get_first_reflection_take_time(i),self.get_first_turn_time(i),self.is_turn(i)[0],self.is_turn(i)[1],self.get_last_answer(i)[0],self.get_last_answer(i)[1],self.get_last_answer(i)[2]] for i in self.data["data"]["data"] ]
        return [data_title,data_frame]
    # 获取第一次答复时间
    def get_first_reply_time(self,data_one):
        flowlogs = data_one["flowlogs"]
        if len(flowlogs) <= 1:
            return '无'
        else:
            i = 1
            while i < len(flowlogs) + 1:
                if flowlogs[i-1]["type"] == 1:
                    return create_time_formate(flowlogs[i-1]["created_at"])
                else:
                    i += 1
            return '无'
        # 首次响应时间
    def get_first_reflection(self,data_one):
        flowlogs = data_one["flowlogs"]
        if len(flowlogs) <= 1:
            return '无'
        else:
            i = 1
            while i < len(flowlogs):
                if flowlogs[i]["type"] == 1 or flowlogs[i]["type"] == 2:
                    return create_time_formate(flowlogs[i]["created_at"])
                else:
                    i += 1
            return '无'
    # 获取首次转研发时间
    def get_first_turn_time(self,data_one):
        if 'turn_dev_time' in data_one.keys():
            return timeformat(data_one["turn_dev_time"])
        else:
            return '无'
    # 获取问题是否转研发 ,是否需要工程师掌握
    def is_turn(self,data_one):
        if 'advice_support' in data_one.keys():
            if data_one["advice_support"] == 1:
                return ['是', '是']
            else:
                return ['是', '否']
        else:
            return ['否', '否']
    # 获取问题的[最后答复时间]\[最后问答数量]\[最后回复的问题状态]，用来统计绩效
    def get_last_answer(self,data_one):
        flowlogs = data_one["flowlogs"]
        # [最后问答数量]
        Qa_count = len(flowlogs)
        # [最后回复的问题状态]
        Qa_last_state = flowlogs[len(flowlogs)-1]["type"]
        #[最后回答时间]
        last_answer_Index = self.get_last_answer_index(data_one)
        if last_answer_Index == None:
            last_answer_time = '无'
        else:
            last_answer_time = create_time_formate(flowlogs[last_answer_Index]["created_at"])
        return [last_answer_time,Qa_last_state,Qa_count]
    # 获取最后问题答复的index
    def get_last_answer_index(self,data_one):
        flowlogs = data_one["flowlogs"]
        if len(flowlogs) <= 1:
            return None
        else:
            i = 1
            while i < len(flowlogs) + 1:
                if flowlogs[len(flowlogs) - i]["type"] == 1:
                    return len(flowlogs) - i
                else:
                    i += 1
            return None
    # 首次回复耗时
    def get_first_reply_take_time(self,data_one):
        if len(data_one["flowlogs"])>0:
            first_reply_time0 = self.get_first_reply_time(data_one)
            first_ask_time0 = create_time_formate(data_one["flowlogs"][0]["created_at"])
            if first_reply_time0 == '无':
                res = '无'
            else:
                first_reply_time = int(datetime.strptime(first_reply_time0, '%Y-%m-%d %H:%M').timestamp())
                first_ask_time = int(datetime.strptime(first_ask_time0, '%Y-%m-%d %H:%M').timestamp())
                res = caculate_engineer_time(first_reply_time - first_ask_time)
        else:
            res = '无'
        return res
    # 首次响应花费时间
    def get_first_reflection_take_time(self,data_one):
        if len(data_one["flowlogs"]) > 0:
            first_reflection_time0 = self.get_first_reflection(self,data_one)
            first_ask_time0 = create_time_formate(data_one["flowlogs"][0]["created_at"])
            if first_reflection_time0 == '无':
                res = '无'
            else:
                first_reflection_time = int(datetime.strptime(first_reflection_time0, '%Y-%m-%d %H:%M').timestamp())
                first_ask_time = int(datetime.strptime(first_ask_time0, '%Y-%m-%d %H:%M').timestamp())
                res = caculate_engineer_time(first_reflection_time - first_ask_time)
        else:
            res = '无'
        return res

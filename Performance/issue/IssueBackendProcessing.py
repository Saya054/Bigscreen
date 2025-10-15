
class IssueBackendData(object):
    def __init__(self, alldata):
        self.data = alldata
    def GetbasicCountdata(self):
        data_title = ['工程师','部门','答复问题数']
        data_frame = [[i['name'].replace("畅捷服务","").replace("-",""),i['org_name'],i['counts'] ]for i in self.data['data']['list']]
        return [data_title,data_frame]
    def GetbasicScoredata(self):
        data_title = ['工程师','部门','5分评分数','4分评分数','3分评分数','2分评分数','1分评分数','未评分']
        data_frame = [[i['name'].replace("畅捷服务","").replace("-",""),i['org_name'],i['score5'],i['score4'],i['score3'],i['score2'],i['score1'],i['score0'] ]for i in self.data['data']['list']]
        return [data_title,data_frame]


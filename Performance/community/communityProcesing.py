
class CommunityData(object):
    def __init__(self, alldata):
        self.data = alldata
    def Getbasicdata(self):
        data_title = ['工程师','楼层数','问题数']
        data_frame = [[i['engineer'].replace("畅捷服务","").replace("-",""),i['floor'],i['question']]for i in self.data['data']['list']]
        return [data_title,data_frame]
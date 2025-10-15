
class WebimData(object):
    def __init__(self,alldata):
        self.data = alldata
    def Getbasicdata(self):
        data_title = ['工程师','总对话量','有效对话数']
        data_frame = [[i['im_agent_workload__agent'].replace("财税",""), i['im_agent_workload__dialog_count'].replace(',',''), i['im_agent_workload__valid_dialog_count'].replace(',','')] for i in self.data["data"]["rows"]]
        return [data_title, data_frame]

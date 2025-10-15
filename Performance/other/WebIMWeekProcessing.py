from Base.Basefun.basicfunc import  getListdic
from Base.Basefun.basicfunc import combine_lst
class Webimweek(object):
    def __init__(self,alldata):
        self.data = alldata
    def Getbasicdata(self):
        data_title = ['产品线队列','总对话量','有效对话数','有效服务率','接待客户数']
        data_frame = [[i["im_queue_workload__queue"],i["im_queue_workload__dialog_count"],i["im_queue_workload__valid_dialog_count"],i["im_queue_workload__served_client_cnt"]] for i in self.data["data"]["rows"]]
        data_frame = combine_lst(data_frame)
        return [data_title, data_frame]




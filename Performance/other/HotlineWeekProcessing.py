from Base.Basefun.basicfunc import  getListdic
class Hotlineweek(object):
    def __init__(self,alldata):
        self.data = alldata
    def Getbasicdata(self):
        data_title = ['产品线队列','呼入数','呼入接通数','呼入接通率','不满意评价数','满意评价数']
        dis_key = self.GetKey("呼入：快速路由满意度-不满意评价数")
        good_key = self.GetKey("呼入：快速路由满意度-满意评价数")
        product = "T+、T1产品伙伴"
        if dis_key and good_key:
            data_frame = [[i['cc_queue_callin__queue'], i['cc_queue_callin__callin_count'].replace(',',''), i['cc_queue_callin__callin_answered_count'].replace(',',''), i['cc_queue_callin__callin_answered_rate'].replace(',',''),i[dis_key].replace(',',''),i[good_key].replace(',','')] for i in self.data["data"]["rows"]]
            # print('data_frame', data_frame)
            data_frame = getListdic(data_frame,0,product)
            # print('data_frame', data_frame)
            return [data_title, data_frame]
        else:
            if dis_key == False and good_key!=False:
                data_frame = [[i['cc_queue_callin__queue'], i['cc_queue_callin__callin_count'].replace(',', ''),i['cc_queue_callin__callin_answered_count'].replace(',', ''), i['cc_queue_callin__callin_answered_rate'].replace(',',''),'0',i[good_key].replace(',', '')] for i in self.data["data"]["rows"]]
                # print('data_frame', data_frame)
                data_frame = getListdic(data_frame, 0, product)
                # print('data_frame', data_frame)
                return [data_title, data_frame]
            elif good_key == False and dis_key != False:
                data_frame = [[i['cc_queue_callin__queue'], i['cc_queue_callin__callin_count'].replace(',', ''),i['cc_queue_callin__callin_answered_count'].replace(',', ''),i['cc_queue_callin__callin_answered_rate'].replace(',', ''), i[dis_key].replace(',', ''),"0"] for i in self.data["data"]["rows"]]
                # print('data_frame', data_frame)
                data_frame = getListdic(data_frame, 0, product)
                # print('data_frame', data_frame)
                return [data_title, data_frame]
            else:
                data_frame = [[i['cc_queue_callin__queue'], i['cc_queue_callin__callin_count'].replace(',', ''),i['cc_queue_callin__callin_answered_count'].replace(',', ''), i['cc_queue_callin__callin_answered_rate'].replace(',',''),"0","0"] for i in self.data["data"]["rows"]]
                # print('data_frame', data_frame)
                data_frame = getListdic(data_frame, 0, product)
                # print('data_frame', data_frame)
                return [data_title, data_frame]
    def GetKey(self,key):
        for infos in self.data["data"]["header"]["indicators"]:
            if str(infos["fieldTitle"]) == key:
                return infos["fieldKey"]
        return False


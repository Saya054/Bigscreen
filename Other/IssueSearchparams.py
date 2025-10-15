SearchParams={"问题编号":"issueno",
              "产品名称":"product",
              "产品版本":"pversion",
              "产品模块":"pmodule",
              "服务部门":"support_org",
              "支持工程师":"supporter",
              "单位名称":"raise_org_name",
              "办事处":"bsc_org",
              "是否远程":"need_remote",
              "是否有数据":"data_source",
              "是否转研发":"jiraid",
              "紧急程度":"important",
              "问题状态":"state",
              "问题类型":"qtype",
              "问题标题":"subject",
              "问题描述":"desc",
              "问题答复":"flowbody",
              "处理方式":"flowbodyprocess",
              "方案":"support_solution",
              "联系人":"lxrname",
              "联系电话":"lxrmobilephone",
              "联系人邮箱":"lxremail",
              "提问时间(开始)":"starttime",
              "提问时间(结束)":"endtime",
              "补丁位置(研发回复)":"txt_answer_content",
              "精准描述":"represent",
              "是否需要掌握":"advice_support",
              "问题定性":"question_type",
              "页数":"page"
}

Search_option_dict={"product":["易报税","数据修复","畅云管家","好业财","数据库损坏","T+小畅报销","T6升级T+","T+新零售2.0","电商通","新订货商城","T3升级T+","加密激活","企业认证","发票管理","友空间","云主机","T+专属云","T+Cloud","易代账财务","易代账平台","好生意","好会计","加密狗","T1系列","T6系列","其他","云产品系列","G3系列","G6系列","T+系列","T3系列"],


}



# 根据中文带出查询参数的英文
def GetSearchparam(chs_param):
    return SearchParams.get(chs_param)



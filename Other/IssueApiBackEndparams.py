backendFunctiondict={"工程师统计":"supporter-statics",
                       "产品线统计":"new-search",
                       "问题转研发统计":"issue-dev-stats",
                       "工程师问题状态统计":"support-issue-state",
                       "工程师产品线统计":"support-product-stats",
                       "工程师满意度统计":"support-scores",
                       "工程师工作量统计":"support-works"
}

ActionUrldict ={
    "supporter-statics":"/stats-serviceplat/supporter-statics",
    "new-search":"/issue-score/new-index",
    "issue-dev-stats":"/stats/issue-dev-stats",
    "support-issue-state":"/stats/support-issue-state",
    "support-product-stats":"/stats/support-product-stats",
    "support-scores":"/stats/support-scores",
    "support-works":"/stats/support-works"
}

supporter_static_param={
    "激活网页":"actionUrl",
    "部门ID": "support_org",
    "支持工程师": "supporter",
    "起始日期": "startday",
    "结束日期": "endday",
    "结果页数": "page"}

new_search_param = {
    "激活网页":"actionUrl",
    "开始时间":"bt",
    "结束时间":"et"
}

issue_dev_stats_param = {
    "激活网页":"actionUrl",
    "顺序":"order",
    "补偿(控制页数)":"offset",
    "每页记录数":"limit",
    "开始日期":"startdate",
    "结束日期":"enddate",
    "产品线":"product"
}

support_issue_state_param = {
    "激活网页":"actionUrl",
    "顺序":"order",
    "补偿(控制页数)":"offset",
    "每页记录数":"limit",
    "开始日期":"startdate",
    "结束日期":"enddate",
    "服务部门ID":"org_id",
    "工程师ID":"support_id"
}

support_product_stats_param = {
    "激活网页": "actionUrl",
    "顺序": "order",
    "补偿(控制页数)": "offset",
    "每页记录数": "limit",
    "开始日期": "startdate",
    "结束日期": "enddate",
    "服务部门ID": "org_id",
    "工程师ID": "support_id"
}

support_scores_param = {
    "激活网页": "actionUrl",
    "顺序": "order",
    "补偿(控制页数)": "offset",
    "每页记录数": "limit",
    "开始日期": "startdate",
    "结束日期": "enddate",
    "服务部门ID": "org_id",
    "工程师ID": "support_id"
}

support_works_param = {
    "激活网页": "actionUrl",
    "顺序": "order",
    "补偿(控制页数)": "offset",
    "每页记录数": "limit",
    "开始日期": "startdate",
    "结束日期": "enddate",
    "服务部门ID": "org_id",
    "工程师ID": "support_id"
}
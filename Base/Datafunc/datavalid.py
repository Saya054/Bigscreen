import re

# 检验输入是否日期
def is_valid_datetime(string):
    pattern = "^\\d{4}-\\d{2}-\\d{2}"
    if re.match(pattern, string):
        return True
    else:
        return False
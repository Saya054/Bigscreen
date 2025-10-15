import json
from Base.FileFunc.Filefunctions import repath

def Getjsondata(key,path):
    try:
        with open(repath(path),encoding='utf-8') as f:
            key_values = json.load(f)
        if key in key_values:
            value = key_values[key]
            return value
        else:
            return None
    except Exception as e:
        # print(e)
        return False
def Getjsonkey(path):
    with open(repath(path),'r',encoding='utf-8') as file:
        json_data = file.read()
    data = json.loads(json_data)
    keys = list(data.keys())
    return keys


# key = 'cookies'
# path = 'I:\\Project-support\\support.json'
# b= Getjsondata(key,path)
# print(b)
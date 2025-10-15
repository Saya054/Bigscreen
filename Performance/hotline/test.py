import requests
import json
from Config.Confagent import mainConfig
from Config.JsonAgent import Getjsondata

url = 'https://chanjet.udesk.cn/spa1/init_data'

header = {"content-type":"application/json"}

data = '''{
"email":"zengqingh@chanjet.com",
"password":"ufsoft0000"

}'''
response = requests.post(url=url, headers=header,data = data)
sdata = json.loads(response.text)
print(sdata)
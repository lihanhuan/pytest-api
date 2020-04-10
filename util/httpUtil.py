import requests
import json
from common.commonData import CommonData

class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type':'application/json;charset=UTF-8'}

    def post(self,path,data):
        host=CommonData.host             #获取全局变量host路径
        data_json=json.dumps(data)       #将python格式转为json双引号格式

        resp=self.http.post(url=host+path,
                           data=data_json,
                           headers=self.headers)
        assert resp.status_code==200
        resp_json=resp.text
        resp_dict=json.loads(resp_json)
        return resp_dict
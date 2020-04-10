import pytest
import requests
import json
from common.commonData import CommonData
from util.httpUtil import HttpUtil
import allure

http = HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def session_fixture():
        # proxies = {'http': 'http://localhost:2333'}
        # headers = {}
        # headers['Content-Type'] = 'application/json;charset=UTF-8'
        # http = requests.session()

        # resp = http.post(url="http://192.168.1.203:8083/sys/login",
        #                  proxies=proxies,
        #                  data='{"userName":"18210034706","password":"123456"}',
        #                  headers=headers)
    path="/sys/login"
    data={'userName':CommonData.mobile,
          'password':CommonData.password}
    resp=http.post(path,data)
    CommonData.token=resp['object']['token']
    print("登录成功。。。。。。。。")





















        # yield
        # headers = {}
        # headers['Content-Type'] = 'application/json;charset=UTF-8'
        # http = requests.session()
        #
        # resp = http.post(url="http://192.168.1.203:8083/sys/logout",
        #                  proxies=proxies,
        #                  headers=headers)
        # assert resp.status_code==200
        # print("退出成功")
        # return http
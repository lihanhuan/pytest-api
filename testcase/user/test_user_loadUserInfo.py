from common.commonData import CommonData
from conftest import http
import random
import allure
@allure.feature("校验用户模块")  #报告中的模块名字
class Test_sys_getUserInfo():
    @allure.story("校验成功")     #报告模块下的用例名
    def test_sys_getUserInfo(self):
        path = "/sys/getUserInfo"
        data = {'token': CommonData.token}
        resp=http.post(path,data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        # print(resp)

        path = "/user/saveOrUpdateUser"
        # nickName='13'
        # userName='13144444455'
        nickName = str(random.randint(10000000,100000000))
        userName='135'+nickName
        data = {'nickName':nickName,
                'userName':userName,
                'telNo':'',
                'email':'',
                'address':'',
                'roleIds':'',
                'regionId':1,
                'regionLevel':1}
        resp=http.post(path,data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        # print(resp)

        path = "/sys/login"
        data = {'userName':userName,
                'password': CommonData.password}
        resp = http.post(path, data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        r=resp['object']['userId']
        # print(resp)

        path = "/user/loadUserList"
        data = {"pageCurrent":1,"pageSize":10,"nickName":"","userName":"","regionId":1}
        resp = http.post(path, data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        # print(resp)
        rr=resp['object']['list'][0]['id']
        if(rr==r):
            print("success")
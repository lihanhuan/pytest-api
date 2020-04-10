from common.commonData import CommonData
from conftest import http
import allure

@allure.feature("登录模块")
class Test_login():
    @allure.story("登录成功")
    def test_login_success(self):
        path = "/sys/login"
        data = {'userName': CommonData.mobile,
                'password': CommonData.password}
        resp=http.post(path,data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        # assert resp['object']['userId']==197
        # print(resp)

    @allure.story("用户不存在")
    def test_login_fail(self):
        path = "/sys/login"
        data = {'userName': '13133451201',
                'password': CommonData.password}
        resp=http.post(path,data)
        assert resp['code']==301
        assert resp['msg']=='用户不存在'
        # print(resp)
    # def test_login_fail2(self):
    #     path = "/sys/login"
    #     data = {'userName': '',
    #             'password': CommonData.password}
    #     resp=http.post(path,data)
    #     assert resp['code']==
    #     assert resp['msg']=='用户不能为空'
    #     print(resp)
    @allure.story("用户名或密码错误")
    def test_login_fail3(self):
        path = "/sys/login"
        data = {'userName': CommonData.mobile,
                'password': '111111'}
        resp = http.post(path, data)
        assert resp['code'] == 410
        assert resp['msg'] == '用户名或密码错误'
        # print(resp)

    @allure.story("此账户禁止登录")
    def test_login_fail4(self):
        path = "/sys/login"
        data = {'userName': '',
                'password': ''}
        resp = http.post(path, data)
        assert resp['code'] == 3010
        assert resp['msg'] == '此账户禁止登录'
        # print(resp)

    @allure.story("用户不存在")
    def test_login_fail5(self):
        path = "/sys/login"
        data = {'password': CommonData.password}
        resp = http.post(path, data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'
        # print(resp)

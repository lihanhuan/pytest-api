from common.commonData import CommonData
from conftest import http
import allure
@allure.feature("修改密码模块")
class Test_change_psw():
    @allure.story("修改密码成功")
    def test_changePwd_success(self):
        path = "/sys/changePwd"
        data = {'userId':197,
                'userName': CommonData.mobile,
                'oldPwd': CommonData.password,
                'password':'123456'
                }
        resp=http.post(path,data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        print(resp)

    @allure.story("回归密码成功")
    def test_changePwd_fail(self):
        path = "/sys/changePwd"
        data = {'userId': 197,
                'userName': CommonData.mobile,
                'oldPwd': '111111',
                'password': '123456'
                }
        resp = http.post(path, data)
        assert resp['code'] == 411
        assert resp['msg'] == '旧密码错误'
        print(resp)
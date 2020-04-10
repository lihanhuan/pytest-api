import requests

# 登录
# pay_load = {"loginId":"lihanhuan","password":"123456","orgId":1}
# response = requests.post("http://dev.v3.alphacoding.cn/api/auth/login", pay_load)
# print(response.cookies)
# data = response.json()
# print(data)
# assert data["ok"] == True


# 获取最近学习动态
url = "http://dev.v3.alphacoding.cn/api/courses/v3/trends"
hearder = {'ac-token':'qp6XpOkQH98uhcO0nu3vUt_paQ_M6fEV'}
response = requests.get(url, headers = hearder)
data = response.json()
print(data)
# assert data["ok"] == True


# 打印HTTP响应消息的函数
# def printResponse(response):
#     print('\n\n-------- HTTP response * begin -------')
#     print(response.status_code)
#
#     for k, v in response.headers.items():
#         print(f'{k}: {v}')
#
#     print('')
#
#     print(response.content.decode('utf8'))
#     print('-------- HTTP response * end -------\n\n')
#
#
# # 使用session
# session = requests.session()
# pay_load = {"loginId":"lihanhuan","password":"123456","orgId":1}
# response = session.post("http://dev.v3.alphacoding.cn/api/auth/login", pay_load)
#
# printResponse(response)
#
# response = session.get("http://dev.v3.alphacoding.cn/api/courses/v3/trends")
#
# printResponse(response)

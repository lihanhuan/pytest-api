import requests

# 模拟get请求
# response = requests.get("https://www.baidu.com")
# print(response.text)

# 模拟一个post的登录请求
# pay_load = {"loginId":"lihanhuan","password":"123456","orgId":1}
# response = requests.post("http://dev.v3.alphacoding.cn/api/auth/login", pay_load)
# data = response.json()
# assert data['ok'] == True

# 模拟一个get 请求,添加一个请求头
# headers = {"ac-token":"U2S16YQ14TD_dwH8zxNPsmsKV4JIy6VB"}
# response = requests.get("http://dev.v3.alphacoding.cn/api/courses/v3/trends", headers = headers)
# data = response.json()
# assert data['ok'] == True

# 打印HTTP响应消息的函数
def printResponse(response):
    print('\n\n------HTTP response *begin--------')
    print(response.status_code)

    for k,v in response.headers.items():
        print(f'{k}:{v}')
    print(" ")

    print(response.content.decode('utf8'))
    print('\n\n------HTTP response *end--------')

# 使用session
session = requests.session()
pay_load = {"loginId":"lihanhuan","password":"123456","orgId":1}
response = session.post("http://dev.v3.alphacoding.cn/api/auth/login", pay_load)

printResponse(response)

response = session.get("http://dev.v3.alphacoding.cn/api/courses/v3/trends")
printResponse(response)
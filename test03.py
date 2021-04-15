import requests
import jsonpath
import re


def gettoken_OA(username, password):
    url = 'http://passport.t.xgimi.com/doLogin'
    datas = {'username': username, 'password': password}
    r = requests.post(url, data=datas)
    message = r.raw
    # print(message)
    s = r.headers['Set-Cookie']
    # res = re.match(r'GM_TOKEN=.*', s)
    # print(res.group())
    info = res.split(';')
    Token = info[0].split('=')[1]
    print(token)
    return Token


gettoken_OA('xiaomei.zhang', 'Zz123456')


def gettoken_Account(username, password):
    url = 'https://account.xgimi.com/pass/login'
    datas = {'username': username, 'password': password, 'loginType': '1', 'mobile': '', 'validate': '',
             'verify': 'HTMAK'}
    r = requests.post(url, data=datas)
    message = r.raw
    print(message)
    res = r.headers
    # print(res)


# gettoken_Account('susan.wu@ucpsolution.com', 'Xgimi123')
# gettoken_Account('xiaomei.zhang210@xgimi.com','Xgimi123')
# uid = info[4].split(',')[1]
# print(uid)

host = 'http://srm.t.xgimi.com/apis'


# token = gettoken_OA('xiaomei.zhang', 'Zz123456')
# print(token)


def testAuth():
    url = host + '/permission/user/auth'
    header = {'appId': 'srm', 'token': token}
    r = requests.get(url, headers=header)
    message = r.json()
    return message


# FCST明细列表
def testForecast_item(pageSize, currentPage):
    url = host + '/forecast_item/list'
    datas = {'pageSize': pageSize, 'currentPage': currentPage}
    header = {'token': token}
    r = requests.get(url, params=datas, headers=header)
    message = r.json()
    print(message)

# testForecast_item(50, 1)

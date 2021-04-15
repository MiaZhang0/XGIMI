import requests


# 获取token
def gettoken_OA(username, password):
    url = 'http://passport.t.xgimi.com/doLogin'
    datas = {'username': username, 'password': password}
    r = requests.post(url, data=datas)
    token = r.headers['Set-Cookie'].split(';')[0].split('=')[1]
    return token

if __name__ == '__main__':
    token = gettoken_OA('xiaomei.zhang', 'Xx11111!')
    print(token)

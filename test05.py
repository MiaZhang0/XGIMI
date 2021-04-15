import requests

host = 'http://srm.d.xgimi.com/apis'

token = 'lP4WEeyU9rfwjqkaQ9ys0l8N52oJoCH99FUjTvxwNilij3sID%2Fj5cjTTJyxDfT8O4uXwr1RLOYLzT5JqSKnp9vPUdnQKiG8g4PzUbnmbpjck4wtvtTy6I5Kb%2F7jJaWUsK8jGpEoz%2Fd1pWdk0Kjx2jzpdY3puTy7xAQQQL%2FFos1QLH8TV0Ieem7cXtIC8%2FJsC%2BHOJZ1cqxmzf%2FywIPe0XSw%3D%3D'


def testDelivery_noteUpdate():
    url = host + '/delivery_note/update'
    header = {'Content-Type': 'application/json', 'token': token}
    datas = {"id": 86, "deliveryNoteCode": "PC6002201216000002", "deliveryStat": "1", "deliveryStatName": "待发货",
             "receiveStat": "0", "receiveStatName": "未收货", "plantCode": "1070", "plantName": "极创工厂",
             "supplierCode": "3100", "supplierName": "扬州吉新光电有限公司", "warehouseCode": "6002",
             "warehouseName": "成都-PT-成品待检仓111 OR 1=1--", "creationDate": "2020-12-16", "expectDeliveryDate": "2020-12-23",
             "_XID": "row_302", "expressNo": "zxm11"}
    r = requests.post(url, headers=header, data=datas)
    res = r.json()
    print(res)

import requests
import sys
import threading
import time
from srm2.common.gettoken import gettoken_OA
from requests_toolbelt import MultipartEncoder

host = 'http://srm-in.t.xgimi.com/apis'
token = gettoken_OA('xiaomei.zhang', 'Xx123456')


def now():
    return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


def testForecast(forecastWeek=None, purchaserCode=None, supplierCode=None):
    print('start loop', 'at:', now())
    start = time.clock()

    url = host + '/forecast_item/list'
    datas = {'forecastWeek': forecastWeek, 'purchaserCode': purchaserCode, 'supplierCode': supplierCode}
    header = {'token': token}
    r = requests.get(url, params=datas,headers=header)
    message = r.json()

    end = time.clock()
    print("run: %f s" % (end - start))
    print(message)


# 交期回复导入
def testMRPImportFile(file, forecastWeek,forecastVersion):
    print('start loop', 'at:', now())
    start = time.clock()
    url = host + '/mrp/mrp_import_file'
    m = MultipartEncoder({'forecastWeek': forecastWeek, 'forecastVersion':forecastVersion,'file':file})
    header = {'token': token, 'Content-Type':m.content_type}
    # datas = {'forecastWeek': forecastWeek,'forecastVersion':forecastVersion}
    r = requests.post(url, data=m, headers=header)
    message = r.json()
    end = time.clock()
    print("run: %f s" % (end - start))
    print(message)


def post():
    testForecast()
    filepath = r'D:\apache-jmeter-5.3\apache-jmeter-5.3\testdata\import.txt'
    with open(filepath, 'r') as f:
        filenames = f.readlines()
        # print(filenames)
        for line in filenames:
            filename = line.strip('\n')
            # print(filename)
            file = (filename, open(filename, 'rb'), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            msg = testMRPImportFile(file=file, forecastWeek='2021年-第10周', forecastVersion='2021030502')
            print(msg)


def main():
    loop = int(sys.argv[1])
    print(loop)
    ths = int(sys.argv[2])
    print(ths)

    for i in range(loop):
        threadpool = []
        for i in range(ths):
            th = threading.Thread(target=post)
            threadpool.append(th)
        for th in threadpool:
            th.start()
        for th in threadpool:
            threading.Thread.join(th)

    post()


if __name__ == '__main__':
    main()
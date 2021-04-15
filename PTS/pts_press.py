import threading
import requests
import time
import logging
import random
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

Pass = []
Fail = []
restime = []


# class Multi_thread():
def get_info(sumpost, i, URL, param):
    for n in range(sumpost):

        try:
            r = requests.post(URL, json=param, timeout=10)
            msg = r.json()
            print(msg)
            code = msg.get('code')
            restime.append(r.elapsed.total_seconds())

            if code == 200:
                # print (res.text)
                # print(res.status_code)
                Pass.append(code)
                logger.info(str((i + 1)) + '线程的第 ' + str(n + 1) + '次请求，请求成功，状态码' + str(code))
            else:
                # print (res.status_code)
                Fail.append(code)
                logger.info(str(i * n) + '请求异常，状态码' + str(code))
            # time.sleep(10)
            # get_info()

        except Exception as e:
            print(e)


def start(sumthread, sumpost, URL, param):
    threads = []
    n_t = 1
    for i in range(sumthread):
        threads.append(threading.Thread(target=get_info(sumpost, i, URL, param), args=()))

    for t in threads:
        time.sleep(0.3)
        t.start()
    for t in threads:
        t.join()


def statistics(sumthread, sumpost, URL, param):
    start(sumthread, sumpost, URL, param)
    print('请求通过次数：', len(Pass))
    print('请求异常次数：', len(Fail))
    print('总响应最大时长：', max(restime))
    print('总响应最小时长：', min(restime))
    print('总响应时长：', sum(restime))
    print('平均响应时长：', sum(restime) / len(restime))

    if (len(Fail)) == 0:
        print(str(sumthread) + '个线程，每个线程压力请求' + str(sumpost) + '次,共计' + str(sumthread * sumpost) + '次，没有请求异常')
    else:
        print('存在 ' + str(len(Fail)) + '个，请求异常')
        print(Fail)


if __name__ == '__main__':
    # Multi_thread = Multi_thread()
    URL1 = 'http://gateway.t.xgimi.com/pts/tsp/uploadParam'  # 地址
    URL2 = 'http://gateway.t.xgimi.com/pts/tsp/getParam'
    URL3 = 'http://gateway.t.xgimi.com/pts/tsp/uploadAwb'

    testtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sumthread = 1  # 线程数
    sumpost = 1  # 每个线程请求次数

    for i in range(100):
        num = random.randint(1, 100)
        tspSn = str(num) + '@abc'
        param1 = {
            "tspSn": tspSn,
            "workOrderNo": "won001",
            "siteName": "S-A-1",
            "material": "11-22-33-44",
            "testLiner": "L1",
            "testTime": testtime,
            "testResult": "PASS",
            "testParams": {
                "again": "again-0004",
                "cgain": "cgain",
                "alength": "alength",
                "clength": "clength",
                "aconvert": "aconvert",
                "cconvert": "cconvert",
                "ver": "V3.1.1"
            }
        }
        param2 = {"tspSn": tspSn}
        param3 = {
            "ansi": 13382.723467,
            "area": {
                "height": 1,
                "width": 1
            },
            "barcode": "1023L66500640137",
            "biaoliang": {
                "Ev": 14390,
                "index": 3,
                "look": 0,
                "x": 0.291,
                "y": 0.3048
            },
            "black": {
                "Ev": 94.5,
                "x": 0.3352,
                "y": 0.346
            },
            "blue": {
                "Ev": 670,
                "x": 0.1426,
                "y": 0.0303
            },
            "colorGamut": 86.11048356510746,
            "contrast": 152,
            "duty": {
                "b": 27,
                "g": 37,
                "r": 36
            },
            "err": "",
            "green": {
                "Ev": 12000,
                "x": 0.3266,
                "y": 0.629
            },
            "huyan": {
                "Ev": 14600,
                "index": 23,
                "look": 4,
                "x": 0.2979,
                "y": 0.3144
            },
            "minliang": {
                "Ev": 15160,
                "index": 46,
                "look": 3,
                "x": 0.2967,
                "y": 0.3181
            },
            "red": {
                "Ev": 2047,
                "x": 0.6817,
                "y": 0.3037
            },
            "renzheng": {
                "Ev": 22060,
                "index": 0,
                "look": 2,
                "x": 0.3142,
                "y": 0.4669
            },
            "renzhengAnsi": 20515.8,
            "result": "ok",
            "time": "[2020/07/27 11:10:17.096]",
            "tsp": "03212802610600",
            "tspBarcode": "M100102026260321280261060000",
            "white": {
                "Ev": 14390,
                "x": 0.291,
                "y": 0.3048
            },
            "ver": str(num)
        }
        # start(sumthread, sumpost, URL1, param1)
        #
        # start(sumthread, sumpost, URL2, param2)
        #
        # start(sumthread, sumpost, URL3, param3)
        # print(param1)
        # statistics(sumthread, sumpost, URL1, param1)
        print(param2)
        statistics(sumthread, sumpost, URL2, param2)
        # print(param3)
        # statistics(sumthread, sumpost, URL3, param3)

    input('Press Enter to exit...')

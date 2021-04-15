import random
import time
import csv

def write_param():
    testtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
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
            "ver": num
        }
        with open(r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\PTS\testdata\param1.csv', 'a', encoding='utf-8') as f:
            f.write(str(param3) + '\n')
        print(param3)


def read_param1():
    with open(r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\PTS\testdata\param1.txt','r') as f1:
        param = f1.readlines()
    for i in param:
        list = i.split("\n")
        return list


def read_param2():
    with open(r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\PTS\testdata\param2.txt','r') as f2:
        param = f2.readlines()
    for i in param:
        list = i.split(",")
        return list


def read_param3():
    with open(r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\PTS\testdata\param3.txt','r') as f3:
        param = f3.readlines()
    for i in param:
        list = i.split("\n")
        return list


if __name__ == '__main__':
    list1 = read_param1()
    print(list1)
    print(len(list1))
    # list2 = read_param2()
    # print(len(list2))
    # # for i in list2:
    # #     print(i)
    list3 = read_param3()
    print(list3)
    print(len(list3))
    # for j in list3:
    #     print(j)







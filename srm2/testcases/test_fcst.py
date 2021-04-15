import unittest
from srm2.common import fcst
import time


# FCST管理
class TestFCSTCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.obj = fcst.TestFcst()
        print("----test_fcst start----")

    # FCST周列表
    def testForcastWeek_success(self):
        msg = self.obj.testForcastWeek()
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'fail')

    # FCST列表查询成功
    def testFCSTlist_success(self):
        msg = self.obj.testFCSTlist()
        msg1 = msg.get('code')
        self.assertEqual(200,msg1,'fail')

    # MRP明细查詢成功
    def testMRPlist_success(self):
        msg = self.obj.testMRPlist(forecastWeek='2021年-第10周', forecastVersion='2021030502')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, '')

    # 交期回复导入成功
    def testMRPImportFile_success(self):
        filepath = r'D:\apache-jmeter-5.3\apache-jmeter-5.3\testdata\import.txt'
        with open(filepath,'r') as f:
            filenames = f.readlines()
            # print(filenames)
            for line in filenames:
                filename = line.strip('\n')
                # print(filename)
                f2 = open(filename, 'rb')
                file = (filename, f2, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                msg = self.obj.testMRPImportFile(file=file, forecastWeek='2021年-第10周', forecastVersion='2021030502')
                print(msg)
                msg1 = msg.get('code')
                self.assertEqual(200, msg1, filename + 'fail')
                f2.close()

    # FCST明细列表查询成功
    def testForecast_success(self):
        msg = self.obj.testForecast()
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'fail')

    # MRP明细导出成功
    def testMRPDetail_success(self):
        t = time.time()
        msg = self.obj.testMRPDetail(forecastWeek='2021年-第10周',forecastVersion='2021030502',t=t)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'fail')

    # MRP汇总列表查询成功
    def testMRPSum_success(self):
        msg = self.obj.testMRPSum(forecastWeek='2021年-第10周', forecastVersion='2021030502')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'fail')

    # MRP汇总导出成功
    def testMRPExport_success(self):
        t = time.time()
        msg = self.obj.testMRPExport(forecastWeek='2021年-第10周',forecastVersion='2021030502',t=t)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'fail')

    # 导出交期回复数据
    def testMRPAsyncExport_success(self):
        t = time.time()
        msg = self.obj.testMRPAsyncExport(forecastWeek='2021年-第10周', forecastVersion='2021030502', t=t)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'fail')

    # MRP解锁
    def testMRPunlock_success(self):
        msg = self.obj.testMRPunlock(id='')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'fail')

    # FCST明细列表-确认
    def testForecastConfirm_success(self):
        ids = []
        msg = self.obj.testForecastConfirm(id=ids)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'fail')

    # FCST明细列表-取消确认
    def testForecastUnconfirm_success(self):
        ids = []
        msg = self.obj.testForecastUnconfirm(id=ids)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'fail')

    @classmethod
    def tearDownClass(self):
        print("----test_fcst end----")


if __name__ == '__main__':
    unittest.main()
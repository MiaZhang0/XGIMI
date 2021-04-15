import unittest
from srm2.testcases.test_pm import TestPMCase
from HTMLTestRunner import HTMLTestReportEN
import time

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # test_dir = r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\srm2\testcases'
    # tests = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    # suite.addTests(tests)

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPMCase))

    # runner = unittest.TextTestRunner(verbosity=2)
    d = time.strftime("%Y%m%d", time.localtime())
    report_dir = r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\srm2\report\HTMLReport' + d + '.html'
    with open(report_dir, 'wb') as f:
        runner = HTMLTestReportEN(stream=f, title='SRM2-采购订单接口测试报告', description='测试用例的执行情况', verbosity=2, tester='ZhangXiaomei')
        runner.run(suite)

import unittest
from srm2.common import soa
import requests
import time

# 采购对账、供应商对账
class TestSOACase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj = soa.TestSoa()
        cls.g = globals()
        cls.s = requests.session()
        print("----test_soa start----")

    # 供应商对账-交货明细查询成功（供应商确认状态是已确认，未生成对账单）
    def test_c(self):
        msg = self.obj.test_supDDList(companyCode='1020', postingDateBegin='2021-03-01', postingDateEnd='2021-03-17',
                                      supplierConfirmed='0', reconciliationNoteCreated='0')
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        print(msg['data']['data'][0])
        self.g["id"] = msg['data']['data'][0]['id']
        self.g["companyCode"] = msg['data']['data'][0]['companyCode']
        self.g["supplierCode"] = msg['data']['data'][0]['supplierCode']
        self.assertEqual(200, msg1, 'API067_test_supDDList_success001_fail')
        self.assertNotEqual(0, msg2, 'API067_test_supDDList_success001_fail')

    # 供应商确认状态-交货明细确认成功(前提：采购已确认)
    def test_d(self):
        list = [{'id': self.g["id"]}]
        msg = self.obj.test_DDConfirm(batchType='s', list=list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API072_test_DDConfirm_success002_fail')

    # 供应商对账 - 生成对账单成功(前提：供应商已确认)
    def test_e(self):
        list = [{'id': self.g["id"]}]
        print(list)
        msg = self.obj.test_CRN(companyCode=self.g["companyCode"], supplierCode=self.g["supplierCode"],
                                postingDateBegin='2020-12-01',
                                postingDateEnd='2021-03-17', list=list)
        print(msg)
        msg1 = msg.get('code')
        self.g["b"] = msg.get('data')
        print(self.g["b"])
        self.assertEqual(200, msg1, 'API081_test_CRN_success_fail')

    # 登记发票成功
    def test_f(self):
        re = self.g["CRN_success"]
        id = time.strftime("%Y-%m-%d", time.localtime())
        il = [{"invoiceQuantity": "1", "invoiceNo": "1", "unTaxAmount": "1", "taxAmount": "1", "invoiceDate": id}]
        msg = self.obj.test_RegInvoice(reconciliationNoteCode=re, invoiceList=il, remark='1')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API095_test_RegInvoice_success_fail')


if __name__ == '__main__':
    unittest.main()

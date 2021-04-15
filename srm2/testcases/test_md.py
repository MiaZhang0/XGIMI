import unittest
from srm2.common import md
import time


# 物料接收用例
class TestMDCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.obj = md.TestMd()
        print("----test_md start----")

    # 物料接收确认列表查询
    def test_MdList_success001(self):
        msg = self.obj.test_MdList()
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API054_test_MdList_success001_fail')
        self.assertNotEqual(0, msg2, 'API054_test_MdList_success001_fail')

    # 物料接收确认列表带条件查询
    def test_MdList_success002(self):
        msg = self.obj.test_MdList(materielCode='306-00186', purchaseOrderCode=None, supplierCode=None,
                                   materielDocumentCode=None,materielReceiveStat=None)
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API055_test_MdList_success002_fail')
        self.assertNotEqual(0, msg2, 'API055_test_MdList_success002_fail')

    # 物料接收确认列表查询暂无数据
    def test_MdList_success003(self):
        msg = self.obj.test_MdList(materielCode='www', purchaseOrderCode=None, supplierCode=None,
                                   materielDocumentCode=None,materielReceiveStat=None)
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API056_test_MdList_success003_fail')
        self.assertEqual(0, msg2, 'API056_test_MdList_success003_fail')

    # 物料接收-修改实收数量、备注成功
    def test_MdReceivedQuantity_success(self):
        d = time.strftime("%Y-%m-%d", time.localtime())
        list = [{'materielDocumentCode': '5000000962', 'materielDocumentItem': '1', 'thisTimeReceiveQuantity': '1',
                 'remark': 'zxm11接口勿动' + d}, {'materielDocumentCode': '5000000961', 'materielDocumentItem': '1',
                'thisTimeReceiveQuantity': '1', 'remark': 'zxm11接口勿动' + d}]
        msg = self.obj.test_MdReceivedQuantity(list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API057_test_MdReceivedQuantity_success_fail')

    # 物料接收-修改实收数量、备注传入空值
    def test_MdReceivedQuantity_fail(self):
        list = []
        msg = self.obj.test_MdReceivedQuantity(list)
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API058_test_MdReceivedQuantity_fail_fail')

    # 物料接收确认-导出成功
    def test_MdExport_success(self):
        msg = self.obj.test_MdExport()
        msg1 = msg.get('code')
        self.assertEqual(200,msg1,'API059_test_MdExport_success_fail')

    # 物料接收明细查询
    def test_MdItemList_success001(self):
        msg = self.obj.test_MdItemList()
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API060_test_MdItemList_success001_fail')
        self.assertNotEqual(0, msg2, 'API060_test_MdItemList_success001_fail')

    # 物料接收明细带条件查询
    def test_MdItemList_success002(self):
        msg = self.obj.test_MdItemList(purchaseOrderCode='118', supplierCode=None, materielDesc=None, materielCode=None,
                        stockOutStat=None)
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API061_test_MdItemList_success002_fail')
        self.assertNotEqual(0, msg2, 'API061_test_MdItemList_success002_fail')

    # 物料接收明细查询暂无数据
    def test_MdItemList_success003(self):
        msg = self.obj.test_MdItemList(purchaseOrderCode='qqq', supplierCode=None, materielDesc=None, materielCode=None,
                                       stockOutStat=None)
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API062_test_MdItemList_success003_fail')
        self.assertEqual(0, msg2, 'API062_test_MdItemList_success003_fail')

    # 物料接收明细导出成功
    def test_MdItemExport_success(self):
        msg = self.obj.test_MdItemExport()
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API063_test_MdItemExport_success_fail')

    @classmethod
    def tearDownClass(self):
        print("----test_md end----")


if __name__ == '__main__':
    unittest.main()

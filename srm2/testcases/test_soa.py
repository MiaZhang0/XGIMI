import unittest
from srm2.common import soa
import time


# 采购对账、供应商对账
class TestSOACase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.obj = soa.TestSoa()
        self.g = globals()
        print("----test_soa start----")

    # 采购对账-交货明细查询
    def test_purDDList_success001(self):
        msg = self.obj.test_purDDList()
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API064_test_purDDList_success001_fail')
        self.assertNotEqual(0, msg2, 'API064_test_purDDList_success001_fail')

    # 采购对账-交货明细带条件查询(采购确认状态是未确认)
    def test_a(self):
        msg = self.obj.test_purDDList(companyCode='1020', postingDateBegin='2021-02-01', postingDateEnd='2021-02-28',
                                      supplierCode=None, purchaserConfirmed='0', supplierConfirmed=None,
                                      reconciliationNoteCreated=None, purchaseOrderType=None)
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.g['a'] = msg['data']['data'][0]
        print(self.g['a'])
        print(type(self.g['a']))
        self.assertEqual(200, msg1, 'API065_test_purDDList_success002_fail')
        self.assertNotEqual(0, msg2, 'API065_test_purDDList_success002_fail')

    # 采购对账-交货明细查询暂无数据
    def test_purDDList_success003(self):
        msg = self.obj.test_purDDList(companyCode='1010', postingDateBegin='2021-02-01', postingDateEnd='2021-02-28',
                                      supplierCode=None, purchaserConfirmed=None, supplierConfirmed=None,
                                      reconciliationNoteCreated=None, purchaseOrderType=None)
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API066_test_purDDList_success003_fail')
        self.assertEqual(0, msg2, 'API066_test_purDDList_success003_fail')

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

    # 供应商对账-交货明细查询无数据
    def test_supDDList_success002(self):
        msg = self.obj.test_supDDList(companyCode='1010', postingDateBegin='2021-02-01', postingDateEnd='2021-02-28')
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API068_test_supDDList_success002_fail')
        self.assertEqual(0, msg2, 'API068_test_supDDList_success002_fail')

    # 供应商对账-交货明细查询失败
    def test_supDDList_fail(self):
        msg = self.obj.test_supDDList(companyCode='', postingDateBegin='', postingDateEnd='')
        msg1 = msg.get('code')
        self.assertEqual(500, msg1, 'API069_test_supDDList_fail_fail')

    # 采购确认状态-交货明细确认成功
    def test_b(self):
        res = self.g['a']['id']
        list = [{'id': res}]
        print(list)
        msg = self.obj.test_DDConfirm(batchType='p', list=list)
        print(msg)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API070_test_DDConfirm_success001_fail')

    # 采购确认状态-交货明细取消确认成功
    def test_DDUnconfirm_success001(self):
        id = self.g["purDDList_success002"]
        list = [{'id': id}]
        msg = self.obj.test_DDUnconfirm(batchType='p', list=list)
        print(msg)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API071_test_DDUnconfirm_success001_fail')

    # 供应商确认状态-交货明细确认成功(前提：采购已确认)
    def test_d(self):
        list = [{'id': self.g["id"]}]
        msg = self.obj.test_DDConfirm(batchType='s', list=list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API072_test_DDConfirm_success002_fail')

    # 供应商确认状态-交货明细确认失败(前提：3893采购未确认。采购未确认的交货明细，供应商无法确认)
    def test_DDConfirm_fail002(self):
        id = self.g["purDDList_success002"]
        list = [{'id': id}]
        msg = self.obj.test_DDConfirm(batchType='s', list=list)
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API073_test_DDConfirm_fail002_fail')

    # 供应商确认状态-交货明细取消确认成功（3674供应商已确认）
    def test_DDUnconfirm_success002(self):
        list = [{'id': '3674'}]
        msg = self.obj.test_DDUnconfirm(batchType='s', list=list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API074_test_DDUnconfirm_success002_fail')

    # 确认状态-交货明细确认失败(传入空值)
    def test_DDConfirm_fail(self):
        list = [{'id': '3711'}]
        msg = self.obj.test_DDConfirm(batchType='', list=list)
        print(msg)
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API075_test_DDConfirm_fail_fail')

    # 取消确认状态-交货明细取消确认失败
    def test_DDUnconfirm_fail(self):
        list = [{'id': '3711'}]
        msg = self.obj.test_DDUnconfirm(batchType='', list=list)
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API076_test_DDUnconfirm_fail_fail')

    # 供应商对账-修改备注4400000077,10行
    def test_DDRemark_success(self):
        d = time.strftime("%Y-%m-%d", time.localtime())
        msg = self.obj.test_DDRemark(id='3714', remark='zxm11接口' + d)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API077_test_DDRemark_success_fail')

    # 供应商对账-修改备注4400000077,10行
    def test_DDRemark_fail(self):
        msg = self.obj.test_DDRemark(id='', remark='')
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API078_test_DDRemark_fail_fail')

    # 交货明细导出成功
    def test_DDExport_success(self):
        msg = self.obj.test_DDExport(companyCode='1020', postingDateBegin='2021-02-01', postingDateEnd='2021-02-28',
                                     supplierCode='', purchaserConfirmed='', supplierConfirmed='',
                                     reconciliationNoteCreated='', purchaseOrderType=None)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API079_test_DDRemark_success_fail')

    # 交货明细导出失败
    def test_DDExport_fail(self):
        msg = self.obj.test_DDExport(companyCode='1020', postingDateBegin='', postingDateEnd='', supplierCode='',
                                     purchaserConfirmed='', supplierConfirmed='', reconciliationNoteCreated='',
                                     purchaseOrderType=None)
        msg1 = msg.get('code')
        self.assertEqual(500, msg1, 'API080_test_DDRemark_fail_fail')

    # 供应商对账 - 生成对账单成功(前提：供应商已确认)
    def test_e(self):
        list = [{'id': self.g["id"]}]
        print(list)
        msg = self.obj.test_CRN(companyCode=self.g["companyCode"], supplierCode=self.g["supplierCode"],
                                postingDateBegin='2020-12-01', postingDateEnd='2021-03-17', list=list)
        print(msg)
        msg1 = msg.get('code')
        self.g["b"] = msg.get('data')
        print(self.g["b"])
        self.assertEqual(200, msg1, 'API081_test_CRN_success_fail')

    # 供应商对账-生成对账单失败(前提：存在结算日期之前两个月的未生成对账单的数据)
    def test_CRN_fail001(self):
        list = [{'id': '3701'}, ]
        msg = self.obj.test_CRN(companyCode='1020', supplierCode='3139', postingDateBegin='2020-02-01',
                                postingDateEnd='2021-02-28', list=list)
        # print(msg)
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API082_test_CRN_fail001_fail')

    # 供应商对账-生成对账单失败（供应商未确认）
    def test_CRN_fail002(self):
        list = [{'id': '3701'}, ]
        msg = self.obj.test_CRN(companyCode='1020', supplierCode='3139', postingDateBegin='2020-02-01',
                                postingDateEnd='2021-02-28', list=list)
        # print(msg)
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API083_test_CRN_fail002_fail')

    # 供应商对账-生成对账单失败（传入值都为空）
    def test_CRN_fail003(self):
        list = [{'id': ''}, ]
        msg = self.obj.test_CRN(companyCode='', supplierCode='', postingDateBegin='', postingDateEnd='', list=list)
        msg1 = msg.get('code')
        self.assertEqual(500, msg1, 'API084_test_CRN_fail003_fail')

    # 供应商对账-生成对账单失败（仅结算日期为空）
    def test_CRN_fail004(self):
        list = [{'id': '1631'}, ]
        msg = self.obj.test_CRN(companyCode='', supplierCode='3139', postingDateBegin='2020-12-01',
                                postingDateEnd='2021-01-31', list=list)
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API085_test_CRN_fail004_fail')

    # 供应商对账-生成对账单失败（仅供应商为空）
    def test_CRN_fail005(self):
        list = [{'id': '1631'}, ]
        msg = self.obj.test_CRN(companyCode='1020', supplierCode='', postingDateBegin='2020-12-01',
                                postingDateEnd='2021-01-31', list=list)
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API086_test_CRN_fail005_fail')

    # 供应商对账-生成对账单失败（已生成对账单）
    def test_CRN_fail006(self):
        list = [{'id': '1636'}, ]
        msg = self.obj.test_CRN(companyCode='1020', supplierCode='3139', postingDateBegin='2020-12-01',
                                postingDateEnd='2021-01-31', list=list)
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API087_test_CRN_fail006_fail')

    # 对账单列表查询成功
    def test_RNList_success001(self):
        msg = self.obj.test_RNList()
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API088_test_RNList_success001_fail')
        self.assertNotEqual(0, msg2, 'API088_test_RNList_success001_fail')

    # 对账单列表带条件查询成功,获取生成的对账单对应的id self.g["CRN_success"]
    def test_RNList_success002(self):
        msg = self.obj.test_RNList(supplierCode=None, companyCode=None, settlementBeginDate=None,
                                   settlementEndDate=None, invoiceCreated=None,
                                    reconciliationNoteCode=self.g["CRN_success"])
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.g["RNList_success002"] = msg['data']['data'][0]['id']
        print(self.g["RNList_success002"])
        self.assertEqual(200, msg1, 'API089_test_RNList_success002_fail')
        self.assertNotEqual(0, msg2, 'API089_test_RNList_success002_fail')

    # 对账单列表查询暂无数据
    def test_RNList_success003(self):
        msg = self.obj.test_RNList(supplierCode='qqq', companyCode='1020', settlementBeginDate='2021-01-01',
                                   settlementEndDate='2021-01-31', invoiceCreated=None, reconciliationNoteCode=None)
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API090_test_RNList_success003_fail')
        self.assertEqual(0, msg2, 'API090_test_RNList_success003_fail')

    # 对账单明细列表查询成功
    def test_RNItemList_success001(self):
        msg = self.obj.test_RNItemList()
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API091_test_RNItemList_success001_fail')
        self.assertNotEqual(0, msg2, 'API091_test_RNItemList_success001_fail')

    # 对账单明细列表带条件查询成功
    def test_RNItemList_success002(self):
        msg = self.obj.test_RNItemList(supplierCode='3139', companyCode=None, settlementBeginDate=None,
                                       settlementEndDate=None,
                                       reconciliationNoteCode=None, invoiceCreated=None)
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API092_test_RNItemList_success002_fail')
        self.assertNotEqual(0, msg2, 'API092_test_RNItemList_success002_fail')

    # 对账单明细列表查询暂无数据
    def test_RNItemList_success003(self):
        msg = self.obj.test_RNItemList(supplierCode='111')
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API093_test_RNItemList_success003_fail')
        self.assertEqual(0, msg2, 'API093_test_RNItemList_success003_fail')

    # 对账单明细导出
    def test_RNItemExport_success(self):
        msg = self.obj.test_RNItemExport()
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API094_test_RNItemList_success_fail')

    # 登记发票成功
    def test_RegInvoice_success(self):
        re = self.g["CRN_success"]
        id = time.strftime("%Y-%m-%d", time.localtime())
        il = [{"invoiceQuantity": "1", "invoiceNo": "1", "unTaxAmount": "1", "taxAmount": "1", "invoiceDate": id}]
        msg = self.obj.test_RegInvoice(reconciliationNoteCode=re, invoiceList=il, remark='1')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API095_test_RegInvoice_success_fail')

    # 登记发票失败（传入空值）
    def test_RegInvoice_fail001(self):
        msg = self.obj.test_RegInvoice(reconciliationNoteCode='', invoiceList='')
        msg1 = msg.get('code')
        self.assertEqual(500,msg1,'API096_test_RegInvoice_fail001_fail')

    # 登记发票失败（已登记的对账单）
    def test_RegInvoice_fail002(self):
        id = time.strftime("%Y-%m-%d", time.localtime())
        il = [{"invoiceQuantity": "1", "invoiceNo": "1", "unTaxAmount": "1", "taxAmount": "1", "invoiceDate":id}]
        msg = self.obj.test_RegInvoice(reconciliationNoteCode='202103170004', invoiceList=il, remark='1')
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API097_test_RegInvoice_fail002_fail')

    # 发票明细分页查询成功
    def test_InvoiceItemList_success(self):
        msg = self.obj.test_InvoiceItemList(reconciliationNoteCode=self.g["CRN_success"])
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API098_test_InvoiceItemList_success_fail')

    # 采购对账-对账单确认入账成功
    def test_paConfirm_success(self):
        id = self.g["RNList_success002"]
        msg = self.obj.test_paConfirm(idList=id)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API099_test_paConfirm_success_fail')

    # 采购对账-对账单取消确认入账成功
    def test_paUnConfirm_success(self):
        id = self.g["RNList_success002"]
        msg = self.obj.test_paUnConfirm(idList=id)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API100_test_paUnConfirm_success_fail')

    # 对账单导出成功
    def test_RNExport_success(self):
        msg = self.obj.test_RNExport(reconciliationNoteCode=self.g["CRN_success"], supplierCode=None, companyCode=None,
                                     settlementBeginDate=None, settlementEndDate=None, invoiceCreated=None)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API101_test_RNExport_success_fail')

    # 批量作废对账单
    def test_UnRN_success(self):
        id = self.g["RNList_success002"]
        msg = self.obj.test_UnRN(idList=id)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API102_test_UnRN_success_fail')

    @classmethod
    def tearDownClass(self):
        print("----test_soa end----")


if __name__ == '__main__':
    unittest.main()

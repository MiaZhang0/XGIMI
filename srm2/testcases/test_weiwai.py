import unittest
from srm2.common import weiwai_new
import time
import json


# 采购订单用例
class TestWeiWaiCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.obj = weiwai_new.TestWeiWai()
        print("----test_weiwai start----")

    # 委外维修订单列表无条件查询
    def test_WeiWaiPOList_success001(self):
        msg = self.obj.test_WeiWaiPOList()
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200,msg1,'test_WeiWaiPOList_success001_fail')
        self.assertNotEqual(0,msg2,'test_WeiWaiPOList_success001_fail')

    # 委外维修订单列表带条件查询
    def test_WeiWaiPOList_success002(self):
        msg = self.obj.test_WeiWaiPOList(purchaseOrderCode='265')
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'test_WeiWaiPOList_success002_fail')
        self.assertNotEqual(0, msg2, 'test_WeiWaiPOList_success002_fail')

    # 委外维修订单列表查询暂无数据
    def test_WeiWaiPOList_success003(self):
        msg = self.obj.test_WeiWaiPOList(purchaseOrderCode='qqq')
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'test_WeiWaiPOList_success003_fail')
        self.assertEqual(0, msg2, 'test_WeiWaiPOList_success003_fail')

    # 用料回复列表无条件查询
    def test_MaterielReplyList_success001(self):
        msg = self.obj.test_MaterielReplyList()
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'test_MaterielReplyList_success001_fail')
        self.assertNotEqual(0, msg2, 'test_MaterielReplyList_success001_fail')

    # 用料回复列表带条件查询
    def test_MaterielReplyList_success002(self):
        msg = self.obj.test_MaterielReplyList(outsourceReplyCode='0003')
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'test_MaterielReplyList_success002_fail')
        self.assertNotEqual(0, msg2, 'test_MaterielReplyList_success002_fail')

    # 用料回复列表查询暂无数据
    def test_MaterielReplyList_success003(self):
        msg = self.obj.test_MaterielReplyList(outsourceReplyCode='qqqq')
        print(msg)
        msg1 = msg.get('code')
        # msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'test_MaterielReplyList_success003_fail')
        # self.assertEqual(0, msg2, 'test_MaterielReplyList_success003_fail')

    # 用料回复列表导出
    def test_MaterielReplyListExport_success(self):
        msg = self.obj.test_MaterielReplyListExport()
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'test_MaterielReplyListExport_success_fail')

    # 用料回复详情导出
    def test_MaterielReplyDetailExport_success(self):
        msg = self.obj.test_MaterielReplyDetailExport()
        msg1 = msg.get('code')
        self.assertEqual(200,msg1,'test_MaterielReplyDetailExport_success_fail')

    # 委外维修订单列表导出
    def test_WeiWaiListExport_success(self):
        msg = self.obj.test_WeiWaiListExport()
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'test_WeiWaiListExport_success_fail')

    # 用料回复模板导出(数据为空)
    def test_MaterielReplyTemplateExport_fail001(self):
        list = [{'supplierCode':'','purchaseOrderCode':'','purchaseOrderItem':'','materielCode':''}]
        msg = self.obj.test_MaterielReplyTemplateExport(replyItemList=list)
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'test_MaterielReplyTemplateExport_fail001_fail')
        self.assertIn('未查询到数据',msg2,'test_MaterielReplyTemplateExport_fail001_fail')

    # 用料回复模板导出（已回复的订单行）
    def test_MaterielReplyTemplateExport_fail002(self):
        list = [{'supplierCode':'3139','purchaseOrderCode':'4500000264','purchaseOrderItem':'10','materielCode':'251-00002'}]
        msg = self.obj.test_MaterielReplyTemplateExport(replyItemList=list)
        print(msg)
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'test_MaterielReplyTemplateExport_fail002_fail')
        self.assertIn('存在已回复订单',msg2,'test_MaterielReplyTemplateExport_fail002_fail')

    # 用料回复模板导出（不同供应商不同物料）
    def test_MaterielReplyTemplateExport_fail003(self):
        list = [{'supplierCode': '3043', 'purchaseOrderCode': '4500000266', 'purchaseOrderItem': '10',
                 'materielCode': '421-00330'}, {'supplierCode': '3139', 'purchaseOrderCode': '4500000259',
                                                'purchaseOrderItem': '30', 'materielCode': '251-00199'}]
        msg = self.obj.test_MaterielReplyTemplateExport(replyItemList=list)
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'test_MaterielReplyTemplateExport_fail003_fail')
        self.assertIn('一次只能选择单个供应商的一个物料进行回复', msg2, 'test_MaterielReplyTemplateExport_fail003_fail')

    # 用料回复模板导出（同一供应商同一物料，未回复、驳回的订单行）
    def test_MaterielReplyTemplateExport_success(self):
        list = [{'supplierCode': '3139', 'purchaseOrderCode': '4500000264', 'purchaseOrderItem': '30',
                 'materielCode': '251-00199'}, {'supplierCode': '3139', 'purchaseOrderCode': '4500000259',
                                                'purchaseOrderItem': '30', 'materielCode': '251-00199'}]
        msg = self.obj.test_MaterielReplyTemplateExport(replyItemList=list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'test_MaterielReplyTemplateExport_success_fail')

    # 用料回复导入(数据为空)
    def test_MaterielReplyImport_fail001(self):
        filepath = r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\srm2\files\委外维修用料回复1.xlsx'
        file = open(filepath, 'rb')
        msg = self.obj.test_MaterielReplyImport(file)
        file.close()
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400,msg1,'test_MaterielReplyImport_fail001_fail')
        self.assertIn('存在类别为空的订单行',msg2,'test_MaterielReplyImport_fail001_fail')

    # 用料回复导入(数据正常)
    def test_MaterielReplyImport_success(self):
        filepath = r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\srm2\files\委外维修用料回复2.xlsx'
        file = open(filepath, 'rb')
        msg = self.obj.test_MaterielReplyImport(file)
        file.close()
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'test_MaterielReplyImport_success_fail')

    # 用料回复导入(一个订单行多种类别)
    def test_MaterielReplyImport_fail002(self):
        filepath = r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\srm2\files\委外维修用料回复3.xlsx'
        file = open(filepath, 'rb')
        msg = self.obj.test_MaterielReplyImport(file)
        file.close()
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'test_MaterielReplyImport_fail002_fail')
        self.assertIn('存在一个订单行有多种维修类型',msg2,'test_MaterielReplyImport_fail002_fail')

    # 用料回复导入(不同供应商不同物料)
    def test_MaterielReplyImport_fail003(self):
        filepath = r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\srm2\files\委外维修用料回复4.xlsx'
        file = open(filepath, 'rb')
        msg = self.obj.test_MaterielReplyImport(file)
        file.close()
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'test_MaterielReplyImport_fail003_fail')
        self.assertIn('一次只能针对单个供应商的一个物料进行回复', msg2, 'test_MaterielReplyImport_fail003_fail')

    # 查看用料明细(委外维修编号为空)
    def test_MaterielReplyItem_fail001(self):
        msg = self.obj.test_MaterielReplyItem(outsourceReplyCode='')
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400,msg1,'test_MaterielReplyItem_fail001_fail')
        self.assertIn('委外维修编号不能为空',msg2,'test_MaterielReplyItem_fail001_fail')

    # 查看用料明细(委外维修编号英文字符，目前返回500)
    def test_MaterielReplyItem_fail002(self):
        msg = self.obj.test_MaterielReplyItem(outsourceReplyCode='qqq')
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'test_MaterielReplyItem_fail002_fail')

    # 查看用料明细(委外維修编号模糊数字)
    def test_MaterielReplyItem_fail003(self):
        msg = self.obj.test_MaterielReplyItem(outsourceReplyCode='0407')
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(404, msg1, 'test_MaterielReplyItem_fail003_fail')
        self.assertIn('数据不存在',msg2,'test_MaterielReplyItem_fail003_fail')

    # 查看用料明细成功
    def test_MaterielReplyItem_success(self):
        msg = self.obj.test_MaterielReplyItem(outsourceReplyCode='202104070003')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'test_MaterielReplyItem_success_fail')

    # 提交BPM审核(委外维修编号为空)
    def test_BPMCommit_fail(self):
        msg = self.obj.test_BPMCommit(outsourceReplyCode='')
        msg1 = msg.get('code')
        self.assertEqual(400,msg1,'test_BPMCommit_fail_fail')

    # 提交BPM审核成功
    def test_BPMCommit_success(self):
        msg = self.obj.test_BPMCommit(outsourceReplyCode='202104070001')
        msg1 = msg.get('code')
        self.assertEqual(200,msg1,'test_BPMCommit_success_fail')

    # 委外维修订单匹配(订单物料与组件物料都为空)
    def test_WeiWaiPOMatch_fail001(self):
        msg = self.obj.test_WeiWaiPOMatch(supplierCode='3139',maintainQuantity='100')
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'test_WeiWaiPOMatch_fail001_fail')

    # 委外维修订单匹配（供应商编号、订单数量为空）
    def test_WeiWaiPOMatch_fail002(self):
        msg = self.obj.test_WeiWaiPOMatch(supplierCode='',maintainQuantity='')
        msg1 = msg.get('code')
        self.assertEqual(500, msg1, 'test_WeiWaiPOMatch_fail002_fail')

    # 委外维修订单匹配失败（未查询到订单）
    def test_WeiWaiPOMatch_fail003(self):
        msg = self.obj.test_WeiWaiPOMatch(supplierCode='3139', maintainQuantity='100',materielCode='',maintainMaterielCode='421-00330')
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'test_WeiWaiPOMatch_fail003_fail')
        self.assertIn('没有可供回复的订单',msg2,'test_WeiWaiPOMatch_fail003_fail')

    # 委外维修订单匹配失败（最多匹配4个订单）
    def test_WeiWaiPOMatch_fail004(self):
        msg = self.obj.test_WeiWaiPOMatch(supplierCode='3139', maintainQuantity='78', materielCode='251-00009',
                                          maintainMaterielCode='')
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'test_WeiWaiPOMatch_fail004_fail')
        self.assertIn('尝试手工选择', msg2, 'test_WeiWaiPOMatch_fail004_fail')

    # 委外维修订单匹配成功
    def test_WeiWaiPOMatch_success(self):
        msg = self.obj.test_WeiWaiPOMatch(supplierCode='3043', maintainQuantity='100', materielCode='',
                                          maintainMaterielCode='421-00330')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'test_WeiWaiPOMatch_success_fail')

    # 取消用料回复失败
    def test_MaterielReplyCancel_fail(self):
        list = [{'id':38},{'id':37}]
        msg = self.obj.test_MaterielReplyCancel(outsourceReplyPlanList=list)
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'test_MaterielReplyCancel_fail_fail')

    # 取消用料回复成功
    def test_MaterielReplyCancel_success(self):
        list = [{'id': 38}]
        msg = self.obj.test_MaterielReplyCancel(outsourceReplyPlanList=list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'test_MaterielReplyCancel_success_fail')

    @classmethod
    def tearDownClass(self):
        print("----test_weiwai end----")


if __name__ == '__main__':
    unittest.main()
import unittest
from srm2.common import pm
import time
import json


# 采购订单用例
class TestPMCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.obj = pm.TestPm()
        print("----test_pm start----")

    # 采购订单列表无条件查询成功
    def test_PoList_success001(self):
        msg = self.obj.test_PoList()
        msg2 = len(msg['data']['data'])
        msg1 = msg.get('code')
        # if (res == 200) and msg2 != 0:
        #     print('PI001_test_PoList_success001_success')
        # else:
        #     print('API001_test_PoList_success001_fail')
        self.assertEqual(200, msg1, 'API001_test_PoList_success001_fail')
        self.assertNotEqual(0, msg2, 'API001_test_PoList_success001_fail')
        time.sleep(1)

    # 采购订单列表有条件查询成功
    def test_PoList_success002(self):
        msg = self.obj.test_PoList('45', '1', '3139', '2021-02-22', '2021-02-22', '1020', 'Z14')
        msg2 = len(msg['data']['data'])
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API002_test_PoList_success002_fail')
        self.assertNotEqual(0, msg2, 'API002_test_PoList_success002_fail')
        time.sleep(1)

    # 采购订单列表查询暂无数据
    def test_PoList_success003(self):
        msg = self.obj.test_PoList('555', '1', '3139', '2021-02-22', '2021-02-22', '1020', 'Z14')
        msg2 = len(msg['data']['data'])
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API003_test_PoList_success003_fail')
        self.assertEqual(0, msg2, 'API003_test_PoList_success003_fail')

    # 采购订单列表打印--已确认4500000080
    def test_PoPrint_success(self):
        msg = self.obj.test_PoPrint('659')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API004_test_PoPrint_success_fail')

    # 采购订单列表打印-待确认
    def test_PoPrint_fail001(self):
        msg = self.obj.test_PoPrint('822')
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API005_test_PoPrint_fail001_fail')

    # 采购订单列表打印-id为空
    def test_PoPrint_fail002(self):
        msg = self.obj.test_PoPrint('')
        msg1 = msg.get('code')
        self.assertEqual(500, msg1, 'API006_test_PoPrint_fail002_fail')

    # 采购订单明细列表无条件查询成功
    def test_PoItemList_success001(self):
        msg = self.obj.test_PoItemList()
        msg2 = len(msg['data']['data'])
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API007_test_PoItemList_success001_fail')
        self.assertNotEqual(0, msg2, 'API007_test_PoItemList_success001_fail')
        time.sleep(1)

    # 采购订单明細列表有条件查询成功
    def test_PoItemList_success002(self):
        msg = self.obj.test_PoItemList(purchaseOrderCode='', orderItemStat='', plantCode='',
                                       supplierCode='', materielCode='', materielDesc='',
                                       purchaseOrderType='Z12', completelyDelivered='',
                                       creationDateBegin='2021-02-23',
                                       creationDateEnd='2021-02-23', warehouseCode='', purchaserName='贺')
        msg2 = len(msg['data']['data'])
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API008_test_PoItemList_success002_fail')
        self.assertNotEqual(0, msg2, 'API008_test_PoItemList_success002_fail')
        time.sleep(1)

    # 采购订单明細列表查询暂无数据
    def test_PoItemList_success003(self):
        msg = self.obj.test_PoItemList(purchaseOrderCode='qq0000', orderItemStat='', plantCode='',
                                       supplierCode='', materielCode='', materielDesc='',
                                       purchaseOrderType='Z02', completelyDelivered='0',
                                       creationDateBegin='2021-02-23',
                                       creationDateEnd='2021-02-23', warehouseCode='', purchaserName='贺')
        msg2 = len(msg['data']['data'])
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API009_test_PoItemList_success003_fail')
        self.assertEqual(0, msg2, 'API009_test_PoItemList_success003_fail')
        time.sleep(1)

    # 采购订单明细-备注修改成功
    def test_PoItemRemark_success(self):
        msg = self.obj.test_PoItemRemark(purchaseOrderCode='4200000016', purchaseOrderItem='20', remark='zxm11')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API010_test_PoItemRemark_success_fail')

    # 采购订单明细-备注修改，不传订单号或订单行号
    def test_PoItemRemark_fail(self):
        msg = self.obj.test_PoItemRemark(purchaseOrderCode='', purchaseOrderItem='', remark='zxm11')
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API011_test_PoItemRemark_fail_fail')

    # 采购订单明细-确认成功
    def test_PoItemConfirm_success001(self):
        list = [{'purchaseOrderItem': '20', 'orderItemStat': '1',
                 'purchaseOrderCode': '4200000016', 'orderQuantity': '0',
                 'preDeliveryQuantity': '0', 'receiveQuantity': '0'}]
        msg = self.obj.test_PoItemConfirm(list)
        # print(msg)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API012_test_PoItemConfirm_success001_fail')
        time.sleep(1)

    # 采购订单明细-确认成功(订单行状态传入空值)，后端不使用前端所传的参数
    def test_PoItemConfirm_fail001(self):
        list = [{'purchaseOrderItem': '20', 'orderItemStat': '',
                 'purchaseOrderCode': '4200000016', 'orderQuantity': '0',
                 'preDeliveryQuantity': '0', 'receiveQuantity': '0'}]
        msg = self.obj.test_PoItemConfirm(list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API013_test_PoItemConfirm_fail001_fail')
        time.sleep(1)

    # 采购订单明细-确认失败(传入空值)
    def test_PoItemConfirm_fail002(self):
        list = [{'purchaseOrderItem': '20', 'orderItemStat': '1',
                 'purchaseOrderCode': '4200000016', 'orderQuantity': '',
                 'preDeliveryQuantity': '', 'receiveQuantity': '0'}]
        msg = self.obj.test_PoItemConfirm(list)
        msg1 = msg.get('code')
        self.assertEqual(500, msg1, 'API014_test_PoItemConfirm_fail002_fail')
        time.sleep(1)

    # 采购订单明细-确认成功（订单行状态填入任意字符），后端不使用前端所传的参数
    def test_PoItemConfirm_success002(self):
        list = [{'purchaseOrderItem': '20', 'orderItemStat': 'ww',
                 'purchaseOrderCode': '4200000016', 'orderQuantity': '0',
                 'preDeliveryQuantity': '0', 'receiveQuantity': '0'}]
        msg = self.obj.test_PoItemConfirm(list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API015_test_PoItemConfirm_success002_fail')

    # 采购订单明细-取消确认成功
    def test_PoItemUnConfirm_success001(self):
        list = [{'purchaseOrderItem': '20', 'orderItemStat': '0',
                 'purchaseOrderCode': '4200000016', 'orderQuantity': '0',
                 'preDeliveryQuantity': '0', 'receiveQuantity': '0'}]
        msg = self.obj.test_PoItemUnConfirm(list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API016_test_PoItemUnConfirm_success001_fail')
        time.sleep(1)

    # 采购订单明细-取消确认成功(订单行状态填入任意字符，后端不使用前端所传的参数)
    def test_PoItemUnConfirm_success002(self):
        list = [{'purchaseOrderItem': '20', 'orderItemStat': 'ww',
                 'purchaseOrderCode': '4200000016', 'orderQuantity': '0',
                 'preDeliveryQuantity': '0', 'receiveQuantity': '0'}]
        msg = self.obj.test_PoItemUnConfirm(list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API017_test_PoItemUnConfirm_success002_fail')
        time.sleep(1)

    # 采购订单明细-取消确认失败(订单数量为空)
    def test_PoItemUnConfirm_fail003(self):
        list = [{'purchaseOrderItem': '20', 'orderItemStat': '1',
                 'purchaseOrderCode': '4200000016', 'orderQuantity': '',
                 'preDeliveryQuantity': '0', 'receiveQuantity': '0'}]
        msg = self.obj.test_PoItemUnConfirm(list)
        msg1 = msg.get('code')
        self.assertEqual(500, msg1, 'API018_test_PoItemUnConfirm_fail003_fail')
        time.sleep(1)

    # 采购订单明细导出成功
    def test_PoItemExport_success(self):
        msg = self.obj.test_PoItemExport()
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API019_test_PoItemExport_success_fail')

    # 采购订单明细-批量确认成功
    def test_PoItemConfirmX_success002(self):
        list = [{'purchaseOrderItem': '280', 'orderItemStat': '1', 'purchaseOrderCode': '4300000044',
                 'orderQuantity': '700', 'preDeliveryQuantity': '0', 'receiveQuantity': '0'},
                {'purchaseOrderItem': '270', 'orderItemStat': '1', 'purchaseOrderCode': '4300000044',
                 'orderQuantity': '300', 'preDeliveryQuantity': '0', 'receiveQuantity': '0'}, ]
        msg = self.obj.test_PoItemConfirm(list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API020_test_PoItemConfirm_success002_fail')
        time.sleep(1)

    # 采购订单明细-批量取消成功
    def test_PoItemUnConfirmX_success002(self):
        list = [{'purchaseOrderItem': '280', 'orderItemStat': '0', 'purchaseOrderCode': '4300000044',
                 'orderQuantity': '700', 'preDeliveryQuantity': '0', 'receiveQuantity': '0'},
                {'purchaseOrderItem': '270', 'orderItemStat': '0', 'purchaseOrderCode': '4300000044',
                 'orderQuantity': '300', 'preDeliveryQuantity': '0', 'receiveQuantity': '0'}, ]
        msg = self.obj.test_PoItemUnConfirm(list)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API021_test_PoItemUnConfirm_success002_fail')
        time.sleep(1)

    # 采购订单明细-预发货成功
    def test_PoItemPre_delivery_success(self):
        list = [{'purchaseOrderCode': '4300000044', 'purchaseOrderItem': '20', 'materielCode': '251-00741-001',
                 'warehouseCode': '6006', 'plantCode': '1070',
                 'supplierCode': '3041', 'deliveryQuantity': '1', 'remark': 'zxm11'},
                {'purchaseOrderCode': '4300000044', 'purchaseOrderItem': '10', 'materielCode': '251-00741-001',
                 'warehouseCode': '6006', 'plantCode': '1070',
                 'supplierCode': '3041', 'deliveryQuantity': '1', 'remark': 'zxm11'}]
        msg = self.obj.test_PoItemPre_delivery(list)
        # print(msg)
        msg1 = msg.get('code')
        # globals()["pc1"] = msg('data')
        self.assertEqual(200, msg1, 'API022_test_PoItemPre_delivery_success_fail')

    # 采购订单明细-预发货失败,预发货数为空
    def test_PoItemPre_delivery_fail001(self):
        list = [{'purchaseOrderCode': '4300000044', 'purchaseOrderItem': '20', 'materielCode': '251-00741-001',
                 'warehouseCode': '6006', 'plantCode': '1070',
                 'supplierCode': '3041', 'deliveryQuantity': '', 'remark': 'zxm11'}]
        msg = self.obj.test_PoItemPre_delivery(list)
        msg1 = msg.get('code')
        self.assertEqual(500, msg1, 'API023_test_PoItemPre_delivery_fail001_fail')

    # 采购订单明细-预发货失败,预发货数为0或者负数或者為小数（单位为EA的物料）
    def test_PoItemPre_delivery_fail002(self):
        list = [{'purchaseOrderCode': '4300000044', 'purchaseOrderItem': '20', 'materielCode': '251-00741-001',
                 'warehouseCode': '6006', 'plantCode': '1070',
                 'supplierCode': '3041', 'deliveryQuantity': '0', 'remark': 'zxm11'}]
        msg = self.obj.test_PoItemPre_delivery(list)
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API024_test_PoItemPre_delivery_fail002_fail')

    # 采购订单明细-导入预发货open(filepath, 'rb')
    # filepath = r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\srm2\files\导入预发货模板.xls'
    def test_PoItemPre_deliveryFile_success(self):
        filepath = r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\srm2\files\导入预发货模板01.xls'
        file = open(filepath, 'rb')
        msg = self.obj.test_PoItemPre_deliveryFile(file)
        file.close()
        # print(msg)
        msg1 = msg.get('code')
        global pc
        pc = msg['data']['importResult'][0]['resultInfo']
        # print(self.pc)
        self.assertEqual(200, msg1, 'API025_test_PoItemPre_deliveryFile_success_fail')
        return pc

    # 采购订单明细-导入预发货失败（文件格式不正确）
    def test_PoItemPre_deliveryFile_fail001(self):
        filepath = r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\srm2\files\test.txt'
        msg = self.obj.test_PoItemPre_deliveryFile(filepath)
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'API026_test_PoItemPre_deliveryFile_fail001_fail')
        self.assertIn('Excel格式', msg2, '')

    # 采购订单明细-导入预发货失败-未匹配到订单
    def test_PoItemPre_deliveryFile_fail002(self):
        filepath = r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\srm2\files\导入预发货模板02.xls'
        file = open(filepath, 'rb')
        msg = self.obj.test_PoItemPre_deliveryFile(file)
        file.close()
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'API029_test_PoItemPre_deliveryFile_fail002_fail')
        self.assertIn('未匹配到可发货的订单', msg2, 'API027_test_PoItemPre_deliveryFile_fail002_fail')

    # 采购订单明细-下载导入预发货模板PRE_DELIVERY_TEMPLATE
    def test_BizCodeDict_success(self):
        msg = self.obj.test_BizCodeDict(bizType='PRE_DELIVERY_TEMPLATE')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API028_test_BizCodeDict_success_fail')

    # 采购订单明细-下载导入预发货模板bizType为空
    def test_BizCodeDict_fail(self):
        msg = self.obj.test_BizCodeDict(bizType='')
        msg1 = msg.get('code')
        self.assertEqual(500, msg1, 'API029_test_BizCodeDict_fail_fail')

    # 送货单列表查询成功
    def test_PcList_success001(self):
        msg = self.obj.test_PcList()
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API030_test_PcList_success001_fail')
        self.assertNotEqual(0, msg2, 'API030_test_PcList_success001_fail')

    # 送货单列表带条件查询成功
    def test_PcList_success002(self):
        msg = self.obj.test_PcList(deliveryNoteCode='210304', deliveryStat='', receiveStat='', supplierCode='',
                                   materielCode='', materielDesc='', plantCode='')
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API031_test_PcList_success002_fail')
        self.assertNotEqual(0, msg2, 'API031_test_PcList_success002_fail')

    # 送货单列表查询暂无数据
    def test_PcList_success003(self):
        msg = self.obj.test_PcList(deliveryNoteCode='www')
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'API032_test_PcList_success003_fail')
        self.assertEqual(0, msg2, 'API032_test_PcList_success003_fail')

    # 送货单列表-修改备注成功expressNo
    def test_PcRemark_success(self):
        d = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        msg = self.obj.test_PcRemark(id=661, deliveryNoteCode='PC6006210305000008', plantCode='1073',
                                     supplierCode='3159', warehouseCode='A001', creationDate='2021-03-05',
                                     expectDeliveryDate=None, actualDeliveryDate=None, printTime=None,
                                     expressNo='zxm11接口勿动' + d)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API033_test_PcRemark_success_fail')

    # 送货单预计送达日期成功
    def test_PcDate_success(self):
        d = time.strftime("%Y-%m-%d", time.localtime())
        msg = self.obj.test_PcDate(id=661, expectDeliveryDate=d)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API034_test_PcDate_success_fail')

    # 送货单-变更发货数量成功
    def test_PcDQ_update_success(self):
        msg = self.obj.test_PcDQ_update(id=4514, deliveryNoteCode='PC6006210305000008', deliveryNoteItem='1',
                                        purchaseOrderCode='4300000044', purchaseOrderItem='10',
                                        deliveryQuantity='4', quantityUnit='EA', materielCode='251-00741-001')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API035_test_PcDQ_update_success_fail')

    # 送货单-变更发货数量失败（负数、0、单位为EA不能是小数）
    def test_PcDQ_update_fail(self):
        msg = self.obj.test_PcDQ_update(id=4477, deliveryNoteCode='PCA001210305000003', deliveryNoteItem='1',
                                        purchaseOrderCode='4100000754', purchaseOrderItem='10',
                                        deliveryQuantity='-12.4', quantityUnit='EA', materielCode='310A-00008')
        msg1 = msg.get('code')
        self.assertEqual(400, msg1, 'API036_test_PcDQ_update_fail_fail')

    # 送货单打印成功
    def test_PcPrint_success(self):
        d = time.strftime("%Y-%m-%d", time.localtime())
        dtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        msg = self.obj.test_PcPrint(actualDeliveryDate=d, deliveryNoteCode='PC6006210305000008', printTime=dtime)
        msg1 = msg.get('code')
        msg2 = len(msg.get('data'))
        self.assertEqual(200, msg1, 'API037_test_PcPrint_success_fail')
        self.assertEqual(0, msg2, 'API037_test_PcPrint_success_fail')

    # 送货单打印失败
    def test_PcPrint_fail(self):
        msg = self.obj.test_PcPrint(actualDeliveryDate='',deliveryNoteCode='',printTime='')
        msg1 = msg.get('code')
        msg2 = len(msg.get('data'))
        self.assertEqual(500, msg1, 'API038_test_PcPrint_fail_fail')

    # 送货单-发货成功,前置条件：送货单已打印，预计送达日期与备注已维护
    def test_PcDeliver_success(self):
        msg = self.obj.test_PcDeliver(deliveryNoteCode='PC6006210305000008')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API039_test_PcDeliver_success_fail' + str(msg))

    # 送货单-发货失败，前置条件：已发货的送货单
    def test_PcDeliver_fail001(self):
        msg = self.obj.test_PcDeliver(deliveryNoteCode='PC2006210304000032')
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'API040_test_PcDeliver_fail001_fail')
        self.assertIn('不是待发货状态', msg2, 'API040_test_PcDeliver_fail001_fail')

    # 送货单-发货失败，前置条件：送货单编号为空
    def test_PcDeliver_fail002(self):
        msg = self.obj.test_PcDeliver(deliveryNoteCode='')
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'API041_test_PcDeliver_fail002_fail')
        self.assertIn('信息不存在', msg2, 'API041_test_PcDeliver_fail002_fail')

    # 送货单-取消发货成功，前置条件：待发货的送货单
    def test_PcUnDeliver_success001(self):
        # pc = TestPMCase.test_PoItemPre_deliveryFile_success()
        msg = self.obj.test_PcUnDeliver(deliveryNoteCode='PC2001201215000008', deleteReason='取消发货接口验证')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API042_test_PcUnDeliver_success001_fail')

    # 送货单-取消发货成功，前置条件：已发货，未收货的送货单
    def test_PcUnDeliver_success002(self):
        msg = self.obj.test_PcUnDeliver(deliveryNoteCode='PC3002201203000009', deleteReason='取消发货接口验证')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'API043_test_PcUnDeliver_success002_fail')

    # 送货单-取消发货失败，前置条件：送货单编号为空
    def test_PcUnDeliver_fail001(self):
        msg = self.obj.test_PcUnDeliver(deliveryNoteCode='', deleteReason='取消发货接口验证')
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'API044_test_PcUnDeliver_fail001_fail')
        self.assertIn('信息不存在', msg2, 'API044_test_PcUnDeliver_fail001_fail')

    # 送货单-取消发货失败，前置条件：WMS已操作过的送货单,送货单状态为收货完成
    def test_PcUnDeliver_fail002(self):
        msg = self.obj.test_PcUnDeliver(deliveryNoteCode='PC2002210113000002', deleteReason='取消发货接口验证')
        msg1 = msg.get('code')
        msg2 = msg.get('msg')
        self.assertEqual(400, msg1, 'API045_test_PcUnDeliver_fail_fail')
        self.assertIn('库房已操作，不可撤单', msg2, 'API045_test_PcUnDeliver_fail002_fail')

    # 送货单-取消发货失败（目前是能取消成功的），前置条件：已发货，WMS未进行过操作的送货单，SAP做的收货，送货单状态为部分收货,PC2002210219000010
    def test_PcUnDeliver_fail003(self):
        msg = self.obj.test_PcUnDeliver(deliveryNoteCode='PC2002210219000010', deleteReason='取消发货接口验证')
        msg1 = msg.get('code')
        self.assertNotEqual(200, msg1, 'API046_test_PcUnDeliver_fail003_fail')

    # 送货单-物料标签打印校验
    def test_MaterielLablePrint_success(self):
        msg = self.obj.test_MaterielLablePrint(purchaseOrderCode='4100000754', materielCode='10',
                                               materielDesc='310A-00008', supplierCode='3159',
                                               productionDate='2021-03-01', dueDate='2021-03-05', dateCode='0000',
                                               lotNo='0', latestPdi='', humiditySensitiveGrade='L1', boxNum='1',
                                               quantity='1', baseUnit='EA')
        # print(msg)
        self.assertIn('200', msg, 'API047_test_MaterielLablePrint_success_fail')

    # 送货单-物料标签打印成功
    def test_PcMaterielLablePrint_success(self):
        msg = self.obj.test_PcMaterielLablePrint(purchaseOrderCode='4100000754', purchaseOrderItem='10')
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'api048_test_PcMaterielLablePrint_success_fail')

    # 送货单-物料标签打印失败
    def test_PcMaterielLablePrint_fail(self):
        msg = self.obj.test_PcMaterielLablePrint(purchaseOrderCode='', purchaseOrderItem='10')
        msg1 = msg.get('code')
        self.assertNotEqual(200, msg1, 'api049_test_PcMaterielLablePrint_success_fail')

    # 送货单明细列表-查询
    def test_PcItemList_success001(self):
        msg = self.obj.test_PcItemList()
        msg1 = msg.get('code')
        msg2 = len(msg.get('data'))
        self.assertEqual(200, msg1, 'api050_test_PcItemList_success001_fail')
        self.assertNotEqual(0, msg2, 'api050_test_PcItemList_success001_fail')

    # 送货单明细列表-带条件查询
    def test_PcItemList_success002(self):
        msg = self.obj.test_PcItemList(deliveryNoteCode='6006', purchaseOrderCode=None, supplierCode=None,
                                       plantCode=None, materielCode=None, materielDesc=None, warehouseCode=None,
                                       receiveStat=None)
        msg1 = msg.get('code')
        msg2 = len(msg.get('data'))
        self.assertEqual(200, msg1, 'api051_test_PcItemList_success002_fail')
        self.assertNotEqual(0, msg2, 'api051_test_PcItemList_success002_fail')

    # 送货单明细列表-查询暂无数据
    def test_PcItemList_success003(self):
        msg = self.obj.test_PcItemList(deliveryNoteCode='qqq', purchaseOrderCode=None, supplierCode=None,
                                       plantCode=None, materielCode=None, materielDesc=None, warehouseCode=None,
                                       receiveStat=None)
        msg1 = msg.get('code')
        msg2 = len(msg['data']['data'])
        self.assertEqual(200, msg1, 'api052_test_PcItemList_success003_fail')
        self.assertEqual(0, msg2, 'api052_test_PcItemList_success003_fail')

    # 送货单明细导出成功
    def test_PcItemExport_success(self):
        msg = self.obj.test_PcItemExport(deliveryNoteCode='6006', purchaseOrderCode=None, supplierCode=None,
                                         materielCode=None, materielDesc=None, plantCode=None, warehouseCode=None)
        msg1 = msg.get('code')
        self.assertEqual(200, msg1, 'api053_test_PcItemExport_success_fail')

    @classmethod
    def tearDownClass(self):
        print("----test_pm end----")


if __name__ == '__main__':
    unittest.main()

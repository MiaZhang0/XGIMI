import requests
from srm2.common.gettoken import gettoken_OA
import time


# 采购管理
class TestPm():
    def __init__(self):
        self.host = 'http://srm-in.t.xgimi.com/apis'
        self.token = gettoken_OA('xiaomei.zhang', 'Xx123456')

    # 采购订单列表查询
    def test_PoList(self, purchaseOrderCode=None, purchaseOrderStat=None, supplierCode=None, startDate=None,
                    endDate=None, companyCode=None, purchaseOrderType=None):
        url = self.host + '/purchaseOrder/list'
        datas = {'purchaseOrderCode': purchaseOrderCode, 'purchaseOrderStat': purchaseOrderStat,
                 'supplierCode': supplierCode,
                 'startDate': startDate, 'endDate': endDate, 'companyCode': companyCode,
                 'purchaseOrderType': purchaseOrderType}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 采购订单打印
    def test_PoPrint(self, id):
        url = self.host + '/purchaseOrder/print'
        data = {'id': id}
        header = {'token': self.token}
        r = requests.get(url, params=data, headers=header)
        message = r.json()
        return message

    # 采购订单明细列表查询
    def test_PoItemList(self, purchaseOrderCode=None, orderItemStat=None, plantCode=None, supplierCode=None,
                        materielCode=None, materielDesc=None, startDate=None, endDate=None, purchaseOrderType=None,
                        completelyDelivered=None, creationDateBegin=None, creationDateEnd=None, warehouseCode=None,
                        purchaserName=None):
        url = self.host + '/purchaseOrderItem/list'
        datas = {'purchaseOrderCode': purchaseOrderCode, 'orderItemStat': orderItemStat, 'plantCode': plantCode,
                 'supplierCode': supplierCode, 'materielCode': materielCode, 'materielDesc': materielDesc,
                 'startDate': startDate, 'endDate': endDate, 'purchaseOrderType': purchaseOrderType,
                 'completelyDelivered': completelyDelivered, 'creationDateBegin': creationDateBegin,
                 'creationDateEnd': creationDateEnd, 'warehouseCode': warehouseCode, 'purchaserName': purchaserName}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 采购订单明细-备注
    def test_PoItemRemark(self, purchaseOrderCode, purchaseOrderItem, remark=None):
        url = self.host + '/purchaseOrderItem/update_remark'
        datas = {'purchaseOrderCode': purchaseOrderCode, 'purchaseOrderItem': purchaseOrderItem, 'remark': remark}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 采购订单明细-确认
    def test_PoItemConfirm(self, list):
        url = self.host + '/purchaseOrderItem/poItemConfirm'
        datas = {'purchaseOrderItemList': list}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 采购订单明细-取消确认
    def test_PoItemUnConfirm(self, list):
        url = self.host + '/purchaseOrderItem/poItemUnConfirm'
        datas = {'purchaseOrderItemList': list}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 采购订单明细-导出
    def test_PoItemExport(self):
        url = self.host + '/purchaseOrderItem/async_export'
        header = {'token': self.token}
        r = requests.get(url, headers=header)
        message = r.json()
        return message

    # 采购订单明细-预发货
    def test_PoItemPre_delivery(self, list):
        url = self.host + '/purchaseOrderItem/pre_delivery'
        datas = {'poItemList': list}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 采购订单明细-导入预发货open(filepath, 'rb')
    # filepath = r'C:\Users\xiaomei.zhang\PycharmProjects\pythonProject1\srm2\files\导入预发货模板.xls'
    def test_PoItemPre_deliveryFile(self, file):
        url = self.host + '/purchaseOrderItem/pre_delivery_file'
        header = {'token': self.token}
        data = {'file': file}
        r = requests.post(url, files=data, headers=header)
        message = r.json()
        return message

    # 采购订单明细-下载导入预发货模板PRE_DELIVERY_TEMPLATE
    def test_BizCodeDict(self, bizType):
        url = self.host + '/biz_code_dict/api_list'
        header = {'token': self.token}
        data = {'bizType': bizType}
        r = requests.get(url, params=data, headers=header)
        message = r.json()
        return message

    # 送货单列表查询
    def test_PcList(self, deliveryNoteCode=None, deliveryStat=None, receiveStat=None, supplierCode=None,
                    materielCode=None, materielDesc=None, plantCode=None):
        url = self.host + '/delivery_note/list'
        datas = {'deliveryNoteCode': deliveryNoteCode, 'deliveryStat': deliveryStat, 'receiveStat': receiveStat,
                 'supplierCode': supplierCode, 'materielCode': materielCode, 'materielDesc': materielDesc,
                 'plantCode': plantCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 送货单列表-修改备注expressNo
    def test_PcRemark(self, id, deliveryNoteCode, plantCode, supplierCode, warehouseCode, creationDate,
                      expectDeliveryDate=None, actualDeliveryDate=None, printTime=None, expressNo=None):
        url = self.host + '/delivery_note/update'
        datas = {'id': id, ' deliveryNoteCode': deliveryNoteCode, 'plantCode': plantCode, 'supplierCode': supplierCode,
                 'warehouseCode': warehouseCode, 'creationDate': creationDate, 'expectDeliveryDate': expectDeliveryDate,
                 'actualDeliveryDate': actualDeliveryDate, 'printTime': printTime, 'expressNo': expressNo}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 送货单预计送达日期
    def test_PcDate(self, id, expectDeliveryDate):
        url = self.host + '/delivery_note/update_expect_delivery_date'
        datas = {'id': id, 'expectDeliveryDate': expectDeliveryDate}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 送货单-变更发货数量
    def test_PcDQ_update(self, id, deliveryNoteCode, deliveryNoteItem, purchaseOrderCode, purchaseOrderItem,
                         deliveryQuantity, quantityUnit, materielCode):
        url = self.host + '/delivery_note_item/delivery_quantity_update'
        datas = {'id': id, 'deliveryNoteCode': deliveryNoteCode, 'deliveryNoteItem': deliveryNoteItem,
                 'purchaseOrderCode': purchaseOrderCode,
                 'purchaseOrderItem': purchaseOrderItem, 'deliveryQuantity': deliveryQuantity,
                 'quantityUnit': quantityUnit, 'materielCode': materielCode}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 送货单-发货
    def test_PcDeliver(self, deliveryNoteCode):
        url = self.host + '/delivery_note/deliver'
        datas = {'deliveryNoteCode': deliveryNoteCode}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 送货单-取消发货
    def test_PcUnDeliver(self, deliveryNoteCode, deleteReason):
        url = self.host + '/delivery_note/deliver_cancel'
        datas = {'deliveryNoteCode': deliveryNoteCode, 'deleteReason': deleteReason}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 送货单打印
    def test_PcPrint(self, actualDeliveryDate, deliveryNoteCode, printTime):
        url = self.host + '/delivery_note/update'
        data = {'actualDeliveryDate': actualDeliveryDate, 'deliveryNoteCode': deliveryNoteCode, 'printTime': printTime}
        header = {'token': self.token}
        r = requests.post(url, json=data, headers=header)
        message = r.json()
        return message

    # 送货单-物料标签打印校验
    def test_MaterielLablePrint(self, purchaseOrderCode, materielCode, materielDesc, supplierCode, productionDate,
                                dueDate, dateCode, lotNo, latestPdi, humiditySensitiveGrade, boxNum, quantity,
                                baseUnit):
        url = self.host + '/print/materiel_label'
        datas = {'purchaseOrderCode': purchaseOrderCode, 'materielCode': materielCode, 'materielDesc': materielDesc,
                 'supplierCode': supplierCode,
                 'productionDate': productionDate, 'dueDate': dueDate, 'dateCode': dateCode, 'lotNo': lotNo,
                 'latestPdi': latestPdi,
                 'humiditySensitiveGrade': humiditySensitiveGrade, 'boxNum': boxNum, 'quantity': quantity,
                 'baseUnit': baseUnit}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.text
        return message

    # 送货单-物料标签打印
    def test_PcMaterielLablePrint(self, purchaseOrderCode, purchaseOrderItem):
        url = self.host + '/purchaseOrderItem/materiel_label'
        datas = {'purchaseOrderCode': purchaseOrderCode, 'purchaseOrderItem': purchaseOrderItem}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 送货单明细列表-查询
    def test_PcItemList(self, deliveryNoteCode=None, purchaseOrderCode=None, supplierCode=None, plantCode=None,
                        materielCode=None, materielDesc=None, warehouseCode=None, receiveStat=None):
        url = self.host + '/delivery_note_item/list'
        datas = {'deliveryNoteCode': deliveryNoteCode, 'purchaseOrderCode': purchaseOrderCode,
                 'supplierCode': supplierCode,
                 'plantCode': plantCode, 'materielCode': materielCode, 'materielDesc': materielDesc,
                 'warehouseCode': warehouseCode,
                 'receiveStat': receiveStat}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 送货单明细导出
    def test_PcItemExport(self, deliveryNoteCode=None, purchaseOrderCode=None, supplierCode=None, materielCode=None,
                          materielDesc=None, plantCode=None, warehouseCode=None):
        url = self.host + '/delivery_note_item/async_export'
        datas = {'deliveryNoteCode': deliveryNoteCode, 'purchaseOrderCode': purchaseOrderCode,
                 'supplierCode': supplierCode,
                 'materielCode': materielCode, 'materielDesc': materielDesc, 'plantCode': plantCode,
                 'warehouseCode': warehouseCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message


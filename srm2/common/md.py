import requests
from srm2.common.gettoken import gettoken_OA


# 物料接收
class TestMd():
    def __init__(self):
        self.host = 'http://srm-in.t.xgimi.com/apis'
        self.token = gettoken_OA('xiaomei.zhang', 'Xx123456')

    # 物料接收确认列表
    def test_MdList(self, materielCode=None, purchaseOrderCode=None, supplierCode=None, materielDocumentCode=None,
                    materielReceiveStat=None):
        url = self.host + '/materiel_document/list'
        datas = {'materielCode': materielCode, 'purchaseOrderCode': purchaseOrderCode, 'supplierCode': supplierCode,
                 'materielDocumentCode': materielDocumentCode, 'materielReceiveStat': materielReceiveStat}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 物料接收-实收数量、备注
    def test_MdReceivedQuantity(self, list):
        url = self.host + '/materiel_document/confirm_quantity'
        datas = {'materielDocumentList':list}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 物料接收确认-导出
    def test_MdExport(self):
        url = self.host + '/materiel_document/async_export'
        header = {'token': self.token}
        r = requests.get(url, headers=header)
        message = r.json()
        return message

    # 物料接收明细查询
    def test_MdItemList(self, purchaseOrderCode=None, supplierCode=None, materielDesc=None, materielCode=None,
                        stockOutStat=None):
        url = self.host + '/purchase_order_sub_component/list_poitem_subcomponent'
        datas = {'purchaseOrderCode': purchaseOrderCode, 'supplierCode': supplierCode, 'materielDesc': materielDesc,
                 'materielCode': materielCode, 'stockOutStat': stockOutStat}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 物料接收明细导出
    def test_MdItemExport(self):
        url = self.host + '/purchase_order_sub_component/async_export'
        header = {'token': self.token}
        r = requests.get(url, headers=header)
        message = r.json()
        return message

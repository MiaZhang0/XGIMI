import requests
from srm2.common.gettoken import gettoken_OA

# 委外维修用料回复
class TestWeiWai():
    def __init__(self):
        self.host = 'http://srm-in.t.xgimi.com/apis'
        self.token = gettoken_OA('xiaomei.zhang', 'Xx123456')

    # 委外维修列表
    def test_MaterialReplyList(self,purchaseOrderCode=None,supplierCode=None,materielCode=None,materielDesc=None,
                               materialReplyMark=None,approvalMark=None):
        url = self.host + '/purchaseOrderItem/list_material_reply'
        datas = {'purchaseOrderCode':purchaseOrderCode,'supplierCode':supplierCode,'materielCode':materielCode,
                 'materielDesc':materielDesc,'materialReplyMark':materialReplyMark,'approvalMark':approvalMark}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 用料回复模板导出
    def test_MaterialReplyExport(self,modelList,purchaseOrderCode,materialCode):
        url = self.host + '/materiel_reply/model_export'
        datas = {'modelList':modelList,'purchaseOrderCode':purchaseOrderCode,'materialCode':materialCode}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 用料回复导入
    def test_MaterialReplyImport(self,file):
        url = self.host + '/materiel_reply/import'
        datas = {'file':file}
        header = {'token': self.token}
        r = requests.post(url, file=datas, headers=header)
        message = r.json()
        return message

    # 查看用料明细
    def test_MaterialReplyDetail(self,purchaseOrderCode=None,materialCode=None):
        url = self.host + '/materiel_reply/get_materiel_reply'
        datas = {'purchaseOrderCode':purchaseOrderCode,'materialCode':materialCode}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 取消用料回复
    def test_MaterialReplyCancel(self,poItemList):
        url = self.host + '/purchaseOrderItem/cancel_material_reply_mark'
        datas = {'poItemList':poItemList}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 提交BPM审批
    def test_MaterialReplySubmit(self,purchaseOrderCode,materielCode):
        url = self.host + '/materiel_reply/priceExamine4Bpm'
        datas = {'purchaseOrderCode':purchaseOrderCode,'materielCode':materielCode}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 用料回复列表
    def test_MaterialReplyItemList(self,purchaseOrderCode,materialCode):
        url = self.host + '/materiel_reply_item/list'
        datas = {'purchaseOrderCode':purchaseOrderCode,'materialCode':materialCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 用料回复导出
    def test_MaterialReplyItemExport(self,purchaseOrderCode,materialCode):
        url = self.host + '/materiel_reply_item/async_export'
        datas = {'purchaseOrderCode':purchaseOrderCode,'materialCode':materialCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 委外订单明细列表
    def test_WeiWaiOrderItemList(self,purchaseOrderCode=None,supplierCode=None,materielCode=None,inboundStat=None,
                                 purchaserName=None,purchaseOrderType=None,startDate=None,endDate=None,
                                 componentMaterielCode=None,backStat=None):
        url = self.host + '/purchase_order_sub_component/list_outsource_order'
        datas = {'purchaseOrderCode':purchaseOrderCode,'supplierCode':supplierCode,'materielCode':materielCode,
                 'inboundStat':inboundStat,'purchaserName':purchaserName,'purchaseOrderType':purchaseOrderType,
                 'startDate':startDate,'endDate':endDate,'componentMaterielCode':componentMaterielCode,'backStat':backStat}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 委外订单明细导出
    def test_WeiWaiOrderItemExport(self,purchaseOrderCode=None,supplierCode=None,materielCode=None,inboundStat=None,
                                   purchaserName=None,purchaseOrderType=None,startDate=None,endDate=None,
                                   componentMaterielCode=None):
        url = self.host + '/purchase_order_sub_component/export_outsource_order'
        datas = {'purchaseOrderCode':purchaseOrderCode,'supplierCode':supplierCode,'materielCode':materielCode,
                 'inboundStat':inboundStat,'purchaserName':purchaserName,'purchaseOrderType':purchaseOrderType,
                 'startDate':startDate,'endDate':endDate,'componentMaterielCode':componentMaterielCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message
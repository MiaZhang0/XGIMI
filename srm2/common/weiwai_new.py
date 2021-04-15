import requests
from srm2.common.gettoken import gettoken_OA


# 委外维修用料回复
class TestWeiWai():
    def __init__(self):
        self.host = 'http://srm-in.t.xgimi.com/apis'
        self.token = gettoken_OA('xiaomei.zhang', 'Xx11111!')

    # 委外维修订单列表
    def test_WeiWaiPOList(self, purchaseOrderCode=None, supplierCode=None, materielCode=None, maintainMaterielCode=None,
                          outsourceReplyMark=None):
        url = self.host + '/outsource_reply/outsource_maintain_po_item'
        datas = {'purchaseOrderCode': purchaseOrderCode, 'supplierCode': supplierCode, 'materielCode': materielCode,
                 'maintainMaterielCode': maintainMaterielCode, 'outsourceReplyMark': outsourceReplyMark}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 用料回复列表
    def test_MaterielReplyList(self, outsourceReplyCode=None, supplierCode=None, materielCode=None, approvalMark=None):
        url = self.host + '/outsource_reply/list'
        datas = {'outsourceReplyCode': outsourceReplyCode, 'supplierCode': supplierCode, 'materielCode': materielCode,
                 'approvalMark': approvalMark}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 用料回复列表导出
    def test_MaterielReplyListExport(self, outsourceReplyCode=None, supplierCode=None, materielCode=None,
                                     approvalMark=None):
        url = self.host + '/outsource_reply/export_outsource_reply'
        datas = {'outsourceReplyCode': outsourceReplyCode, 'supplierCode': supplierCode, 'materielCode': materielCode,
                 'approvalMark': approvalMark}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 委外维修订单列表导出
    def test_WeiWaiListExport(self, purchaseOrderCode=None, supplierCode=None, materielCode=None,
                              maintainMaterielCode=None, outsourceReplyMark=None):
        url = self.host + '/outsource_reply/export_po_item'
        datas = {'purchaseOrderCode': purchaseOrderCode, 'supplierCode': supplierCode, 'materielCode': materielCode,
                 'maintainMaterielCode': maintainMaterielCode, 'outsourceReplyMark': outsourceReplyMark}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 用料回复模板导出
    def test_MaterielReplyTemplateExport(self, replyItemList=None):
        url = self.host + '/outsource_reply/export_reply_template'
        datas = {'replyItemList': replyItemList}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 查看用料明细
    def test_MaterielReplyItem(self, outsourceReplyCode):
        url = self.host + '/outsource_reply/list_outsource_materiel_reply'
        datas = {'outsourceReplyCode': outsourceReplyCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 用料回复导入
    def test_MaterielReplyImport(self, file):
        url = self.host + '/outsource_reply/maintain_materiel_reply'
        data = {'file': file}
        header = {'token': self.token}
        r = requests.post(url, files=data, headers=header)
        message = r.json()
        return message

    # 提交BPM审核
    def test_BPMCommit(self, outsourceReplyCode):
        url = self.host + '/outsource_reply/priceExamine4Bpm'
        datas = {'outsourceReplyCode': outsourceReplyCode}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 委外维修订单匹配
    def test_WeiWaiPOMatch(self, supplierCode, maintainQuantity, materielCode=None, maintainMaterielCode=None):
        url = self.host + '/outsource_reply/matching_po_item'
        datas = {'supplierCode': supplierCode, 'maintainQuantity': maintainQuantity, 'materielCode': materielCode,
                 'maintainMaterielCode': maintainMaterielCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 取消用料回复
    def test_MaterielReplyCancel(self, outsourceReplyPlanList=None):
        url = self.host + '/outsource_reply/cancel_outsource_materiel_reply'
        datas = {'outsourceReplyPlanList': outsourceReplyPlanList}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 用料回复详情导出
    def test_MaterielReplyDetailExport(self, outsourceReplyCode=None, supplierCode=None, materielCode=None,
                                       approvalMark=None):
        url = self.host + '/outsource_reply/export_outsource_reply_detail'
        datas = {'outsourceReplyCode': outsourceReplyCode, 'supplierCode': supplierCode, 'materielCode': materielCode,
                 'approvalMark': approvalMark}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message


# T = TestWeiWai()
# list = [{'id':38}]
# RES2 = T.test_MaterielReplyCancel(outsourceReplyPlanList=list)
# print(RES2)

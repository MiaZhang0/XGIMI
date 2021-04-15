import requests


# 委外维修用料回复
class TestMaterialReplyModule():
    def __init__(self):
        self.host = 'http://srm.t.xgimi.com/apis'

    # 查看用料详情
    def testGetMaterialReplay(self, purchaseOrderCode=None, materialCode=None):
        url = self.host + '/materiel_reply/get_materiel_reply'
        datas = {'purchaseOrderCode': purchaseOrderCode, 'materialCode': materialCode}
        header = {'Content-Type': 'application/json'}
        r = requests.post(url, headers=header, data=datas)
        message = r.json()
        return message

    # 用料回复导入
    def testMaterialReplay(self, file):
        url = self.host + '/materiel_reply/reply'
        datas = {'file': file}
        header = {'Content-Type': 'multipart/form-data'}
        r = requests.post(url, headers=header, data=datas)
        message = r.json()
        return message

    # 委外维修列表
    def testMaterialReplayList(self, purchaseOrderCode=None, supplierCode=None, materielCode=None, materielDesc=None,
                               materialReplyMark=None, approvalMark=None):
        url = self.host + '/purchaseOrderItem/list_material_reply'
        datas = {'purchaseOrderCode': purchaseOrderCode, 'supplierCode': supplierCode, 'materielCode': materielCode,
                 'materielDesc': materielDesc, 'materialReplyMark': materialReplyMark, 'approvalMark': approvalMark}
        r = requests.get(url, params=datas)
        message = r.json()
        return message
    # 用料回复模板导出,modelList是个对象
    def testMaterialReplyExport(self,purchaseOrderCode,materialCode,modelList=None):
        url = self.host + '/materiel_reply/model_export'
        header = {'Content-Type':'application/json'}
        datas = {'modelList':modelList,'purchaseOrderCode':purchaseOrderCode,'materialCode':materialCode}
        r = requests.post(url,headers=header,data=datas)
        message = r.json()
        return message
    # 用料回复列表
    def testMaterialReplyList(self,purchaseOrderCode=None,materialCode=None):
        url = self.host + '/materiel_reply_item/list'
        datas = {'purchaseOrderCode':purchaseOrderCode,'materialCode':materialCode}

t = TestMaterialReplyModule()
t2 = t.testMaterialReplay('')

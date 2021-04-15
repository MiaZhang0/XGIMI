import requests
from srm2.common.gettoken import gettoken_OA


# 加工费结算
class TestPf():
    def __init__(self):
        self.host = 'http://srm-in.t.xgimi.com/apis'
        self.token = gettoken_OA('xiaomei.zhang', 'Xx123456')

    # 生产订单列表
    def test_ManOrderList(self, postingMonth, manufactureOrderCode=None, manufactureOrderStat=None,
                          manufactureOrderType=None,
                          plantCode=None, technicallyCompleted=None):
        url = self.host + '/processing_fee_settlement/list'
        datas = {'postingMonth': postingMonth, 'manufactureOrderCode': manufactureOrderCode,
                 'manufactureOrderStat': manufactureOrderStat, 'manufactureOrderType': manufactureOrderType,
                 'plantCode': plantCode, 'technicallyCompleted': technicallyCompleted}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 创建采购订单
    def test_createPO(self, manufactureOrderCode, postingMonth, materielCode, postingDate):
        url = self.host + '/processing_fee_settlement/create_purchase_order'
        datas = {'manufactureOrderCode': manufactureOrderCode, 'postingMonth': postingMonth,
                 'materielCode': materielCode, 'postingDate': postingDate}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 过账
    def test_POposting(self, manufactureOrderCode, postingMonth, materielCode, postingDate):
        url = self.host + '/processing_fee_settlement/posting_order'
        datas = {'manufactureOrderCode': manufactureOrderCode, 'postingMonth': postingMonth,
                 'materielCode': materielCode, 'postingDate': postingDate}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 技术性完成
    def test_TechComplete(self, manufactureOrderCode, materielCode, postingMonth):
        url = self.host + '/processing_fee_settlement/tech_complete'
        datas = {'manufactureOrderCode': manufactureOrderCode, 'materielCode': materielCode,
                 'postingMonth': postingMonth}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 物料凭证导出
    def test_MMExport(self, postingMonth):
        url = self.host + '/processing_fee_settlement/async_export'
        datas = {'postingMonth': postingMonth}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

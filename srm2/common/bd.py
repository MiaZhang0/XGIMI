import requests
from srm2.common.gettoken import gettoken_OA

# 基础数据
class TestBd():
    def __init__(self):
        self.host = 'http://srm-in.t.xgimi.com/apis'
        self.token = gettoken_OA('xiaomei.zhang', 'Xx123456')

    # supplierGroup=None,内部用户不能关联供应商；供应商角色才能关联供应商
    def test_user_login_update(self, id, purchaserCode, purchasingGroup, supplierGroup=None):
        url = 'http://srm-in.d.xgimi.com/apis' + '/user_login/update'
        datas = {'id': id, 'purchaserCode': purchaserCode, 'purchasingGroup': purchasingGroup,
                 'supplierGroup': supplierGroup}
        print(datas)
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message
msg = TestBd().test_PoItemPre_delivery('poItemList', '4200000006', '10', '251-00816-001', '2002', '1020', '3117',
                                       '如323', 'zxm11')
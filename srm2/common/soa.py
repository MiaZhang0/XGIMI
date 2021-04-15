import requests
from srm2.common.gettoken import gettoken_OA


# 采购对账、供应商对账
class TestSoa():
    def __init__(self):
        self.host = 'http://srm-in.t.xgimi.com/apis'
        self.token = gettoken_OA('xiaomei.zhang', 'Xx123456')

    # 采购对账-交货明细
    def test_purDDList(self, companyCode=None, postingDateBegin=None, postingDateEnd=None, supplierCode=None,
                       purchaserConfirmed=None, supplierConfirmed=None, reconciliationNoteCreated=None,
                       purchaseOrderType=None):
        url = self.host + '/delivery_detail/list'
        datas = {'companyCode': companyCode, 'postingDateBegin': postingDateBegin, 'postingDateEnd': postingDateEnd,
                 'supplierCode': supplierCode, 'purchaserConfirmed': purchaserConfirmed,
                 'supplierConfirmed': supplierConfirmed,
                 'reconciliationNoteCreated': reconciliationNoteCreated, 'purchaseOrderType': purchaseOrderType}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 供应商对账-交货明细
    def test_supDDList(self, companyCode, postingDateBegin, postingDateEnd, supplierConfirmed=None,
                       reconciliationNoteCreated=None):
        url = self.host + '/delivery_detail/list_supplier_confirm'
        datas = {'companyCode': companyCode, 'postingDateBegin': postingDateBegin, 'postingDateEnd': postingDateEnd,
                 'supplierConfirmed': supplierConfirmed, 'reconciliationNoteCreated': reconciliationNoteCreated}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 交货明细确认
    def test_DDConfirm(self, batchType, list):
        url = self.host + '/delivery_detail/confirm'
        datas = {'batchType': batchType, 'deliveryDetailList': list}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 交货明细取消确认
    def test_DDUnconfirm(self, batchType, list):
        url = self.host + '/delivery_detail/cancel_confirm'
        datas = {'batchType': batchType, 'deliveryDetailList': list}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 供应商对账-修改备注
    def test_DDRemark(self, id, remark):
        url = self.host + '/delivery_detail/remark'
        datas = {'id': id, 'remark': remark}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 交货明细导出
    def test_DDExport(self, companyCode, postingDateBegin, postingDateEnd, supplierCode, purchaserConfirmed,
                      supplierConfirmed, reconciliationNoteCreated, purchaseOrderType=None):
        url = self.host + '/delivery_detail/async_export'
        datas = {'companyCode': companyCode, 'postingDateBegin': postingDateBegin, 'postingDateEnd': postingDateEnd,
                 'supplierCode': supplierCode,'purchaserConfirmed': purchaserConfirmed,
                 'supplierConfirmed': supplierConfirmed,'reconciliationNoteCreated': reconciliationNoteCreated,
                 'purchaseOrderType': purchaseOrderType}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 供应商对账-生成对账单
    def test_CRN(self, companyCode, supplierCode, postingDateBegin, postingDateEnd, list):
        url = self.host + '/delivery_detail/create_reconciliation_note'
        datas = {'companyCode': companyCode, 'supplierCode': supplierCode, 'postingDateBegin': postingDateBegin,
                 'postingDateEnd': postingDateEnd, 'deliveryDetailList': list}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 对账单列表
    def test_RNList(self, supplierCode=None, companyCode=None, settlementBeginDate=None, settlementEndDate=None,
                    invoiceCreated=None, reconciliationNoteCode=None):
        url = self.host + '/reconciliation_note/list'
        datas = {'supplierCode': supplierCode, 'companyCode': companyCode, 'settlementBeginDate': settlementBeginDate,
                 'settlementEndDate': settlementEndDate, 'invoiceCreated': invoiceCreated,
                 'reconciliationNoteCode': reconciliationNoteCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 对账单明细列表
    def test_RNItemList(self, supplierCode=None, companyCode=None, settlementBeginDate=None, settlementEndDate=None,
                        reconciliationNoteCode=None, invoiceCreated=None):
        url = self.host + '/reconciliation_note_item/list'
        datas = {'supplierCode': supplierCode, 'companyCode': companyCode, 'settlementBeginDate': settlementBeginDate,
                 'settlementEndDate': settlementEndDate, 'reconciliationNoteCode': reconciliationNoteCode,
                 'invoiceCreated': invoiceCreated}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 对账单明细导出
    def test_RNItemExport(self, supplierCode=None, companyCode=None, settlementBeginDate=None, settlementEndDate=None):
        url = self.host + '/reconciliation_note_item/async_export'
        datas = {'supplierCode': supplierCode, 'companyCode': companyCode, 'settlementBeginDate': settlementBeginDate,
                 'settlementEndDate': settlementEndDate}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 登记发票
    def test_RegInvoice(self, reconciliationNoteCode, invoiceList, remark=None):
        url = self.host + '/invoice/record_note'
        datas = {'reconciliationNoteCode': reconciliationNoteCode, 'invoiceList': invoiceList, 'remark': remark}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 发票明细分页查询
    def test_InvoiceItemList(self, reconciliationNoteCode):
        url = self.host + '/invoice/list'
        datas = {'reconciliationNoteCode': reconciliationNoteCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 批量作废对账单
    def test_UnRN(self, idList):
        url = self.host + '/reconciliation_note/cancel_ReconciliationNote'
        datas = {'idList': idList}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 对账单导出
    def test_RNExport(self, reconciliationNoteCode=None, supplierCode=None, companyCode=None, settlementBeginDate=None,
                      settlementEndDate=None, invoiceCreated=None):
        url = self.host + '/reconciliation_note/export'
        datas = {'reconciliationNoteCode': reconciliationNoteCode, 'supplierCode': supplierCode,
                 'companyCode': companyCode,
                 'settlementBeginDate': settlementBeginDate, 'settlementEndDate': settlementEndDate,
                 'invoiceCreated': invoiceCreated}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 采购对账-对账单确认入账
    def test_paConfirm(self, idList):
        url = self.host + '/reconciliation_note/posting_account'
        datas = {'idList': idList}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

    # 采购对账-对账单取消确认入账
    def test_paUnConfirm(self, idList):
        url = self.host + '/reconciliation_note/posting_account_cancel'
        datas = {'idList': idList}
        header = {'token': self.token}
        r = requests.post(url, json=datas, headers=header)
        message = r.json()
        return message

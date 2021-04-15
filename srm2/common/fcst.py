import requests
from srm2.common.gettoken import gettoken_OA
from requests_toolbelt import MultipartEncoder


# FCST管理
class TestFcst():
    def __init__(self):
        self.host = 'http://srm-in.t.xgimi.com/apis'
        self.token = gettoken_OA('xiaomei.zhang', 'Xx123456')

    # FCST列表
    def testFCSTlist(self, forecastWeek=None, purchaserCode=None):
        url = self.host + '/forecast/list'
        datas = {'forecastWeek': forecastWeek, 'purchaserCode': purchaserCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas,headers=header)
        message = r.json()
        return message

    # MRP明细
    def testMRPlist(self, forecastWeek,forecastVersion, companyCode=None, supplierCode=None, purchaserCode=None):
        url = self.host + '/mrp/list'
        datas = {'forecastWeek': forecastWeek,'forecastVersion': forecastVersion, 'companyCode': companyCode, 'supplierCode': supplierCode,
                 'purchaserCode': purchaserCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas,headers=header)
        message = r.json()
        return message

    # MRP解锁
    def testMRPunlock(self, id):
        url = self.host + '/mrp/unlock'
        # MRP主键
        datas = {'id': id}
        header = {'token': self.token}
        r = requests.post(url, data=datas, headers=header)
        message = r.json()
        return message

    # FCST明细列表
    def testForecast(self, forecastWeek=None, purchaserCode=None, supplierCode=None):
        url = self.host + '/forecast_item/list'
        datas = {'forecastWeek': forecastWeek, 'purchaserCode': purchaserCode, 'supplierCode': supplierCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas,headers=header)
        message = r.json()
        return message

    # FCST明细列表-确认
    def testForecastConfirm(self, id):
        url = self.host + '/forecast_item/confirm'
        datas = {'id': id}
        header = {'token': self.token, 'Content-Type': 'application/json'}
        r = requests.post(url, headers=header, data=datas)
        message = r.json()
        return message

    # FCST明细列表-取消确认
    def testForecastUnconfirm(self, id):
        url = self.host + '/forecast_item/un_confirm'
        datas = {'id': id}
        header = {'token': self.token, 'Content-Type': 'application/json'}
        r = requests.post(url, headers=header, data=datas)
        message = r.json()
        return message

    # MRP明细导出
    def testMRPDetail(self, forecastWeek, forecastVersion,t,companyCode=None, supplierCode=None, purchaserCode=None):
        url = self.host + '/mrp/export_mrp_detail'
        datas = {'forecastWeek': forecastWeek,'forecastVersion':forecastVersion, 't':t,'companyCode': companyCode, 'purchaserCode': purchaserCode,
                 'supplierCode': supplierCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # MRP汇总
    def testMRPSum(self, forecastWeek, forecastVersion,companyCode=None, supplierCode=None, purchaserCode=None):
        url = self.host + '/mrp_sum/list'
        datas = {'forecastWeek': forecastWeek, 'forecastVersion': forecastVersion, 'companyCode': companyCode,
                 'purchaserCode': purchaserCode, 'supplierCode': supplierCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # MRP汇总导出
    def testMRPExport(self, forecastWeek, forecastVersion,t,companyCode=None, supplierCode=None, purchaserCode=None):
        url = self.host + '/mrp_sum/export'
        datas = {'forecastWeek': forecastWeek, 'forecastVersion': forecastVersion, 't': t, 'companyCode': companyCode, 'purchaserCode': purchaserCode,
                 'supplierCode': supplierCode}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 导出交期回复数据
    def testMRPAsyncExport(self, forecastWeek, forecastVersion, t):
        url = self.host + '/mrp/async_export'
        datas = {'forecastWeek': forecastWeek, 'forecastVersion': forecastVersion, 't': t}
        header = {'token': self.token}
        r = requests.get(url, params=datas, headers=header)
        message = r.json()
        return message

    # 交期回复导入
    def testMRPImportFile(self, file, forecastWeek, forecastVersion):
        url = self.host + '/mrp/mrp_import_file'
        m = MultipartEncoder({'forecastWeek': forecastWeek, 'forecastVersion': forecastVersion, 'file': file})
        header = {'token': self.token, 'Content-Type': m.content_type}
        r = requests.post(url, data=m, headers=header)
        message = r.json()
        return message

    # FCST周列表
    def testForcastWeek(self):
        url = self.host + '/forecast/forecast_week'
        header = {'token': self.token}
        r = requests.get(url,headers=header)
        message = r.json()
        return message



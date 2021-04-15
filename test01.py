import requests

# FCST管理
class TestFcstModule():
    def __init__(self):
        self.host = 'http://srm-in.t.xgimi.com/apis'

    # FCST列表
    def testFCSTlist(self, forecastWeek=None, purchaserCode=None):
        url = self.host + '/forecast/list'
        datas = {'forecastWeek': forecastWeek, 'purchaserCode': purchaserCode}
        r = requests.get(url, params=datas)
        message = r.json()
        return message

    # MRP明细
    def testMRPlist(self, forecastWeek, companyCode=None, supplierCode=None, purchaserCode=None):
        url = self.host + '/mrp/list'
        datas = {'forecastWeek': forecastWeek, 'companyCode': companyCode, 'supplierCode': supplierCode,
                 'purchaserCode': purchaserCode}
        r = requests.get(url, params=datas)
        message = r.json()
        return message

    # MRP解锁
    def testMRPunlock(self, id):
        url = self.host + '/mrp/unlock'
        # MRP主键
        datas = {'id': id}
        r = requests.post(url, data=datas)
        message = r.json()
        return message

    # FCST明细列表
    def testForecast(self, forecastWeek, purchaserCode=None, supplierCode=None):
        url = self.host + '/forecast_item/list'
        datas = {'forecastWeek': forecastWeek, 'purchaserCode': purchaserCode, 'supplierCode': supplierCode}
        r = requests.get(url, params=datas)
        message = r.json()
        return message

    # FCST明细列表-确认
    def testForecastConfirm(self, id):
        url = self.host + '/forecast_item/confirm'
        datas = {'id': id}
        header = {'Content-Type': 'application/json'}
        r = requests.post(url, headers=header, data=datas)
        message = r.json()
        return message

    # FCST明细列表-取消确认
    def testForecastUnconfirm(self, id):
        url = self.host + '/forecast_item/un_confirm'
        datas = {'id': id}
        header = {'Content-Type': 'application/json'}
        r = requests.post(url, headers=header, data=datas)
        message = r.json()
        return message

    # MRP明细导出
    def testMRPDetail(self, forecastWeek, companyCode=None, supplierCode=None, purchaserCode=None):
        url = self.host + '/mrp/export_mrp_detail'
        datas = {'forecastWeek': forecastWeek, 'companyCode': companyCode, 'purchaserCode': purchaserCode,
                 'supplierCode': supplierCode}
        r = requests.get(url, params=datas)
        message = r.json()
        return message

    # MRP汇总
    def testMRPSum(self, forecastWeek, companyCode=None, supplierCode=None, purchaserCode=None):
        url = self.host + '/mrp_sum/list'
        datas = {'forecastWeek': forecastWeek, 'companyCode': companyCode, 'purchaserCode': purchaserCode,
                 'supplierCode': supplierCode}
        r = requests.get(url, params=datas)
        message = r.json()
        return message

    # MRP汇总导出
    def testMRPExport(self, forecastWeek, companyCode=None, supplierCode=None, purchaserCode=None):
        url = self.host + '/mrp_sum/export'
        datas = {'forecastWeek': forecastWeek, 'companyCode': companyCode, 'purchaserCode': purchaserCode,
                 'supplierCode': supplierCode}
        r = requests.get(url, params=datas)
        message = r.json()
        return message

    # 导出交期回复数据
    def testMRPAsyncExport(self, forecastWeek):
        url = self.host + '/mrp/async_export'
        datas = {'forecastWeek': forecastWeek}
        r = requests.get(url, params=datas)
        message = r.json()
        return message

    # 交期回复
    def testMRPImportFile(self, file, forecastWeek):
        url = self.host + '/mrp/mrp_import_file'
        datas = {'file': file, 'forecastWeek': forecastWeek}
        r = requests.get(url, params=datas)
        message = r.json()
        return message

    # FCST周列表
    def testForcastWeek(self):
        url = self.host + '/forecast/forecast_week'
        r = requests.get(url)
        message = r.json()
        return message


t = TestFcstModule()
print(t.testForecast('2020年-第44周'))

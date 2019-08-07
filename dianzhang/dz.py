import hashlib

# origin url
# https://api.dianzhangzhipin.com/api/batch/run?batchMethodFeed=["method=geek.search.boss.v3&page=1&lng=116.410242&positionIndex=0&positionId=95395081&positionCode=41140&lat=39.916403&cityCode=7&district=&area=&salaryCode=0&sortType=1&roam=-1","method=common.ad"]&curidentity=1&v=4.302&app_id=1001&req_time=1565151142040&uniqid=E321EBA9DF42B24AA127F41BB7105790&client_info={"version":"5.1.1","os":"Android","start_time":"1565148730525","resume_time":"1565148730525","channel":"0","model":"gionee||0g1s","ssid":"FAST-knh6-5G","bssid":"00:C8:1D:07:A3:6D","network":"wifi","imei":"351512327287255","dzt":1}&t=BBmlQQQA0UmhUZgBmW2EHYgI0AjNRYAdjCGdaaQ..&sig=f2d4697ced4377606ca7980c437ee661
# https://api.dianzhangzhipin.com/api/batch/run?batchMethodFeed=["method=geek.search.boss.v3&page=1&lng=116.410242&positionIndex=0&positionId=95395081&positionCode=41140&lat=39.916403&cityCode=7&district=&area=&salaryCode=0&sortType=1&roam=-1","method=common.ad"]&curidentity=1&v=4.302&app_id=1001&req_time=1565151142040&uniqid=E321EBA9DF42B24AA127F41BB7105790&client_info={"version":"5.1.1","os":"Android","start_time":"1565148730525","resume_time":"1565148730525","channel":"0","model":"gionee||0g1s","ssid":"FAST-knh6-5G","bssid":"00:C8:1D:07:A3:6D","network":"wifi","imei":"351512327287255","dzt":1}&t=BBmlQQQA0UmhUZgBmW2EHYgI0AjNRYAdjCGdaaQ..&sig=f2d4697ced4377606ca7980c437ee661
# https://....sig=f2d4697ced4377606ca7980c437ee661

### 2. localParams
# localParams = {
#     'batchMethodFeed': '["method=geek.search.boss.v3&page=1&lng=116.410242&positionIndex=0&positionId=95395081&positionCode=41140&lat=39.916403&cityCode=7&district=&area=&salaryCode=0&sortType=1&roam=-1","method=common.ad"]',
#     'curidentity': 1,
#     'v': 4.302,
#     'app_id': 1001,
#     'req_time': 1565151142040,
#     'uniqid': 'E321EBA9DF42B24AA127F41BB7105790',
#     'client_info': '{"version":"5.1.1","os":"Android","start_time":"1565148730525","resume_time":"1565148730525","channel":"0","model":"gionee||0g1s","ssid":"FAST-knh6-5G","bssid":"00:C8:1D:07:A3:6D","network":"wifi","imei":"351512327287255","dzt":1}',
#     't': 'BBmlQQQA0UmhUZgBmW2EHYgI0AjNRYAdjCGdaaQ..'
# }

# localParams_sort = sorted(localParams.items(), key=lambda item: item[0])
# # print(localParams_sort)
#
# str_local = ''
# for k, v in localParams_sort:
#     str_local += '{}={}'.format(k, v)
#
# print(str_local[:5000])
#
# p1 = '/api/batch/run'
# p2 = str_local[:5000]
# p3 = '9f738a3934abf88b1dca8e8092043fbd'
#
# res = hashlib.md5((p1 + p2 + p3).encode()).hexdigest()
# print(res)
import requests


class DZ:
    def __init__(self):
        pass

    def calc_sign(self, params, route):
        """
        计算sign值
        :route: url里的路由，eg: '/api/batch/run'
        """
        # params按key升序排序
        paramsSort = sorted(params.items(), key=lambda item: item[0])

        # 排序好的k，v拼接
        str_local = ''
        for k, v in paramsSort:
            str_local += '{}={}'.format(k, v)

        p1 = route
        # 超过5000截断
        p2 = str_local[:5000]
        p3 = '9f738a3934abf88b1dca8e8092043fbd'  # app里的秘钥
        return hashlib.md5((p1 + p2 + p3).encode()).hexdigest()

    def request_refresh_home_page(self):
        """首页的下拉刷新"""
        params = {
            'batchMethodFeed': '["method=geek.search.boss.v3&page=1&lng=116.410242&positionIndex=0&positionId=95395081&positionCode=41140&lat=39.916403&cityCode=7&district=&area=&salaryCode=0&sortType=1&roam=-1","method=common.ad"]',
            'curidentity': 1,
            'v': 4.302,
            'app_id': 1001,
            'req_time': 1565151142044,
            'uniqid': 'E321EBA9DF42B24AA127F41BB7105790',
            'client_info': '{"version":"5.1.1","os":"Android","start_time":"1565148730525","resume_time":"1565148730525","channel":"0","model":"gionee||0g1s","ssid":"FAST-knh6-5G","bssid":"00:C8:1D:07:A3:6D","network":"wifi","imei":"351512327287255","dzt":1}',
            't': 'BBmlQQQA0UmhUZgBmW2EHYgI0AjNRYAdjCGdaaQ..'
        }
        route = '/api/batch/run'

        sign = self.calc_sign(params, route)
        print('calc sign:', sign)

        params['sig'] = sign

        url = 'https://api.dianzhangzhipin.com/api/batch/run'
        return requests.get(url, params=params).content.decode()

    def request_job_detail_page(self):
        params = {'jobId': '5043072',
                  'lid': '',
                  'lid2': 'F1-geek-flowpage',
                  'specialTag': '',
                  'curidentity': 1,
                  'v': 4.302,
                  'app_id': 1001,
                  'req_time': 1565161911862,
                  'uniqid': 'E321EBA9DF42B24AA127F41BB7105790',
                  'client_info': '{"version":"5.1.1","os":"Android","start_time":"1565148730525","resume_time":"1565148730525","channel":"0","model":"gionee||0g1s","ssid":"FAST-knh6-5G","bssid":"00:C8:1D:07:A3:6D","network":"wifi","imei":"351512327287255","dzt":1}',
                  't': 'BBmlQQQA0UmhUZgBmW2EHYgI0AjNRYAdjCGdaaQ..'}

        route = '/api/job/detail'
        sign = self.calc_sign(params, route)
        print('calc sign:', sign)

        params['sig'] = sign

        url = 'https://api.dianzhangzhipin.com/api/job/detail'
        return requests.post(url, data=params).content.decode()

    def test_request(self, params, route):
        sign = self.calc_sign(params, route)
        print('calc sign:', sign)

        params['sig'] = sign

        url = 'https://api.dianzhangzhipin.com/api/batch/run'
        print(requests.get(url, params=params).content.decode())


if __name__ == '__main__':
    d = DZ()
    # print(d.request_refresh_home_page())
    print(d.request_job_detail_page())

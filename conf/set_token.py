import requests
from conf.settings import *
from common.get_data import GetData
from time import  sleep

# 获取各个平台的token ,初始化header登录状态
class Get_Token:
    global headers  # 设置全局变量heaers存放在字典里面
    headers = {}

    # 全局变量token,header 值
    def __init__(self):
        self.app_phone = app_phone
        self.rider_phone = rider_phone
        self.wei_phone = wei_phone
        self.app_host = app_host
        self.wei_host = wei_host
        self.rider_host = rider_host
        self.cloud_host = cloud_host

    def app_url(self, api):
        url = self.app_host + api
        return url

    def rider_url(self, api):
        url = self.rider_host + api
        return url

    def wei_url(self, api):
        url = self.wei_host + api
        return url

    def cloud_url(self, api):
        url = self.cloud_host + api
        return url

    def app_token(self):  # 发短信验证码登录
        url = 'https://rtapi-qa002.blissmall.net/apis/authc/anon/sms/V1.0.0/sendSmsCode'
        header = {'client-id': 'A8D45196C1B24F24BD373D01F86723C4', 'channel-id': '1102',
                  'sign': '190717173620303GJg8lRRlXE6fHE+vs7Czc2QhzPc0gxKabxOgRL4Tfb/dMq31+4rqr7g02Q3doaQF',
                  'content-type': 'application/json', 'charset': 'UTF-8', 'content-length': '83',
                  'accept-encoding': 'gzip',
                 'user-agent':	'XFGProject/2.0.0 (iPhone; iOS 12.3.1; Scale/3.00)',
                  "token":'aa9fa822-2613-42b5-8ae6-184eeaddc93d'
                  }
        data = {
	"mobile": "13267166832",
	"typeCode": "retailUserLogin"
}
        data["mobile"] = self.app_phone
        self.run_main('post', url, data, header)
        try:
            url = 'https://rtapi-qa002.blissmall.net/apis/auth/userApp/V1.0.0/loginBySms'
            data ={
        "smsCode": "123456",
        "mobile": "13267166832",
        "loginType": "1"
    }
            data["mobile"] = self.app_phone
            re = self.run_main('post', url, data, header)
            header['token'] = re.json()['data']["authMemberInfo"]['token']
            self.userId = re.json()['data']["authMemberInfo"]['userId']
            headers['app'] = header
            return header
        except:
            print('APP登录失败')
        headers['app'] = header
        return header

    def rider_token(self):
        url = 'https://retailadmin-qa002.blissmall.net/apis/auth/appUser/login'
        data = {"clientType": "3", "loginName": "12222222222", "loginType": "1", "password": "sz123456"}
        data["loginName"] = self.rider_phone
        header = {'accept': 'application/json',
                  'accept-encoding': 'gzip, deflate',
                  'accept-charset': 'UTF-8,*;q=0.5',
                  'cache-control': 'no-cache',
                  'client-type': '3',
                  'version': '1.2.0',
                  'ua': 'RiderApp/1.2.0/Android/6.0/Redmi Note 4/78:02:F8:72:2B:09/com.xfxb.rider/1920/1080/73dd6a28-9855-4c46-8237-0036292f862a/3',
                  'content-type': 'application/json',
                  'content-length': '82',
                  'user-agent': 'okhttp/3.11.0',
                  }
        res = self.run_main("post", url, data, header)
        header['token'] = res.json()['data']['token']
        headers['rider'] = header
        return header

    def cloud_token(self):
        header = {'accept': 'application/json',
                  'accept-encoding': 'gzip, deflate',
                  'accept-charset': 'UTF-8,*;q=0.5',
                  'cache-control': 'no-cache',
                  'client-type': '3',
                  'cookie': 'gr_user_id=2af98dbd-db03-4ac5-8b6c-1f9a84b9463b; _ga=GA1.2.2074536304.1558689151',
                  'content-type': 'application/json',
                  'content-length': '82',
                  'user-agent': 'okhttp/3.11.0',
                  }
        data = {
            "loginName": "system",
            "password": "123456",
            "verifyCode": "z",
            "loginType": 1,
            "clientType": 1,
            "verifyId": "1f73bf75-242f-4137-b641-abf6269ae6ef"
        }
        url = 'https://retailadmin-qa002.blissmall.net/apis/auth/sysUser/login'
        res = self.run_main('post', url, data, header)
        header['token'] = res.json()['data']['token']
        headers['cloud'] = header
        return header

    def wei_token(self):
        header = {
            "client-id": "10",
            "channel-id": "1301",
            'Content-Type': 'application/json',
            "content-type": "application/json;charset=UTF-8",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-cn",
            "accept-encoding": "br, gzip, deflate",
            "origin": "https://m-qa002.xfxb.net",
            "referer": "https://m-qa002.xfxb.net/mall/order/confirm",
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.4(0x17000428) NetType/WIFI Language/zh_CN",
            "cookie":"_ga=GA1.2.1005703224.1559028545"
        }
        data = {
            "mobile": "13267166832",
            "typeCode": "wechatH5UserLogin"
        }
        data["mobile"] = self.wei_phone
        url = 'https://rtapi-qa002.blissmall.net/apis/authc/wap/sms/sendSmsCodeAnonymous'
        self.run_main('post', url, data, header)

        url = 'https://m-qa002.xfxb.net/restapi/auth/wap/loginBySms'
        data = {
            "mobile": "11111111111",
            "smsCode": "123456",
        }
        data["mobile"] = self.wei_phone
        res = self.run_main('post', url, data, header)
        header['token'] = res.json()['data']["authMemberInfo"]['token']

        headers['wei'] = header
        return header

    def save_token(self, client_type):
        if client_type == 'app':
            self.app_token()
        elif client_type == 'cloud':
            self.cloud_token()
        elif client_type == 'rider':
            self.rider_token()
        elif client_type == 'wei':
            self.wei_token()
        return headers
    def get_url(self, client_type,api):
        if client_type == 'app':
            return self.app_url(api)
        elif client_type == 'cloud':
            return self.cloud_url(api)
        elif client_type == 'rider':
            return self.rider_url(api)
        elif client_type == 'wei':
            return  self.wei_url(api)

    def get_header(self, row):
        client_type = GetData().get_client_type(row)
        print(client_type)
        if not headers.__contains__(client_type):
            self.save_token(client_type)
        return headers[client_type]

    def send_post(self, url, data, header):
        result = requests.post(url=url, json=data, headers=header)
        return result

    def send_get(self, url, data, header):
        result = requests.get(url=url, json=data, headers=header)
        return result

    def run_main(self, method, url=None, data=None, header=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data, header)
        elif method == 'get':
            result = self.send_get(url, data, header)
        else:
            print("请求方式错误")
        return result

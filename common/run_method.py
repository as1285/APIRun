import requests
from json import dumps
from APIRun.logs.logger import Logger

logger = Logger().logger
class RunMethod:
    def send_post(self, url, header, data):
        try:
            res = requests.post( url=url, json=data, headers=header)
            self.api_log('post',url=url, json=data, headers=header,
                         code=res.status_code, res_text=res.text, res_header=res.headers)
            return res
        except Exception as e:
            logger.error("接口请求异常,原因：{}".format(e))
            raise e

    def send_get(self, url, header, data):
        try:
            res = requests.get( url=url, json=data, headers=header)
            self.api_log('get',url=url, json=data, headers=header,
                         code=res.status_code, res_text=res.text, res_header=res.headers)
            return res
        except Exception as e:
            logger.error("接口请求异常,原因：{}".format(e))
            raise e

    def run_main(self, method, url=None,header=None, data=None):
        result = None
        if method == 'post':
            result = self.send_post(url, header, data)
        elif method == 'get':
            result = self.send_get(url, header, data)
        else:
            print("请求方式错误")
        return result
    def api_log(self,method,url,headers=None,params=None,json=None,cookies=None,file=None,code=None,res_text=None,res_header=None):
        logger.info("请求方式====>{}".format(method))
        logger.info("请求地址====>{}".format(url))
        logger.info("请求头====>{}".format(dumps(headers,indent=4)))
        logger.info("请求参数====>{}".format(dumps(params,indent=4)))
        logger.info("请求体====>{}".format(dumps(json,indent=4)))
        logger.info("上传附件为======>{}".format(file))
        logger.info("Cookies====>{}".format(dumps(cookies,indent=4)))
        logger.info("接口响应状态码====>{}".format(code))
        logger.info("接口响应头为====>{}".format(res_header))
        logger.info("接口响应体为====>{}".format(res_text))
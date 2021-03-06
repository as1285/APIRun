
from common.run_method import RunMethod
from common.get_data import GetData
from common.assert_result import CommonUtil
import json
from common.depend_data import DependdentData

from conf.set_token import Get_Token

class RunTest:
    pass_count = []
    fail_count = []
    def __int__(self):
        self.run_method =RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()

    def go_on_run(self,i):#运行总函数

        # rows_count = GetData().get_case_lines()
        # for i in range(1,rows_count):
        is_run = GetData().get_is_run(i)
        if is_run:
            url = Get_Token().get_url(client_type=GetData().get_client_type(i),api=GetData().get_api(i))
            method = GetData().get_request_method(i)
            case_name =GetData().get_case_name(i)
            data = GetData().get_data(i)
            # print(url,data,method)
            data = json.loads(data)
            header = Get_Token().get_header(i)
            expect = GetData().get_expect_data(i)
            depend_case=GetData().is_depend(i)
            if depend_case !=None:
                #获取响应数据
                self.depend = DependdentData(depend_case)
                depend_response_data=self.depend.get_data_for_key(i)
                #获取依赖的key
                depend_key =GetData().get_depend_field(int(depend_case))
                data[depend_key]=depend_response_data
                RunMethod().run_main(method, url, header, data)

            res = RunMethod().run_main(method,url,header,data)
            if CommonUtil().is_content(expect,res.text):
                GetData().write_result(i,'测试通过')
                self.pass_count.append(i)
            else:
                GetData().write_result(i, res.text)
                self.fail_count.append(i)
            return[i,case_name,method,url,data,expect,res.text]



if __name__ == '__main__':
    run = RunTest()
    rows_count = GetData().get_case_lines()
    for i in range(1,rows_count):
        run.go_on_run(i)

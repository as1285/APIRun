from common.operation_excel import OperationExcel
from common.run_method import RunMethod
from common.get_data import GetData
import json
from jsonpath_rw import jsonpath,parse
from conf.set_token import Get_Token
class DependdentData:
    def __init__(self,case_id):
        self.case_id = case_id
    def get_case_line_data(self):
        rows_data=OperationExcel().get_rows_data(self.case_id)
        return rows_data
    #执行依赖结果，获取数据
    def run_dependdent(self):
        row_num=OperationExcel().get_row_num(self.case_id)
        url = Get_Token().get_url(client_type=GetData().get_client_type(row_num), api=GetData().get_api(row_num))
        method = GetData().get_request_method(row_num)
        data = GetData().get_data(row_num)
        data = json.loads(data)
        header = Get_Token().get_header(row_num)
        res = RunMethod().run_main(method, url, header, data)
        return res.json()
    #根据依赖的key获取执行依赖测试case响应，然后返回
    def get_data_for_key(self,row):
        depend_data = GetData().get_depend_key(row)
        respond_data = self.run_dependdent()
        json_exe = parse(depend_data)
        madle=json_exe.find(respond_data)
        try:
            print('获取依赖参数成功：',[math.value for math in madle][0])
            return [math.value for math in madle][0]
        except IndexError:
            print('获取依赖参数失败',respond_data['message'])

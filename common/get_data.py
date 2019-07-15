from common.operation_excel  import OperationExcel
from conf import data_conf
from common.openration_json import  OperationJson

import json
class GetData:
    def __init__(self):
        self.operation_excel = OperationExcel()
     #去获取excel 的行数，也就是用例的个数
    def get_case_lines(self):
        return self.operation_excel.get_lines()
    #获取是否执行
    def get_is_run(self,row):
        col = data_conf.get_run()
        run_model = self.operation_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag
    #获取请求方法
    def get_request_method(self,row):
        col = data_conf.get_runway()
        request_method = self.operation_excel.get_cell_value(row,col)
        return request_method
    #获取客户端类型 新零售 还是微商城
    def get_client_type(self,row):
        col = data_conf.get_client_type()
        client_type= self.operation_excel.get_cell_value(row,col)
        return client_type
    #获取请求接口URL
    def get_request_url(self,row):
        host_col = data_conf.get_host()
        api_col = data_conf.get_api()
        url = self.operation_excel.get_cell_value(row,host_col)+self.operation_excel.get_cell_value(row,api_col)
        return url
    def get_api(self,row):
        api_col = data_conf.get_api()
        api = self.operation_excel.get_cell_value(row, api_col)
        return api



    #获取请求数据
    def get_data(self,row):
        col = data_conf.get_data()
        data = self.operation_excel.get_cell_value(row,col)
        return data
    #通过关键字拿到data数据
    def get_data_for_json(self):
        oper_json =OperationJson()
        request_data =oper_json.get_data()
        return request_data
    def get_header(self,row):
        col = data_conf.get_header()
        header =self.operation_excel.get_cell_value(row,col)
        return header
    def get_expect_data(self,row):
        col = data_conf.get_expect()
        expect_data = self.operation_excel.get_cell_value(row, col)
        return expect_data
    # 写入数据
    def write_result(self,row,value):
        col = int(data_conf.get_result())
        self.operation_excel.write_excel(row,col,value)
    #获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data_conf.get_data_depend())
        depend_key=self.operation_excel.get_cell_value(row,col)
        if depend_key=='':
            return None
        else:
            return depend_key
    #判断是否有case依赖
    def is_depend(self,row):
        col=int(data_conf.get_case_depend())
        depend_case_id =self.operation_excel.get_cell_value(row,col)
        if depend_case_id =='':
            return None
        else:
            return depend_case_id
    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(data_conf.get_field_depend())
        data = self.operation_excel.get_cell_value(row, col)
        if data =='':
            return None
        else:
            return data



class global_var:
    #case_id
    Id= 0
    client_type=1
    request_name = 2
    host = 3
    api=4
    run = 5
    request_way = 6
    header = 7
    case_depend = 8
    data_depend = 9
    field_depend = 10
    data = 11
    expect = 12
    result = 13
def get_id():
    return global_var.Id
def get_client_type():
    return global_var.client_type
def get_host():
    return global_var.host
def get_api():
    return global_var.api
def get_url():
    return global_var.host+global_var.api
def get_run():
    return global_var.run
def get_runway():
    return global_var.request_way
def get_header():
    return global_var.header
def get_case_depend():
    return global_var.case_depend
def get_data_depend():
    return global_var.data_depend
def get_field_depend():
    return global_var.field_depend
def get_data():
    return global_var.data
def get_expect():
    return global_var.expect
def get_result():
    return global_var.result



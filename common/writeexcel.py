# coding:utf-8
import xlrd
from xlutils.copy import copy


def copy_excel(excelpath1, excelpath2):
    '''复制excek，把excelpath1数据复制到excelpath2'''

    # 读取数据
    wb1 = xlrd.open_workbook(excelpath1)
    wb2 = copy(wb1)
    sheet1 = wb1.sheets()[0]
    max_row = sheet1.nrows
    max_column = sheet1.ncols  # 最大列数

    for m in list(range(max_row)):
        for n in list(range(max_column)):
            cell1 = sheet1.cell_value(m,n)              # 获取data单元格数据
            wb2.get_sheet(0).write(m, n,cell1)              # 赋值到test单元格

    wb2.save(excelpath2)                 # 保存数据

class Write_excel(object):
    '''修改excel数据'''
    def __init__(self, filename):
        self.filename = filename
        self.wb = xlrd.open_workbook(self.filename)

    def write(self, row_n, col_n, value):
        '''写入数据，如(2,3，"hello"),第二行第三列写入数据"hello"'''
        wb = copy(self.wb)
        wb.get_sheet(0).write(row_n, col_n, value)
        wb.save(self.filename)



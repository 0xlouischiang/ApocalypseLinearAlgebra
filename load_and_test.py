import xlrd
from scipy.stats import shapiro


def config_data():
    xl = xlrd.open_workbook(r'./data/20200101.xls')
    table = xl.sheets()[0]
    col = table.col_values(1)
    return col
import xlrd
from scipy.stats import shapiro

xl = xlrd.open_workbook(r'./data/20200101.xls')
table = xl.sheets()[0]
col = table.col_values(1)
print(col)
print("===============")

# Shapiro test
print(shapiro(col))

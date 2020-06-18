import numpy as np
import matplotlib.pyplot as plt

from xlrd import open_workbook
import xlwt


class Dataload:
    def __init__(self):
        pass

    def getData(self):
        workbook = open_workbook(r'20200401.xls')
        sheet = workbook.sheet_by_index(0)
        return sheet

    def getShape(self):
        sor = self.getData()
        print(sor.nrows, sor.ncols)

    def showData(self):
        x_data = []
        y_data = []
        x_volte = []
        temp = []

        sheet = self.getData()
        for row in range(sheet.nrows):
            values = []
            for col in range(sheet.ncols):
                values.append(sheet.cell(row, col).value)
            x_data.append(values[0])
            y_data.append(values[1])
        plt.plot(x_data, y_data, 'bo-', label=u"Phase curve", linewidth=1)
        plt.title(u"Out-flow data")
        plt.legend()

        plt.xlabel(u"Data")
        plt.ylabel(u"COD")

        plt.show()


Dataload().showData()
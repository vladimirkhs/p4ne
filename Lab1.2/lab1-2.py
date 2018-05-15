#
#
#

from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('C:\\Users\\resu\\Desktop\\seafile\\Seafile\\p4ne_training\\data_analysis_lab.xlsx')
sheet = wb['Data']
sheet_A = sheet['A'][1:]
sheet_C = sheet['C'][1:]
sheet_D = sheet['D'][1:]

def getvalue(x):    return x.value

# print(getvalue(sheet_A[1]))

list_A = list(map(getvalue, sheet['A'][1:]))
list_C = list(map(getvalue, sheet['C'][1:]))
list_D = list(map(getvalue, sheet['D'][1:]))

#print(list(list_D))

pyplot.plot(list_A, list_C, label="Метка")
pyplot.plot(list_A, list_D, label="Метка2")

pyplot.show()


#-*- coding: utf-8 -*-
import xlrd
# def getExcleData():
#     try:
#         data = xlrd.open_workbook('doctorAutoCase.xlsx')
#
#     #    print data
#     except Exception,e:
#         print str(e)
#
#     #shrang = range(data.nsheets)
#     sh = data.sheet_by_name("Sheet1")
#     #获取Excel表格里行数。获取列数用nclos
#     cell_value = sh.nrows
#     return cell_value

def getExcleData(i):
    try:
        data = xlrd.open_workbook('doctorAutoCase.xlsx')

    #    print data
    except Exception,e:
        print str(e)

    #shrang = range(data.nsheets)
    sh = data.sheet_by_name("Sheet3")
    #获取Excel表格里的数据，i表示行，j表示列。行和列都是从0开始计数。
    cell_value = sh.cell_value(i,3)
    return cell_value

for i in range(100):
    print(getExcleData(i))
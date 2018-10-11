#-*- coding: utf-8 -*-
import xlrd
#定义函数读取表格的用例内容
def getExcleData(i):
    try:
        data = xlrd.open_workbook('doctorAutoCase.xlsx')

    #    print data
    except Exception,e:
        print str(e)

    #shrang = range(data.nsheets)
    sh = data.sheet_by_name("Sheet1")
    #获取Excel表格里的数据，i表示行，j表示列。行和列都是从0开始计数。
    cell_value = sh.cell_value(i,3)
    return cell_value

if __name__ == '__main__':
    i=0
    getExcleData(i)
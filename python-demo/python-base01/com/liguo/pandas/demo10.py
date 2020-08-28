"""
        "xlrd": _XlrdReader,
        "openpyxl": _OpenpyxlReader,
        "odf": _ODFReader,
        "pyxlsb": _PyxlsbReader,
"""

import xlrd

import xlrd2

import openpyxl

import pyxlsb as px

import pandas as pd

import pylightxl as xl
pd.set_option()
#
# x1 = xlrd2.open_workbook("波士顿房价.xlsx")
# print(x1.sheet_names())
#
#
# table = x1.sheet_by_name('Sheet1')
#
# rowNum = table.nrows
# # print(rowNum)
# # print(table.row_values(0))
#
# # var1 = 10.111
# # print(type(var1))
#
# for i in range(0, rowNum):
#     print(table.row(i))
#     print(table.row_values(i))


#
# list_row=[]
# list_accumulate= []
#
# with px.open_workbook("波士顿房价.xlsx") as wb:
#     sheets = wb.sheets
#     for sheet in sheets:
#         row_generator = wb.get_sheet(sheet).rows()
#         for row in row_generator:
#             for cell in row:
#                 list_row.append(cell.v)
#             list_accumulate.append(list_row)
#             list_row=[]
# df_excel = pd.DataFrame(list_accumulate)
# from openpyxl import load_workbook

#
# wb2 = load_workbook('波士顿房价.xlsx')
#
# print(wb2.get_sheet_names)
#
# ws = wb2.active
#
# print(ws.columns)
#
# print(ws.rows)
#
# for sheet in wb2:
#     print(sheet.title)
#     for row in sheet.rows:
#         for cell in row:
#             print(cell.value)
#
# print(ws.values)


# db = xl.readxl('波士顿房价.xlsx')
#
# # for i in range(0, 500):
# for row in db.ws('Sheet1').rows:
#     print(row)

import datatable as dt

dtf = dt.fread('波士顿房价.xlsx')

print(dtf)
dtf.to_csv("out.csv")
pdt = dtf.to_pandas()
print(pdt)
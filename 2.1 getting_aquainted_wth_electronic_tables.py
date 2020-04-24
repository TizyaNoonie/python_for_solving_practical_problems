# 2.1 Знакомство с электронными таблицами
import xlrd

wb = xlrd.open_workbook('table.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
n_min = sh.row_values(6)[2]
for row_num in range(7, 27):
    temp = sh.row_values(row_num)
    n_min = min(n_min, temp[2])

print(n_min)  # 39650.2

# 2.4 И еще таблицы
import os
import xlrd

salaries = {}

for filename in os.listdir("rogaikopyta"):
    wb = xlrd.open_workbook("rogaikopyta/" + filename)
    sheet = wb.sheet_by_index(0)
    name = sheet.cell(1, 1).value
    salary = int(sheet.cell(1, 3).value)
    salaries[name] = salary

for name in sorted(salaries):
    print(name, salaries[name])  # too many values to display

# 2.2 Работа с одним листом
# Watch your eyes! Better use your code. Seriously
import xlrd

salaries = []
with open("salaries.xlsx", "r") as f:
    wb = xlrd.open_workbook('salaries.xlsx')
    for s in wb.sheets():
        print('Sheet:', s.name)
        for row in range(s.nrows):
            values = []
            for col in range(s.ncols):
                values.append(s.cell(row, col).value)

            salaries.append(values)
all_data = salaries
salaries = salaries[1:]

avg_salary = {}
for salary in salaries:
    key, value = salary[0], salary[1:]
    avg_salary[key] = sum(value) / len(value)

print(sorted(avg_salary, key=lambda k: avg_salary[k], reverse=True))

salary_for_specialist = {}
keys = all_data[0][1:]
salaries = all_data[1:]

index = 1
for key in keys:
    salary_for_specialist[key] = []
    for salary in salaries:
        salary_for_specialist[key].append(salary[index])
    index += 1
for key, value in salary_for_specialist.items():
    print(key, sum(value) / len(value))

# Куала-Лумпур Собачий парикмахер

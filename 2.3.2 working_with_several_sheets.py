# 2.3 Работа с несколькими листами
# WAT?? It worked!
import xlrd

wb = xlrd.open_workbook("trekking2.xlsx")

sheet_0 = wb.sheet_by_index(0)

products = {}
for row in range(1, sheet_0.nrows):
    key = sheet_0.cell(row, 0).value
    products[key] = []
    for col in range(1, sheet_0.ncols):
        value = sheet_0.cell(row, col).value
        products[key].append(value if value else 0)

sheet_1 = wb.sheet_by_index(1)

portions = {}
for row in range(1, sheet_1.nrows):
    key, value = sheet_1.cell(row, 0).value, sheet_1.cell(row, 1).value
    if key not in portions:
        portions[key] = 0
    portions[key] += value / 100


kcal = prots = fats = carbs = 0
for key, value in portions.items():
    kcal += products[key][0] * value
    prots += products[key][1] * value
    fats += products[key][2] * value
    carbs += products[key][3] * value

print(*list(map(int, (kcal, prots, fats, carbs))))  # 4963 203 307 302

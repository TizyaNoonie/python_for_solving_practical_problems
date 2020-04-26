# 2.3 Работа с несколькими листами
# Whoa, I'm a genius!
import xlrd

wb = xlrd.open_workbook("trekking3.xlsx")
sheet_0 = wb.sheet_by_index(0)

products = {}
for row in range(1, sheet_0.nrows):
    key = sheet_0.cell(row, 0).value
    products[key] = []
    for col in range(1, sheet_0.ncols):
        value = sheet_0.cell(row, col).value
        products[key].append(value if value else 0)

sheet_1 = wb.sheet_by_index(1)

quantity_by_day = {}
for row in range(1, sheet_1.nrows):
    day = int(sheet_1.cell(row, 0).value)
    if day not in quantity_by_day:
        quantity_by_day[day] = {}
    food = sheet_1.cell(row, 1).value
    grams = sheet_1.cell(row, 2).value
    if food not in quantity_by_day[day]:
        quantity_by_day[day][food] = 0
    quantity_by_day[day][food] += grams


def count_content(food_name, grams):
    multiplier = grams / 100
    kcal, prots, fats, carbs = products[food_name]
    return list(map(lambda n: n * multiplier, (kcal, prots, fats, carbs)))


for day in sorted(quantity_by_day):
    kcal = prots = fats = carbs = 0
    for food in quantity_by_day[day]:
        a, b, c, d = count_content(food, quantity_by_day[day][food])
        kcal += a
        prots += b
        fats += c
        carbs += d
    print(*list(map(int, (kcal, prots, fats, carbs))))

"""
2405 82 154 172
4963 203 307 302
5219 178 267 502
4873 241 204 537
5278 243 314 367
4451 190 188 497
4806 205 265 386
5738 264 195 720
1766 66 90 171
"""
1
a = 11
b = a + 3
print ("11+3 =", b)

a = int(input("Укажите количество продукта: "))
b = a * 120
print("Общая стоимость", b)

2
a = int(input("Секунды: "))
h = a//3600
m = (a//60)%60
s = a%60
print(f"чч:мм:сс   {h} : {m} : {s}")

3
n = int(input("Введите число n: "))
a = str(n)
b = a + a
c = a + a + a
d = n + int(b) + int(c)
print("Результат:", d)

4
a = int(input("Введите число: "))
b = 0
while a > 0:
    c = a%10
    if c>b: b=c
    a//=10
print("Результат:", b)

5, 6
profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

7
a = int(input("Результат пробежки первого дня в км "))
b = int(input("Общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы придёте к желаемому результату на %.d день" % result_days)
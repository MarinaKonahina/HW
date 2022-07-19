people_number = int(input("Введите количество посетителей: "))
sum = 0
for i in range(1,people_number+1):
    age = int(input("Введите возраст посетителя " + str(i) + ":"))
    if 18 <= age <= 25:
        sum += 990
    elif age > 25:
        sum += 1390
print("Сумма вашего заказа: " + str(sum))
if people_number > 3:
    sum -= sum/100*10
    print("Сумма вашего заказа с учетом скидки: " + str(int(sum)))

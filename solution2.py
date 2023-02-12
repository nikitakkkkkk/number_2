tickets_count = int(input('Введите количество билетов \n'))
visitors_age = [int(input('Введите возраст посетителя \n')) for i in range(tickets_count)] # То есть программа будет запрашивать ввода возраста поситителей такое количество раз, сколько указано билетов
cost = 0
for x in visitors_age:
    if x < 18:
        cost += 0
    if 18 <= x < 25:
        cost += 990
    if x >= 25:
        cost += 1390

if tickets_count > 3:
    cost = cost - cost * 0.1
    print('Итоговая цена с учётом скидки:\n',cost)
else:
    print('Итоговая цена:\n',cost)


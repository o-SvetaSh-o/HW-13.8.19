n = int(input('Введите количество билетов: ')) # задаем переменную n - количество билетов на мероприятие (целое число)
list_ages = [] # создаем список, в котором будет храниться возраст для каждого участника (пока еще пустой)

for i in range(n):
    ages = int(input('Введите возраст посетителя: ')) # для каждого билета запрашивается возраст
    list_ages.append(ages) # заполняем список n_ages числами, которые вводит пользователь

# согласно условиям задачи, выбираем стоимость билета
    def prise(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

    all_prise = sum(map(prise, list_ages)) # считаем стоимость всех билетов

# согласно условиям, расчитываем скидку и печатаем итоговую сумму
    if n > 3:
        print(f"Сумма к оплате: {all_prise * 0.9} рублей")
    else:
        print(f"Сумма к оплате: {all_prise} рублей")
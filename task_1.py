# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
import time

print("Вариант 1: Решение с помощью списков. ")
time.sleep(1)
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input("Введите номер месяца: "))
if month == 1 or month == 2 or month == 12:
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
else:
    print("Такого месяца нет.")

time.sleep(2)

print("Вариант 2: Решение с помощью словарей. ")
time.sleep(1)
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите номер месяца: "))
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
else:
    print("Такого месяца не существует. ")

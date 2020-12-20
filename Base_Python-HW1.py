"""
# 1) Поработайте с переменными
name = input("Введите имя: ")
print(name)

num = int(input("Введите число: "))
print(num)
"""

# 2) Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс
time = int(input("Введите время в секундах: "))
# hours =  time // 3600
# min = (time % 3600) // 60
# sec = time % 60
# print(f"Московское время {hours}:{min}:{sec}")
print(f"Московское время {time // 3600:02}:{(time % 3600) // 60:02}:{time % 60:02}")

"""
# 3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#    Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number = int(input("Введите число: "))
number_t = str(number)
n1 = number_t + number_t
n2 = number_t + number_t + number_t
summ = number + int(n1) + int(n2)
print("Результат равен:", summ)
"""
"""
# 4) Найдите самую большую цифру в числе. 
numSep = int(input("Введите число: "))
sep = numSep % 10
numSep = numSep // 10
while numSep > 0:
    if numSep % 10 > sep:
        sep = numSep % 10
    numSep = numSep // 10
print(sep)
"""
"""
# 5) Расчет выручки и издержек фирмы.
rev  =  int(input("Введите выручку фирмы в руб.: "))
cost =  int(input("Введите издержки фирмы в руб.: "))

if rev > cost:
    print("Олично! Компания работает с прибылью.")
    print(f"Прибыль компании = {rev - cost} руб.")
    staff = int(input("Введите количество сотрудников фирмы и узнаем сколько прибыли получится на одного человека: "))
    print(f"На каждого сотрудника приходится {(rev - cost) / staff} руб. прибыли")
elif rev == cost:
    print("Компания работат в ноль.")
else:
    print("Компания работат в минус(((")
"""
"""
# 6) Определить номер дня, на который общий результат спортсмена составить не менее b километров.

firstRes = int(input("Введите результат первого дня  в км.: "))
targetRes = int(input("Введите результат в км. к которому стремитесь: "))
procRes =  int(input("Введите значение в % на которое хотите ежедневно увеличивать нагрузку: "))
count = 1

print(f"Результат {count} дня: {firstRes:.2f} км")

while firstRes < targetRes:
    firstRes = firstRes + (firstRes / 100 * procRes)
    count += 1
    print(f"Результат {count} дня: {firstRes:.2f} км")

print(f"На {count}-й день вы достигните запланированного результата — не менее {targetRes} км. ")
"""
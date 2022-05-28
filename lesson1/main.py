# -- задача 1
# не python а "питон"
печатай = print
число = int
ввод = input

печатай("IT'S ALIIIIVE !!!")
какое_то_число = число(ввод("возраст:"))
какое_то_число += 1
печатай("просто прибавил 1: ", какое_то_число)

print = печатай
int = число
input = ввод


# теперь на python
# -- задача 2
input_seconds = int(input("секунды:"))
hours = int(input_seconds / 60) // 60
minutes = int((input_seconds / 60) % 60)
seconds = int(input_seconds - ((minutes * 60) + (hours * 60 * 60)))
print(f"{hours}:{minutes}:{seconds}")


# -- задача 3
n = input('n:')
result = 0
for i in range(1, int(n)+1):
    result += int(n * i)
print('result', result)


#  -- задача 4
num = 444484444
max_num = 0
while num > 0:
    last = num % 10
    num = num // 10

    if last > max_num:
        max_num = last

print('самое большое число:', max_num)


#  -- задача 5 - 6
profit = float(input("выручка:"))
costs = float(input("издержки:"))

if profit > costs:
    real_profit = profit - costs
    print(f"вау мы в плюсе на {real_profit}")
    count_of_workers = int(input('количество сотрудников:'))
    print('рентабельность (прибыль в расчёте на одного сотрудника) :', real_profit / count_of_workers)
elif profit == costs:
    print('денег нет но держатся можно... наверное')
else:
    print('инициализация базы данных ...')
    print('обработка данных         ...')
    print('очень сложные расчёты    ...')
    print('результат: нам п****')


#  -- задача 7
a = int(input('a:'))
b = int(input('b:'))

day = 1
distance = a
while a < b:
    a *= 1.1
    day += 1
    print(f"{day}-й день: {round(a, 2)}")

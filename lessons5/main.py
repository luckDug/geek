# 1

with open('1.txt', 'w') as f:
    while True:
        user_input = input(':')
        if user_input == '':
            break
        f.write(user_input + '\n')

# 2

with open('2.txt', 'r') as f:
    lines = f.readlines()
    print('количество строк:', len(lines))

    for i, line in enumerate(lines):
        count_words_line = len(line.split())
        print(f'номер строки {i + 1}, слов в строке {count_words_line}')

# 3

with open('3.txt', 'r') as f:
    for line in f.readlines():
        surname, salary = line.split()
        if float(salary) < 20000:
            print(surname, salary)

# 4

translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре'
}

first_file = open('4.txt', 'r')
new_file = open('4_new.txt', 'w')

for i in first_file.readlines():
    line_list = i.split()
    line_list[0] = translate[line_list[0].lower()]
    new_file.write(' '.join(line_list) + '\n')

first_file.close()
new_file.close()

# 5

from random import randint

with open('5.txt', 'w') as f:
    result = [str(randint(0, 4000)) for _ in range(randint(200, 400))]
    f.write(' '.join(result))

with open('5.txt', 'r') as f:
    print(sum(map(int, f.read().split())))

# 6

import re

lectures = {}
practice = {}
lab = {}

with open('6.txt', 'r') as f:

    types = {
        '(л)': lectures,
        '(пр)': practice,
        '(лаб)': lab
    }

    for line in f.readlines():
        name = line.split()[0]

        for word in line.split()[1:]:
            value, type_of_value = re.search(r'\w+', word).group(0), re.search(r'\D+', word).group(0)
            types[type_of_value][name] = value

print(lectures)
print(practice)
print(lab)

# 7

import json

profits = [{}]

with open('7.txt', 'r') as f, open('7_result.json', 'w') as r:
	for line in f.readlines():
		firm, forn, revenue, costs = line.split()
		profit = float(revenue) - float(costs)
		profits[0][firm] = profit
	
	profits.append({'average_profit': sum([x for x in profits[0].values()])})
	r.write(json.dumps(profits))

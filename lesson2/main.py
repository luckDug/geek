# 1

types = [1, 1.1, '123', [], {}, (), None]
for value in types:
  print(type(value))

# 2

values = input('enter values (separate by spaces):').split()
count = 0
while count < len(values) - 1:
    values[count], values[count + 1] = values[count + 1], values[count]
    count += 2
print(values)

# 3

month = input('month:')
months = [
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december'
]

number_of_month = int(month) - 1
print(months[number_of_month])

months = {
    '1': 'january',
    '2': 'february',
    '3': 'march',
    '4': 'april',
    '5': 'may',
    '6': 'june',
    '7': 'july',
    '8': 'august',
    '9': 'september',
    '10': 'october',
    '11': 'november',
    '12': 'december'
}
print(months[month])

# 4

words = input(':').split()
for number, value in enumerate(words):
    print(number, value[:10])

# 5

rating = []
index = 0

while True:
    value = input(':')
    if value == 'exit':
        break

    number = int(value)
    rating.insert(0, number)
    index = 0

    while index < len(rating) - 1:
        if rating[index] < rating[index + 1]:
            rating[index], rating[index + 1] = rating[index + 1], rating[index]
        index += 1
    print(rating)

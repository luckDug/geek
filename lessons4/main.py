import sys
from functools import reduce
from itertools import cycle, count

# 1
earnings_per_hour = float(sys.argv[1])
rate_per_hour = float(sys.argv[2])
premium = float(sys.argv[3])
print((earnings_per_hour * rate_per_hour) + premium)

# 2

li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [current for previous, current in zip(li, li[1:]) if current > previous]
print(result)

# 3

result = [x for x in range(20, 241) if x % 21 == 0]
print(result)

# 4

li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [v for v in li if li.count(v) == 1]
print(result)

# 5

result = reduce(lambda a, b: a + b, [i for i in range(100, 1001) if i % 2 == 0])
print(result)

# 6

start = int(input('start:'))
end = int(input('end:'))

assert start >= end

for i in count(start):
    print(i)
    if i == end:
        break

li = [1, 2, 3, 4, 5]

for i in cycle(li):
    print(i)
    stop = input('stop:')
    if stop == 'yes':
        break
# 7

def fact(n):
    result = 1
    if n == 1 or n == 0:
        yield 1
    else:
        for i in range(1, n + 1):
            result *= i
            yield result

for el in fact(9):
    print(el)

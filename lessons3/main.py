# 1

def division(a, b):
  if 0 in (a, b):
      return None
  return a / b

a = input('a:')
b = input('b:')
print('division:', division(float(a), float(b)))

# 2

def profile(name, surname, yaer, city, email, phone):
  print(
      f'name:{name}\n'
      f'surname:{surname}\n'
      f'yaer:{yaer}\n'
      f'city:{city}\n'
      f'email:{email}\n'
      f'phone:{phone}\n'
  )

profile(
  name=input('name:'),
  surname=input('surname:'),
  yaer=input('yaer:'),
  city=input('city:'),
  email=input('email:'),
  phone=input('phone:'),
)

# 3

def my_func(a, b, c):
  numbers = [a, b, c]
  numbers.sort()
  return sum(numbers[1:])

print(my_func(1, 9, 9))

# 4

def degree(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    return x ** y

def degree(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x

    result = x
    for _ in range(1, y):
        result *= x
    return result


print(degree(10, 4))

# 5

def some_sum(*args):
    number = 0
    for i in args:
        number += i
    return number

def is_number(value):
    try:
        int(value)
        return True
    except Exception as e:
        return False

def check_for_next(*args):
    for i in args:
        if not is_number(i):
            return False
    return True

def get_numbers_from_str(string):
    return map(lambda x: int(x) if is_number(x) else 0, string.split())

resutlt = 0
while True:
    input_strs = input('enter_numbers:')
    numbers = get_numbers_from_str(input_strs)
    resutlt += some_sum(*numbers)
    print(resutlt)
    if not check_for_next(*input_strs.split()):
        break

# 6

def int_func(string):
    res = []
    for i in string.split():
        res.append(i[:1].upper() + i[1:])
    return ' '.join(res)

# 7

int_func(input('some text:'))

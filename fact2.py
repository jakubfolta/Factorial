def factor(num):
  if num == 0:
    return 1
  else:
    tot = 1
    while num > 0:
      tot = tot * num  
      num = num - 1
    return tot

print(factor(5))

def factorial(number):
  if number == 0:
    return 1
  else:
    digit = 1
    while number > 0:
      digit = digit * number
      number = number - 1
    return digit

print(factorial(7))

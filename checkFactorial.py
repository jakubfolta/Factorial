def checkFactor(number):
  if number == 0:
    return 1
  else:
    total = 1
    while number > 0:
      total = total * number  
      number = number - 1
    return total

print(checkFactor(9))

def checkFactorial(number):
  if number == 0:
    return 1
  else:
    digit = 1
    while number > 0:
      digit = digit * number
      number = number - 1
    return digit

print(checkFactorial(15))


def checkFactorial(number):
  factorial = 1
  while number > 1:
    factorial = factorial * number
    number = number - 1
  return factorial

print(checkFactorial(3))

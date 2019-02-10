def factorial(number):
  if number == 0:
    return 1
  else:
    otnum = 1
    while number > 0:
      otnum = otnum * number
      number = number - 1
    return otnum


print (factorial(9))

def checkFactorial(number):
    if number == 0:
        return 1
    total = 1
    while number > 1:
        total = total * number
        number -= 1
    return total


print(checkFactorial(5))


def calculateFactorial(number):
  if number == 0:
    return 1
  factorialFromNumber = 1
  while number > 1:
    factorialFromNumber = factorialFromNumber * number
    number -= 1
  return factorialFromNumber

print(calculateFactorial(8))
    

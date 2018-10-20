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

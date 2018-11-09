def factorial(number):
  totalMultiplying = 1
  while number > 0:
    totalMultiplying = totalMultiplying * number
    number = number - 1
  return totalMultiplying

print(factorial(5))

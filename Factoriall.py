def fact(number):
  if number == 0:
    return 1
  else:
    total = 1
    while number > 0:
      total = total * number
      number = number - 1
    return total

print(fact(6))

def factorial(n): #Define function which count factorial
  if n == 0: #Check if number is 0 than print factorial from 0 which is 1
    return 1
  else: 
    dig = 1 #Set variable to 1
    while n > 0: #Set loop active until n is greater than 0
      dig = dig * n #Set first digit of expression which will be the number itself, from second loop multiplication will happen here
      n = n - 1 #Decrease number and at the same time setting second number for multiplication 
    return dig #Return multiplication

print (factorial(4)) #Print factorial to the console



def count_factorial(number):
  total = 1
  if  number == 0:
    return 1
  while number > 1:
    total = total * number
    number -= 1
  return total

print(count_factorial(3))

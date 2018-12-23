def factorial(number):
    if number == 0:
        return 1
    else:
        totalFactorial = 1
        while number > 1:
            totalFactorial = totalFactorial * number
            number = number - 1
        return totalFactorial

print(factorial(4))
    

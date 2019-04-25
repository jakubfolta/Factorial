def factorial(digit):
    total = 1
    while digit >= 1:
        total = total * digit
        digit -= 1
    return total

print(factorial(3))

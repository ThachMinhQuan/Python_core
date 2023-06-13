from unittest import result


def factorial(n):
    if (n > 1):
        return n * factorial(n - 1)
    else:
        return 1

n = int(input(" nhập vào số nguyên dương : "))
while (n <= 0):
    n = int(input(" nhập vào số nguyên dương : "))
result = factorial(n)
print(" Factorial n : " , result)



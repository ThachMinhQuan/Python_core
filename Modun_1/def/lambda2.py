def power(n):
    return lambda a : a ** n
base = power(2)
print("8 pow 2" , base(8))
base = 5
print("8 pow 5" , base(8))
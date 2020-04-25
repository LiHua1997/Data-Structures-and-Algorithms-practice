from math import sqrt
n = int(input("Please input number:"))
for i in range(2, int(sqrt(n))):
    if n % i == 0:
        print("{n} is NOT a prime number.")
        break
else:
        print("{n} is a prime number.")
    

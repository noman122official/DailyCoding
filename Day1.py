'''
QUESTION : Given a number N, print all numbers in the range from 1 to N having
exactly 3 divisors.
'''
import math

def isPrime(num):
    if num == 2:
        return True
    else:
        for i in range(2,num):
               if (num % i) == 0:
                   return False
                   break
               else :
                   return True

def isPerfectSquare(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False

n = int(input("Enter a number"))
count = 0
for i in range(2,n+1):
    if (isPerfectSquare(i) == True):
        y = int(i**0.5)
        if (isPrime(y) == True):
            count = count + 1


print(count)

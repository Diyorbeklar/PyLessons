import os
import math
"""
a = int(input(">>>"))
if a%5==0 and a%3==0:
    print("FIZZBUZZ")
elif a%5==0:
    print("FIZZ")
elif a%3==0:
    print("BUZZ")
else :
    print("FIZZBUZZ Emas")

"""
"""
a = int(input(">>>"))
b = int(input(">>>"))
c = int(input(">>>"))
if a>b and a>c:
    print(a)
elif b>c: 
    print(b)
else: 
    print(c)
"""

"""
a = int(input(">>>"))
i = int()

while a>=i:
    print("* "*i)
    i+=1
"""
"""
a = input(">>> ")
i = int()
k = int()
j = int()
while i < len(a):

    b = a[i]
    i += 1
    if b.isdigit():
        k += 1
    elif b.isalpha():
        j += 1

print("Harflar soni", k)
print("Sonlar  soni", j)

"""
"""
a = int(input(">>> "))
b = int()
c = int(1)
i = int()
while a>i:
    print(c)
    b, c = c, c + b
    i+=1
    

"""

"""
a = int(input(">>> "))
i = int(1)
count = int()
while a > i:
    if a % i == 0:
        count += 1
    i += 1
if count == 1:
    print("TUB")
else: 
    print("tub emas")    
"""
"""

a = int(input(">>> "))
sum = int()

while a != 0:
     
    sum += math.factorial((a % 10))
    a //= 10

print(sum)
"""

"""
a = int(input(">>> "))
sum = int()

while a != 0:
     
    sum += ((a % 10)**3)
    a //= 10

print(sum)

"""
"""
a = int(input(">>> "))
sum = int()

while a != 0:
     
    sum += ((a % 10)**2)
    a //= 10

print(sum)
"""
"""
a = int(input(">>> "))
sum=int(0)
b =a
while a!=0:
     sum = sum*10
     sum += (a % 10) 
     a //= 10

print(sum+b)
"""





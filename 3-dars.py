import os
import random
"""
sum = int()
a = [22,234,2333,234,234,"ASDS","AASD",True,False,4.3]
b = []
for i in a:
    if isinstance(i,int):
        sum+=i
        b.append(i)
print( min(b), max(b) , sum)    
"""
"""
abs = []
natija = []

for i in range(int(input(">>>  "))):
    abs.append(random.randint(1,10))
print(abs)

for i in abs:
    abs.split(i)
    for j in abs:
        abs.extend(j)
    natija.append(i)

print(natija)
"""
lst = [1,2,3,2,1,3,3,3,4]
for i in lst:
    for j in range(lst.count(i)-1):
        lst.remove(i)
          
print(lst)

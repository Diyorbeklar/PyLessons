import os
import random
# -------------------------------------------------------1----------------------------------------------------------
"""
sum = int()
for i in range(1, int(input(">>> "))+1):
    sum += (i**i)
print(sum)
"""
# -------------------------------------------------------2----------------------------------------------------------
"""
n = int(input(">>> Yoshingizni kiriting: "))
for i in range(200):
    if i==n:
        print(i,"=> Bu sizning yoshingiz")
    else:
        print(i)    
"""
# -------------------------------------------------------3----------------------------------------------------------
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("N sonini kiriting: "))

print(f"Tub sonlar {n} gacha: ")
for i in range(2, n + 1):
    if is_prime(i):
        print(i, end=" ")
"""
# -------------------------------------------------------3----------------------------------------------------------
"""
for i in range(100,1000):
       a = i%10
       b = ((i//10)%10)
       c = i//100
       if ((a == b and a!=c) or (a==c and a!=b) or (b==c and a!=c)) :
              print(i)
"""
#---------------------------------------------------------5------------------------------------------------------------------
"""
n = int(input(">>> Sonni kiriting: "))
son = random.randint(1,n)
count= int()
print(son)
while count<3:
    count+=1
    if(int(input("Qaysi son:")) == son):
        print("Winner")
        break;
    else : print("Looser")

"""

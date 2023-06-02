import os
import random
"""
pi=3.14
print("Aylanani maydoni:",2*pi*int(input(">>>  "))," sm")
"""
"""
a =input(">>> ")
print(len(a)*a)
"""
"""
s="Foundation"
print(s[:len(s)//2-1:-1])
print(s[len(s)//2-1::-1])
"""
"""
a=int(input(">>> "))
for i in range(1,11):
    print(f"{a} * {i} = ",a * i)
"""
"""
a=input(">>> ")
a = a[len(a)-1] + a[1:len(a)-1:] + a[0]
print(a)
"""
"""
n = int(input(">>> "))
for i in range(1,n+1):
    print(i*" * ")
"""
"""
raqam = int()
harf = int()
soz = input(">>> ")
for i in soz:
    if i.isalpha():
        harf+=1
    if i.isdigit():
        raqam+=1
print("Raqam => ",raqam)
print("Harf => ",harf)  
"""
"""
a, b = 0, 1
for i in range(int(input(">>> "))):
        print(b)
        a, b = b, a + b
"""
"""
j = int(input(">>> "))
k = int()
for i in range(2,j):
    if j%i == 0:
        k+=1
if k==0:
    print("Tub son")
else:
    print("Tub son emas")
"""
"""
raqam = input(">>> ")
print(f"{raqam} + {raqam[::-1]} =",int(raqam)+int(raqam[::-1]))
"""
"""
gap = input(">>> ")
n = int(input(">>> "))

truncated_gap = gap[:n-1] + gap[n:]
gap = truncated_gap
print(gap)
"""
"""
sum = int()
for i in range(1,int(input(">>> "))+1):
    sum += i**i
print(sum)
"""
"""
yosh = int(input(">>> "))
for i in range(1,201):
    if i == yosh:
        print(i," => Bu sizni yoshingiz") 
    else:
        print(i) 
"""
"""
for i in  range(99,1000):
    a = i%10
    c = i//100
    b = i//10 - c*10
    if (a == b and a!=c) or (a == c and a!=b) or (b == c and a!=c):
        print(i)
"""
"""
m = random.randint(1,10)
i = int()
while (i<3):
   n = int(input(">>> "))
   if i<3 and m==n:
    print("Winner")
    break
   i+=1
if i==3 and m!=n:
  print("Looser")
"""
"""
a = [[1,2],[3,5],[4,1,2,0],[1,5,6,7]]
print(max(a,key=lambda x: sum(x)))
"""
"""
a = ["alik","salom","Hamma","Garang","asdasdasdasd"]
print(max(a,key=len))
"""
"""
a = [[],[1,2,3,4],[],[2,3,4,6,7],[],[3,2,1,0],[]]
for i in range(a.count([])):
    a.remove([])
print(a)
"""
"""
a = ["a","b","s","a"]
a = [str("".join(a))]
print(a)
"""
"""
lst = [[1,4,6],[9,4,5],[6,5,2]]
lst = sorted(lst, key=lambda x: sum(x))
print(lst)
"""
"""
lst = sorted(lst,key=lambda x: x[1])
print(lst)
"""
"""
lst = [[1,8,6],[9,4,5],[6,5,2]] 
for i in range(len(lst)):
    lst[i] = sorted(lst[i])
print(lst)
"""
"""
n = input(">>> Sotib olmoqchi bo'lgan telefoniz: ")
lst = [ ["Iphone",1200,"13PRO"],["Samsung",1000,"S10 Note"],["Honor",1100,"X"]]
for i in range(len(lst)):
    if lst[i][0] == n:
       lst.remove(lst[i])
print(lst)
"""
"""
lst1 = [1,2,3,4]
lst2 = [3,4,5,6]
lst3 = []
lst3.extend(lst1)
lst3.extend(lst2)
print(list(set(lst3)))
"""
"""
lst = [[1,2,3,4,5,6,7],["a","b","c","d","j","k","m"]]
lst2 = []
for i in range(len(lst[0])):
     lst2.append([lst[0][i],lst[1][i]])
print(lst2)
"""
"""
lst = [ ["Iphone",1200,"13PRO"],["Samsung",1000,"S10 Note"],["Honor",1100,"X"]]
for i in range(len(lst)):
     lst[i][1] = lst[0][1] * 1.25
print(lst)
"""

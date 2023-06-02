import os

"""
def karra(n : int):
    for i in range(1,11):
        print(f"{n} * {i} = ",n*i)

karra(int(input(">>> ")))
"""
"""
d1 = {"a":100,"b":200,"c":300}
d2 = {"a":300,"b":200,"d":400}
d3 = dict()
def con(x1,x2,x3):
    for i in {*x1,*x2}:
       if x1.get(i) != None and x2.get(i) != None:
           x3[i] = x1.get(i) + x2.get(i)
       elif x1.get(i) != None:
           x3[i] = x1.get(i)
       elif x2.get(i) != None:
            x3[i] = x2.get(i)       
    return x3

print(con(d1,d2,d3))
"""
"""
n = input(">>>")
dic = dict()
for i in n:
    dic[i] = 0
for i in n:
    dic[i] +=1
print(dic)
"""
"""
def tesrkari_son(n: int):
    n = str(n)
    return int(n[::-1])

print(tesrkari_son(123456))
      
"""
"""
def polidrom(n: int):
    n = str(n)
    return int(n[::-1]) == int(n)

print(polidrom(123456))
"""
"""
def Uzgargan_son(k :int, n:int):
    n = str(n)
    k = str(k)
    n = k + n
    return int(n)

print(Uzgargan_son(4,32423))
"""
gap = input(">>> ")
def soz(qator):
    a = input(">>> ")
    b = input(">>> ")
    c = input(">>> ")
    for i in range(len(qator)):
        for j in a:
           if gap[i] == j:
               gap[i] = '*'
        for k in a:
           if gap[i] == k:
               gap[i] = '*'
        for m in a:
           if gap[i] == m:
               gap[i] = '*'
    return qator
print(soz(gap))


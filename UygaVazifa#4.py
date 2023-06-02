import os
#------------------------------------------------------1-masala----------------------------------------------------
"""
a = [(1,2),(3,5),(5,6),(6,8)]
for i in range(len(a)):
    a[i] = list(a[i])
print(a)
"""
#-----------------------------------------------------2-masala----------------------------------------------------
"""
list = [1,2]
lst2 = []
n = int(input(">>> "))
for i in range(n):
    lst2.extend(list)
list = lst2
print(list)

"""
#-------------------------------------------------------3-masala----------------------------------------------------
"""

lst = [1, 3, 4, 9, 3, 4, 0, -1, 7, 8]
umumiy = []
alohida = []

for i, v in enumerate(lst):
    if i > 0 and v < lst[i-1]:
        if len(alohida)>1:
            umumiy.append(alohida)
        alohida = []
    alohida.append(v)

umumiy.append(alohida)
for i in umumiy:
    print("\"",*i,"\"")
"""
"""
lst = [1, 3, 4, 9, 3, 4, 0, -1, 7, 8]

for i in range(1,len(lst)):

    if (lst[i-1] > lst[i] and lst[i] > lst[i+1] ) :
        pass
    elif lst[i] < lst[i-1]:
        print(lst[i-1])
    else:
        print(lst[i-1],end=" ")
    if len(lst) == i + 1:
        print(lst[i],end=" ")
"""
"""
input:
lst = [1,4,3,9]
"RM"
output:
["RM1","RM4","RM3","RM9"]
"""
"""
lst = [1, 4, 3, 9]
output = ["RM" + str(num) for num in lst]
print(output)
"""
"""
lst = [1,2,3,4,5]
lst2 = list()
yig = int()
for i in range(min(lst),max(lst)+1):
    if i not in lst:
        lst2 += f"{i}"
        yig += i

if yig == 0:
    print(0)
else :
    print("+".join(tuple(lst2)),f" = {yig}")
"""
"""
gap = "W3resoirse"
dct = dict()
for i in gap:
    dct[i] = 0
for i in gap:
    dct[i] +=1
print(dct)
"""
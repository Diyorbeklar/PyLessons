import os
#-----------------------------------------------------------1-masala--------------------------------------------------
"""
a = [[1,2],[0,0,2],[7,0],[2,3]]
print(max(max(a)))
print(max(a))
"""
#----------------------------------------------------------2-masala----------------------------------------------------
"""
a = ["alik", "kim", "it", "web", "arsenal", "uzb"]

maxWord = ""
maxLen = 0

for sen in a:
    for word in sen.split():
        if len(word) > maxLen:
            maxLen = len(word)
            maxWord = word

print(maxWord)


"""
#----------------------------------------------------------3-masala------------------------------------------------------
"""
a = [[],[1,2,3],[],[1,2,3,4,5],[]]
for i in a:
      for j in range(a.count([])):
            a.remove([])

"""
#-----------------------------------------------------------4-masala------------------------------------------------------
"""
a = ["J", "A", "V", "A"]
string_a = "".join(a)
print(string_a)
"""
#------------------------------------------------------------5-masala---------------------------------------------------
"""
arr1 = [1,2,True,"Hikmat","Abbos"]
arr2 = ["RAED",32,4,False,"Gani"]
arr3 = []
for i in arr1:
    arr3.append(i)
for i in arr2:
    arr3.append(i)
print(arr3)
"""
"""
a = [1,4,3,9]
b = "RM"
for i in range(len(a)):
     a[i] = f"RM{a[i]}"
print(a)
"""
"""
lst = [2,3,4,5,6,7,8,9,1,2,3,4,5,6,]

for i in lst:
    for j in range(lst.count(i)-1):
        lst.remove(i)
print(lst)
"""
"""
str1 = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
str2 = input(">>> ")
#str2 = ",".join( str2)
for i in str1:
    for j in str2:
        if i==j:
            str1.remove(j) 

print(str1)
"""
"""
tpf = 1,2,3,4,5,6,8,7
print(sum(tpf))

print(max(tpf)-min(tpf))

tpf = list(tpf)
tpf.remove(max(tpf))
tpf = tuple(tpf)
print(tpf)
"""
"""
tpf = "HASAN","DIYORBEK","AHMOQONA","AFRIKA","JAMO"
gap = list()
for i in tpf:
    if len(i)>=5:
        gap.append(i)


print(gap)
"""
"""
tpf = [(1,3),(1,4,0),(2,3,4),(1,0,0,4)]
tpf = [sum(i) for i in tpf]
print(tpf)
"""
"""
tpf = [(1,2,3),(2,2),(0,0,3)]
tpf.sort(key= lambda x: sum(x))
print(tpf)
"""
"""
tpf = [(1,2),(2,2),(0,3)]
und = list()
ind = list()
list = list()
for i in tpf:
     und.append(i[0])
for i in tpf:
     ind.append(i[1])
list = tuple(und),tuple(ind)
print(list)
"""

list = [[1,2,3],[4,5,6],[9,27],[2,0,10],[1,0],[1],[2,2,2]]

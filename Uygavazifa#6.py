import os
#-----------------------------------------------------1-masala---------------------------------------------------------
"""
lst1=['S001','S002','S003','S004']
lst2=['Adina Park','Leyton Marsh','Duncan Boyle','Saim Richards']
lst3=[85,95,84,75]

def threeToOne(list1 :list,list2 :list,list3 :list):
    dct = dict()
    for i in range(len(list1)):
        dct[list1[i]] = dict([(list2[i],list3[i])])
    return dct
print(threeToOne(lst1,lst2,lst3))
"""
#-----------------------------------------------------2-masala---------------------------------------------------------
"""
dct1 = {1:"ABC",2:"DEF",3:"GHI",4:"JKL",5:"MNO"}
def juftToq(diction:dict):
    c = str()
    for i in diction:
        if i%2==0:
            c = diction[i]
            diction[i] = diction[i-1]
            diction[i-1] = c
    return diction


print(juftToq(dct1))
"""
#-----------------------------------------------------3-masala---------------------------------------------------------
"""
def gapToword(gap :str):
    return f"word:{gap.split()}\nsentence:{gap.split('.')}"
print(gapToword(input(">>> ")))

"""

#-----------------------------------------------------4-masala---------------------------------------------------------
"""
lst1 = [1,2,3]
def toOne(list1:list):
    str1=str()
    lst1.sort(key=lambda x: int(str(x)[0]) if x > 9 else x,reverse=True)
    for i in lst1:
         str1+=str(i)
    return str1
print(toOne(lst1))
"""
#-----------------------------------------------------5-masala---------------------------------------------------------
"""
lst = [[1,"Jean Castro","V"],[2,"Lula Powell","V"],[3,"Brian Howell","VI"],[4,"Lynne Foster","VI"],[5,"Zachary Simon","VII"]]

def toDCT(lst1 :list):
    dct = dict()
    for i in lst1:
        dct[i[0]]=[i[1],i[2]]
    return dct
print(toDCT(lst))
"""
#-----------------------------------------------------6-masala---------------------------------------------------------
"""
lst = [123,234,432,231,345,324]
def toOne(lst1:list):
    for i in lst1:
       if int(str(i)[0])%2==0:
           print(i,end=" ")

toOne(lst)

"""
"""
tpl = (4,3,2,2,-1,18)
def toSum(tpl1):
    sum1=1
    for i in tpl1:
       sum1*=i
    return sum1
print(toSum(tpl))
"""
"""
lst = [(),(1,2),(1,2,3),(12)]
def todeleteTpl(list1:list):
    for i in range(list1.count(())):
        list1.remove(())
    return list1
print(todeleteTpl(lst))
"""
"""
lst = [1,23,45,"WER","EWrwe","EWrwer",32]
def toFindUp(lst1:list):
     return max([i for i in lst if isinstance(i , int)])
print(toFindUp(lst))

"""
"""
keys = ["Ten","Twenty","Thirty"]
values = [10,20,30]
def ConvertToDCT(key:list,value:list):
    dct = dict()
    for i in range(len(key)):
        dct[key[i]] = value[i]
    return dct
print(ConvertToDCT(keys,values))

"""
"""
dct1 = {"Ten":10,"Twenty":20,"Thirty":30}
dct2 = {"Thirty":30,"Fourty":40,"Fifty":50}
def TwoToOne(dict1:dict,dict2:dict):
    dict1 = {**dict1,**dict2}
    return dict1
print(TwoToOne(dct1,dct2))
"""
"""
sampleDict = {
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
}

def toLoca(samp:dict):
    samp["location"] = samp.pop("city")
    return samp
print(toLoca(sampleDict))
"""
"""
sampleDict = {
    "Physics":82,
    "Math":65,
    "History":75
}
def toFindMin(samp:dict):
    for i in samp.keys():
       if samp[i] == min(samp.values()):
           print(i)

toFindMin(sampleDict)
"""

"""
a = {"a":100,"b":200,"c":300}
def toSumDict(dct:dict):
    print(sum(dct.values()))
toSumDict(a)
"""
"""

def int_to_str(num):
   if isinstance(num,int):
        return f"\'{str(num)}\'"
   else:
        return f"\'{str(num)}\'"

def str_to_int(num:str):
    if isinstance(num,int):
        return num
    else:
        return int(num)

print(int_to_str("4"))
"""
"""
gap = "SAlom Dunyo yaxshimisan sadad asd asd wQWEEQwe werew wer w wer wer"
lst = gap.split()
a = input(">>> ")
b = input(">>> ")
c = input(">>> ")

for i,v in enumerate(lst):
    if a==v or b==v or c==v:
        lst[i]=(len(v))*"*"

print(*lst)
"""
"""
a = 87945
a = str(a)
length = len(a)

for i in range(length):
    c = a[0]
    a = a[1:] + c
    print(a)
"""
"""
dct = {1:"YANVAR",2:"FEVRAL",3:"MART",4:"APREL",5:"MAY",6:"IYUL",7:"IYUN",8:"AVGUST",9:"SENTAYBR",10:"OKRABR",11:"NOYABR",12:"DEKABR"}
a = input(">>> ")
b = a.split(".")
print(f"{b[0]}-{dct[int(b[1])]} {b[2]}-yil")
"""
"""
a = input(">>> ")
b =int()
for i in a:
    if int(i)==0:
        b+=1
    else:
        break
print(b)

"""

"""
MORSE1 = {"-----":0,".----":1,"..---":2,"...--":3,"....-":4,".....":5,"-....":6,"--...":7,"---..":8,"----.":9}
a = input(">>> ")
b = a.split()
for i in b:
    print(MORSE1[i], end="")
"""
"""
lst=["A","B","C","E","D","G","F","J","N"]
n = int(input(">>> "))
output = [lst[i:i+n] for i in range(0, len(lst), n)]
print(output)
"""
"""
lst=[1,2,3,4,5,6,1,1,2,3,4,4,5,5,6,6,]
dtr=set(lst)
dct=dict()
for i in dtr:
    dct[i]=lst.count(i)
print(dct)
"""
"""
def is_power_of_two(n: int):
    if n == 1:
        return True
    elif n == 0 or n % 2 != 0:
        return False
    else:
        return is_power_of_two(n // 2)
print(is_power_of_two(6345))
"""
"""
def addDigit(n):
    b=int()
    while n!=0:
       b+=n%10
       n=n//10
    n=b
    if n<=9:
        return n
    return addDigit(n)

print(addDigit(38))
"""
"""
def addDigit(n):
    if n <= 9:
        return n
    return addDigit(sum(int(digit) for digit in str(n)))

print(addDigit(38))
"""




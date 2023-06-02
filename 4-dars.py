import os

"""
dct = {"1":10,"2":20,"3":30,"4":55,"5":25}
maxDCT = max(dct.values())
minDCT = min(dct.values()) 

for k, v in dct.items():
     if maxDCT == v:
        maxDCT = k
     elif minDCT == v:
        minDCT = k  

dct.pop(maxDCT)
dct.pop(minDCT)
print(dct)
"""
"""
dct1 = {1:10,2:20}
dct2 = {3:30,4:40}
dct3 = {9:90,7:70}
dct1.update(dct2)
dct1.update(dct3)
print(dct1)
"""
"""
sum = 0
dct = {"1":10,"2":20,"3":30,"4":55,"5":25}
for k, v in dct.items():
       sum+=v
print(sum)
"""
"""
dct = {"3":10,"1":20,"4":30,"2":55,"6":25}
dctKeys  = list(dct.keys())
dctKeys.sort()
dctSort = {i : dct[i] for i in dctKeys}
print(dctSort)
"""

dct = {"3": 10, "1": 20, "4": 30, "2": 55, "6": 25}
dctSort = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1])}
print(dctSort)


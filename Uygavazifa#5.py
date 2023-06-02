import os

data = [
    {"full_name":"Eugene Elsmor","company":"Kazu","position":"Electrical Engineer","salary":"$4440.86"},
    {"full_name":"Joni Stredder","company":"JumpXS","position":"Environmental Tech","salary":"$870.05"},
    {"full_name":"Terri-jo Fulham","company":"Tagchat","position":"Assistant Media Planner","salary":"$1992.55"},
    {"full_name":"Priscilla Pandya","company":"Youopia","position":"Help Desk Operator","salary":"$3715.95"},
    {"full_name":"Wolfy Swanborough","company":"Topiclounge","position":"Recruiter","salary":"$1045.61"},
    {"full_name":"Raleigh Ratter","company":"Zoozzy","position":"Graphic Designer","salary":"$602.41"},
    {"full_name":"Anastasia Winward","company":"Avaveo","position":"Cost Accountant","salary":"$3641.42"},
    {"full_name":"Dorry Vasyunichev","company":"Fivebridge","position":"Junior Executive","salary":"$2035.05"},
    {"full_name":"Richy Cleft","company":"Jamia","position":"Sales Associate","salary":"$912.98"},
    {"full_name":"Zack Record","company":"Oyonder","position":"Social Worker","salary":"$2492.23"},
    {"full_name":"Lissy Newns","company":"Riffwire","position":"Developer II","salary":"$1177.79"},
    {"full_name":"Audrye Churchyard","company":"Photospace","position":"Environmental Tech","salary":"$4125.83"},
    {"full_name":"Timothy Seligson","company":"Riffpath","position":"Compensation Analyst","salary":"$1271.94"},
    {"full_name":"Brandie Rogeon","company":"Riffpath","position":"Analyst Programmer","salary":"$1911.09"},
    {"full_name":"Dane Rugg","company":"Twimm","position":"Associate Professor","salary":"$2200.72"},
    {"full_name":"Mick Jeduch","company":"Realblab","position":"Executive Secretary","salary":"$1154.20"},
    {"full_name":"Rowland Christofol","company":"Mycat","position":"Senior Cost Accountant","salary":"$1119.94"},
    {"full_name":"Sibella Abrahams","company":"Minyx","position":"Internal Auditor","salary":"$4023.25"},
    {"full_name":"Layne Thomel","company":"Centimia","position":"Research Associate","salary":"$4073.17"},
    {"full_name":"Demetris Clemenzi","company":"Tagopia","position":"Human Resources Manager","salary":"$1530.37"},
    {"full_name":"Kerstin Devon","company":"Katz","position":"Senior Quality Engineer","salary":"$1305.61"},
    {"full_name":"Brandon Burgwyn","company":"Mydeo","position":"Physical Therapy Assistant","salary":"$1325.58"},
    {"full_name":"Dyana Crosby","company":"Riffpath","position":"Payment Adjustment Coordinator","salary":"$1501.54"},
    {"full_name":"Harald Voller","company":"Riffpedia","position":"Accountant I","salary":"$4397.60"},
    {"full_name":"Nollie Phipard-Shears","company":"Aimbo","position":"Legal Assistant","salary":"$3172.57"},
    {"full_name":"Gaynor Dannohl","company":"Riffpath","position":"Administrative Assistant II","salary":"$3035.89"},
    {"full_name":"Tome Bensen","company":"Yamia","position":"Assistant Professor","salary":"$3677.10"},
    {"full_name":"Jessey Anshell","company":"Bubblemix","position":"Registered Nurse","salary":"$2782.66"},
    {"full_name":"Valentijn Melbury","company":"Bluejam","position":"Statistician I","salary":"$1308.43"},
    {"full_name":"Rochelle Andrejevic","company":"Riffpath","position":"VP Product Management","salary":"$1734.61"}
]
# 1 - masala: Human Resources Manager bo'limida nechta odam ishlashini hisoblang
"""
son = int()
for i in data:
    for j in i:
        if i[j] == "Human Resources Manager":
          son+=1
          print(i["full_name"])
print(son,"ta odam ishlaydi")
"""
# 2 - "Riffpath" kompaniyasida ishlaydigan barcha 
# hodimlarga qancha maosh to'lanishini hisoblang 
# (maosh olida $ belgisi bor e'tiborli bo'ling)
"""
summa = float()
for i in data:
    for j in i:
        if i[j] == "Riffpath":
          print(a := i["salary"])
          a = float(a[1:])
          summa += a

print(f"Riffpath ishlaydigonlari ummumiy maoshi: ${summa}")
"""
# 3 - Ismi "K" dan boshlanadigan hodimlarni oyligini 2-karra oshiring
"""
for i in data:
     if i["full_name"][0] == 'K':
          print(i["full_name"],"bu xodimning oylik maoshi ikki karra oshirildi")
          i["salary"] = "$" + str(float(i["salary"][1:])*2)
"""
# 4 - barcha "full_name" keylari ni o'rniga "FIO" ga almashtiring 
# value lar o'chib ketmasin
"""
for i in data:
      i["FIO"] = i.pop("full_name")
      print(i)
"""
# 5 - masala "position" keyning "valuesida" -> "senior" yoki "junior"
# satri bor barcha hodimlarni o'chirib tashlang
"""
for i in data:
      if i["position"][:6] == "Junior" or i["position"][:6] == "Senior":
        print(i)
        i["position"] = i["position"][7:]
        print(i)
"""
# 6 - masala "Assistant" lar soni nechtaligini hisoblang
"""
son = int()
for i in data:
      if i["position"][:9] == "Assistant":
        print(i)
        son+=1
print("Assistantlar soni:",son)
"""
# 7 - masala Barcha "Assistant" larni "Junior" pazitsiyaga o'tqazing
# misol -> "Assistant Professor" -> "Junior Professor"
"""
for i in data:
      if i["position"][:9] == "Assistant":
          print(i)
          i["position"] = "Junior" + i["position"][9:]  
          print(i)
        
"""
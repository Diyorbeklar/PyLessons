import os,random


choiceNum = int(input("""1:Papper\n2:Rock\n3:Scissors\n"""))
dct = {1:"Papper",2:"Rock",3:"Scissors"}
lst = ["Papper","Rock","Scissors"]
randomNum = random.choice(lst)
if dct[choiceNum] == randomNum:
    print("Topdingiz")
else:
    print("Topolmadiz")


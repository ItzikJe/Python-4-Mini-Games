import random

sybols=["@","#","$","%","&","*",]
cell_1=random.choice(sybols)
cell_2=random.choice(sybols)
cell_3=random.choice(sybols)
money=float(input("enter your money to start "))
count=0;
while(money>0):
    print("|", random.choice(sybols),"|", random.choice(sybols),"|", random.choice(sybols),"|")
    print("-----------")
    print("|",cell_1,"|",cell_2,"|",cell_3,"|")
    print("-----------")
    print("|", random.choice(sybols),"|", random.choice(sybols),"|", random.choice(sybols),"|")

    if cell_1==cell_2==cell_3:
        count+=1
        print("you won")
        money+=10
        print("your money ",money)
    else:
        money -= 10
        print("you loose")
        print("your money ",money)

print(count)
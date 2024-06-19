role1 = input()
hp1 = int(input())

role2 = input()
hp2 = int(input())

print(role1, hp1)
print(role2, hp2)

count = 0

while(hp1 > 0 and hp2 > 0):
    print("current round", count)

    if(role1 == "warrior" and role2 == "warrior"):
        hp1 -= 10
        hp2 -= 10
    if(role1 == "warrior" and role2 == "paladin"):
        hp1 -= 5
        hp2 -= 10
        hp2 += 0.1*hp2
    elif(role2 == "warrior" and role1 == "paladin"):
        hp2 -= 5
        hp1 -= 10
        hp1 += 0.1*hp2
    elif(role1 == "warrior" and role2 == "archer"):
        hp1 -= 5
        hp2 -= 10
    elif(role2 == "warrior" and role1 == "archer"):
        hp2 -= 5
        hp1 -= 10
    elif(role1 == "paladin" and role2 == "paladin"):
        hp1 -= 5
        hp2 -= 5
        hp1 += 0.1*hp1
        hp2 += 0.1*hp2
    elif(role1 == "paladin" and role2 == "archer"):
        hp1 -= 5
        hp2 -= 5
        hp1 += 0.1*hp1
    elif(role2 == "paladin" and role1 == "archer"):
        hp2 -= 5
        hp1 -= 5
        hp2 += 0.1*hp2
    elif(role1 == "archer" and role2 == "archer"):
        hp1 -= 5
        hp2 -= 5
    count += 1

    print(hp1, hp2)

if(hp1 > hp2):
    print("yang menang role1 dalam", count, "ronde")
elif(hp2 > hp1):
    print("yang menang role2 dalam", count, "ronde")
else:
    print("seri")



f = open("lmao", "r")

for line in f:
    if(line == b"%PDF-1.3"):
        print("yes")

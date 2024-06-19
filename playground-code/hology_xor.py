s = "3‡0†2?3"

f = open('encrypted', 'r')
s2 = f.read()

#for i in range(len(s)):
#    a = ord(s[i])
#    b = ord(s2[i])
#    print(chr(a^b))

def shift_all(s, i):
    temp = ''
    for x in s:
        temp += (chr(ord(x) + i))
    return temp

for i in range(-40, 100):
    print(shift_all(s, i))

print(s)
print(s2)

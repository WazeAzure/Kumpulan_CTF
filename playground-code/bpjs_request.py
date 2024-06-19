import requests

s = []

for i in range(93):
    r = requests.get(f'http://178.128.112.149/10_medium/?kata_cari={i}', )
    print(r.content)
    temp = (r.content)
    temp = temp.split(b' ')
    print(temp[-1])
    s.append(temp[-1])

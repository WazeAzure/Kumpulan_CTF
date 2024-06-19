import requests
import json

url = 'https://ctf-gemastik.ub.ac.id/api/user'

req = requests.get(url)
res = json.loads(str(req.text))

f = open('daftar_peserta.txt', 'w')

def hi(x):
    f.write(x['username'] + ":" + x['ip'] + '\n')
    return x

res = res['data']

for x in res:
    hi(x)

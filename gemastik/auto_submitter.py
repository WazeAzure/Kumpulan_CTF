import requests
import schedule
import time

def submit():
    url = 'https://ctf-gemastik.ub.ac.id/api/flag'

    YOUR_TOKEN = open('TOKEN', 'r')
    YOUR_TOKEN = YOUR_TOKEN.read().strip('\n')

    header = {
            "Authorization": f"Bearer {YOUR_TOKEN}",
            "Content-Type": "application/json"
            }


    flags = []

    f = open('flags_daftar.txt', 'r')
    for line in f:
        if line != '\n':
            line = line.strip('\n')
            flags.append(line)

    print(flags)
    data = {
            "flags": str(flags)
            }

    print(data)

    submit = requests.post(url, data=data, headers = header)
    res = submit.text
    print(res)
    f.close()


schedule.every(5).minutes.do(submit)
submit()
while True:
    schedule.run_pending()
    time.sleep(1)

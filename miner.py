from hashlib import sha256
from random import choice
from string import ascii_uppercase, digits
import datetime
import os
import http.client
import socket

def getRandomString(n: int):
    return "".join(choice(ascii_uppercase + digits) for _ in range(n)).encode('utf-8')

if __name__ == "__main__":
    difficulty = int(os.environ['difficulty'] if ('difficulty' in os.environ) else 4)
    nodeName = socket.gethostname()
    print("The difficulty is {}".format(difficulty))

    while 1:
        thehash = sha256(getRandomString(25)).hexdigest()

        if thehash[:difficulty] == ('0'*difficulty):
            body =  {
                'node': nodeName,
                'hash': thehash,
                'time': str(datetime.datetime.now()),
                'difficulty': str(difficulty)
            }
            print(body)

            # conn = http.client.HTTPConnection('192.168.2.37:9700')
            # conn.request('POST', '/', str(body).encode())
            # res = conn.getresponse()
            # print(res.status)
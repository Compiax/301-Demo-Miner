from hashlib import sha256
from random import choice
from string import ascii_uppercase, digits
import datetime
import os
import http.client
import socket
import sys

def getRandomString(n: int):
    return "".join(choice(ascii_uppercase + digits) for _ in range(n)).encode('utf-8')

sock = None

def run():
    global sock

    difficulty = int(os.environ['difficulty'] if ('difficulty' in os.environ) else 4)
    nodeName = socket.gethostname()
    print("The difficulty is {}".format(difficulty))
    
    
    while 1:
        string = getRandomString(25)
        thehash = sha256(string).hexdigest()

        if thehash[:difficulty] == ('0'*difficulty):
            body =  {
                'node': nodeName,
                    'key': string.decode('utf-8'),
                'hash': thehash,
                'time': str(datetime.datetime.now()),
                'difficulty': str(difficulty)
            }

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('192.168.2.37', 9700))
            sock.send((str(body) + '\n').encode())
            sock.close()
            print(body)

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("Closed")
        sock.close()
        sys.exit(0)
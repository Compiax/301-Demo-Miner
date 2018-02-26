from hashlib import sha256
from random import choice
from string import ascii_uppercase, digits
import datetime
import os
import http.client
import socket
import sys
import json

def getRandomString(n: int):
    return "".join(choice(ascii_uppercase + digits) for _ in range(n)).encode('utf-8')

sock = None

def hash(string: str):
    return sha256(string).hexdigest()

def run():
    global sock

    difficulty = int(os.environ['difficulty'] if ('difficulty' in os.environ) else 3)
    hostname = str(os.environ['hostname'] if ('hostname' in os.environ) else 'localhost')



    nodeName = socket.gethostname()
    print("The difficulty is {} ".format(difficulty))
    print("Sending output to {}:9700".format(hostname))


    while 1:
        string = getRandomString(25)
        thehash = hash(string)

        if thehash[:difficulty] == ('0'*difficulty):
            body =  {
                'node': nodeName,
                    'key': string.decode('utf-8'),
                'hash': thehash,
                'time': str(datetime.datetime.now()),
                'difficulty': str(difficulty)
            }

            # body = ""

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((hostname, 9700))
            sock.send(json.dumps(body).encode())
            sock.close()
            print(body)

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("Closed")
        sock.close()
        sys.exit(0)

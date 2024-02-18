import docker
import os
import re
import requests
import time


JOIN_RE = re.compile(r'^\[[0-9:]+\] \[Server thread/INFO\]: (?P<player>[A-Za-z0-9_]+) (?P<message>joined the game)$')
LEAVE_RE = re.compile(r'^\[[0-9:]+\] \[Server thread/INFO\]: (?P<player>[A-Za-z0-9_]+) (?P<message>left the game)$')
CHAT_RE = re.compile(r'^\[[0-9:]+\] \[Server thread/INFO\]: (?:\[Not Secure\] )?<(?P<player>[A-Za-z0-9_]+)> (?P<message>.+)$')
ME_RE = re.compile(r'^\[[0-9:]+\] \[Server thread/INFO\]: \* (?P<player>[A-Za-z0-9_]+) (?P<message>.+)$')
ADVANCEMENT_RE = re.compile(r'^\[[0-9:]+\] \[Server thread/INFO\]: (?P<player>[A-Za-z0-9_]+) (?P<message>has made the advancement|has completed the challenge|has reached the goal) \[(?P<advancement>[^]]+)\]$')


if __name__ == '__main__':
    client = docker.from_env()
    while True:
        ctr = client.containers.get(os.environ['CONTAINER_NAME'])
        for entry in ctr.attach(stream=True):
            for line in entry.decode().split('\n'):
                line = line.strip()
                if JOIN_RE.match(line):
                    match = JOIN_RE.match(line)
                    player = match['player']
                    message = '*%s*' % match['message']
                elif LEAVE_RE.match(line):
                    match = LEAVE_RE.match(line)
                    player = match['player']
                    message = '*%s*' % match['message']
                elif CHAT_RE.match(line):
                    match = CHAT_RE.match(line)
                    player = match['player']
                    message = match['message']
                elif ME_RE.match(line):
                    match = ME_RE.match(line)
                    player = match['player']
                    message = '*%s*' % match['message']
                elif ADVANCEMENT_RE.match(line):
                    match = ADVANCEMENT_RE.match(line)
                    player = match['player']
                    message = '*%s* **[%s]**' % (match['message'], match['advancement'])
                else:
                    continue

                requests.post(os.environ['WEBHOOK_URL'], json={
                    'username': player,
                    'avatar_url': 'https://minotar.net/helm/%s/128.png' % player,
                    'content': message
                })

        time.sleep(15)

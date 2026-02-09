import requests
import threading
import sys
from queue import Queue

q = Queue()

def work():
    while not q.empty():
        u = f'{sys.argv[1]}/{q.get()}'
        r = requests.get(u)
        if r.status_code == 200:
            print(f'[+] {u}')
        q.task_done()

[q.put(l.strip()) for l in open(sys.argv[2])]
[threading.Thread(target=work, daemon=True).start() for _ in range(50)]
q.join()

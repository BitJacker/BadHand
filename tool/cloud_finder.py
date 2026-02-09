import requests
import sys

for cloud_service in ['s3', 'blob.core', 'storage.googleapis']:
    r = requests.get(f'https://{sys.argv[1]}.{cloud_service}.com')
    if r.status_code != 404:
        print(f'[!] Cloud found: {cloud_service}')

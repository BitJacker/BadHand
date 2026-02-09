import requests
import sys

cms_dict = {'WP': '/wp-login.php', 'Joom': '/administrator/'}

for cms, path in cms_dict.items():
    if requests.get(sys.argv[1] + path).status_code == 200:
        print(f'CMS Detected: {cms}')

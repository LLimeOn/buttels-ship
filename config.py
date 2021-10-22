import requests
import os
f = requests.get("http://ifconfig.me/ip").text
print(f)

# IP = f'{f}'
IP = f'0.0.0.0'

PORT = os.environ.get('PORTCH')

SALT = 'SaltySaltySalt1'  # ur salt

# leave blank for WS protocol
SSL_CHAIN = ""
SSL_KEY = ""

import requests
f = requests.get("http://ifconfig.me/ip").text
print(f)

IP = f'{f}'
PORT = 7000

SALT = 'SaltySaltySalt1'  # ur salt

# leave blank for WS protocol
SSL_CHAIN = ""
SSL_KEY = ""

#! /usr/bin/env python

import requests
import base64
from cryptography.fernet import Fernet

crypt_flag = requests.get('https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/flag.txt.en').text
password = requests.get('https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/pw.txt').text.strip()

password = Fernet(base64.b64encode(password.encode()))

print(str(password.decrypt(crypt_flag.encode()))[2:-3])


# print(password.decrypt(crypt_flag.text.encode()))

#!/usr/bin/env python

import requests

r = requests.get('https://mercury.picoctf.net/static/2d24d50b4ebed90c704575627f1f57b2/flag')

print(r.text)
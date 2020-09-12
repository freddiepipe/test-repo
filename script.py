import sys
import requests

print(sys.executable)

r = requests.get('https://coreyms.com')
print(r.status_code)

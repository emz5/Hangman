import math
import sys

import requests

print(sys.version)
r = requests.get('https://google.com')
print(r.status_code)
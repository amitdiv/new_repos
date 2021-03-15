from nsetools import Nse
import time
from collections import OrderedDict
from urllib.error import HTTPError
nse = Nse()
d = OrderedDict({})
for i in range(10):
    try:
        data = nse.get_quote('lt')
        if data:
            d[time.time()] = data["basePrice"]
            time.sleep(2)
        else:
            raise Exception
    except HTTPError as e:
        d[time.time()]="NA"

print(d)












































































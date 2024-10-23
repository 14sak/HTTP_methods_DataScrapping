import requests as rq

PoUrl='https://httpbin.org/post'

PoHeader= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'user-name': "['Maharshtra','India']"
}

Poresp=rq.post(PoUrl)
print('PUT response = ',Poresp.content)
print()
print('Header = ',PoHeader['user-name'])
print()
print('Header Type = ',type(PoHeader['user-name']))
print()
strTOlist=list(PoHeader['user-name'])
print('Updated type of user_name header = ',type(strTOlist))

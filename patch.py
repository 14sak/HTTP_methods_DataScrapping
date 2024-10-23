import requests as rq

PaUrl='https://httpbin.org/patch'

PaHeader= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'user-name': "['Maharshtra','India']"
}

Paresp=rq.patch(PaUrl)
print('PUT response = ',Paresp.content)
print()
print('Header = ',PaHeader['user-name'])
print()
print('Header Type = ',type(PaHeader['user-name']))
print()
strTOlist=list(PaHeader['user-name'])
print('Updated type of user_name header = ',type(strTOlist))
 

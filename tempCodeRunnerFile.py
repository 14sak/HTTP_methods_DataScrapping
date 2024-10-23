import requests as rq

pUrl='https://httpbin.org/put'

pHeader= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'user-name': "['Maharshtra','India']"
}

Presp=rq.put(pUrl)
print('PUT response = ',Presp.content)
print()
print('Header = ',pHeader['user-name'])
print()
print('Header Type = ',type(pHeader['user-name']))
print()
strTOlist=list(pHeader['user-name'])
print('Updated type of user_name header = ',type(strTOlist))
 

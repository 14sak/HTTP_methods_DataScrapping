import requests as rq

qurl= 'https://httpbin.org/delete'

Qheader={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'User_Name':"['Sakshi','ARC']"
}
 
resp = rq.delete(url = qurl,headers= Qheader)
print('resp.content = ',resp.content)
print('----')
jresp=resp.json()
print('response_json = ',jresp['headers'])
print()
print('------')
strTOlist=list(Qheader['User_Name'])
print('User name = ',Qheader['User_Name'],'Type of header = ',type(strTOlist))
import requests  # εισαγωγή της βιβλιοθήκης

url = 'http://youtube.com/'  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    headers=response.headers
    cookiesnames=response.cookies
print("\nHeaders:",headers)
print("\nServer:", headers["Server"])
cookies=headers["Set-Cookie"].split("; ")
print("\nCookies:",cookies)
temp=[[]]
i=0
for token in cookies:
    temp[i].append(token)
    if 'Expires' in token:
        temp.append([])
        i+=1
print("\n",temp)
print("\n",cookiesnames)


import requests

url = input("\nenter url ")

with requests.get(url) as response:
    headers=response.headers
    cookiesnames=response.cookies.values()

print("\nHeaders:",headers)
print("\nServer:", headers["Server"])
try:
    cookies=headers["set-cookie"].split("; ")
    cookies=headers["Set-Cookie"].split("; ")

    expires=[]
    i=0
    for token in cookies:
        if 'Expires' in token or 'expires' in token:
            expires.append(token)
            i+=1

    if len(expires)<=len(cookiesnames):
        for j in range(len(expires)):
            print("\ncookie name:",cookiesnames[j],expires[j], "\n")
    else:
        for j in range(len(cookiesnames)):
            print("\ncookie name:",cookiesnames[j],expires[j], "\n")

except:
    print("\nno cookies found")
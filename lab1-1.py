import requests  # εισαγωγή της βιβλιοθήκης

url = 'http://youtube.com/'  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    a=response.headers
print("\nHeaders:",a)
print("\nServer:", a["Server"])
b=a["Set-Cookie"].split("; ")
print("\nCookies",b)

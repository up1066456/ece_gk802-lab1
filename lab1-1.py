import requests  # εισαγωγή της βιβλιοθήκης


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 5 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = input('url?')  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    print(response.headers)
    ##more(html)

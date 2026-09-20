import requests as rq
import bs4

response = rq.get("https://vietnamnet.vn/nguoi-dan-thao-do-nha-giao-mat-bang-lam-cau-duong-binh-tien-2556777.html")
print(response.status_code)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

x = soup.find_all('a')
text = ''
for i in range(len(x)):
    text += x[i].text.strip() + '\n'
    print(text)

print('--------------------')

s1 = '               ngUYỄN         vÂn aNH         '
s2 = s1.title().split()
s3 = " ".join(s2)
print(s3)

print('--------------------')

i1 = '1234-5678-2332'
i2 = i1.split('-')
for i in range(len(s2)-1):
    i2[i] = '****'
i3 = "-".join(i2)
print(i3)

print('--------------------')

import re
my_regex = re.compile("([0-9]+)[^0-9]+([0-9]+)" )
m = my_regex.search("Anna is 15 years old and John is 12 years old")

print(m.group(0))
print(m.group(1))
print(m.group(2))

print('--------------------')

my_regex_1 = re.compile("([^0-9]+([0-9]+[^0-9]+[0-9]+[^0-9]+[0-9]+))")
m = my_regex_1.search("Join 010-1234-5678")
print("Phone number: " + m.group(2))

# ([^0-9]+([0-9]+[^0-9]+[0-9]+[^0-9]+[0-9]+))
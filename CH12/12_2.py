import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 

sample = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_42.html').read()
actual = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_1705072.html').read()
x = True
while x:
    user = input("What file should I scan? Options: sample or actual: ").lower()
    if user == 'sample':
        html = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_42.html').read()
        x = False
    elif user == 'actual':
        html = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_1705072.html').read()
        x = False
    else:
        print("That's not an option dumb dumb...\n")

data = BeautifulSoup(html, 'html.parser')
elements = data('span')
grades = []
count = 0
for element in elements:
    grades.append(int(element.text))
    count = count +1

print('Count', count)
print('Sum', sum(grades))

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 

repeat = int(input('How many time should I run this? '))
start_pos = int(input('What is the staring postion? '))

names = []
html = None

while(True):
    user = input("What file should I scan? Options: sample or actual: ").lower()
    if user == 'sample':
        html = urllib.request.urlopen('https://py4e-data.dr-chuck.net/known_by_Fikret.html').read()
        break
    elif user == 'actual':
        html = urllib.request.urlopen('https://py4e-data.dr-chuck.net/known_by_Lloyde.html').read()
        break
    else:
        print("That's not an option dumb dumb...\n")

data = BeautifulSoup(html, 'html.parser')
tags = data('a')

for line in tags:
    names.append(line.text)

set_name = names[start_pos-1]
    
print(set_name)

for loop_name in range(repeat-1):
    new_link = urllib.request.urlopen('https://py4e-data.dr-chuck.net/known_by_'+ set_name + '.html').read()
    data = BeautifulSoup(new_link, 'html.parser')
    tags = data('a')
    new_names = []
    for line in tags:
        new_names.append(line.text)
    set_name = new_names[start_pos-1]
    print(set_name)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL Certificate errors
ctx =ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) <1:
    url = 'http://python-data.dr-chuck.net/known_by_Conar.html'
def user_inputs():
    x = int(input('Enter count: '))
    y = int(input('Enter position:'))-1
    return x,y

count, pos = user_inputs()    

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")
href = soup('a')

for i in range(count):
    link = href[pos].get('href', None)
    print('Retrieving: ',link)
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')
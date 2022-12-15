import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as soup
import ssl

#Ignore SSL Certificate errors
ctx =ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) <= 1:
    url = 'https://webscraper.io/test-sites'
    
html = urllib.request.urlopen(url, context=ctx).read()
clean_url = soup(html, 'html.parser')

tags = clean_url('a')

for tag in tags:
    print('comments',tag.contents[0])
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input ('Enter url: ')
if len(url) == 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
else:
    url = 'http://py4e-data.dr-chuck.net/comments_1705074.xml'
    
print('Retrieving', url)

total = 0
count = 0

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
lst = tree.findall ('comments/comment')

for item in lst:
    count = count + 1
    t = item.find ('count').text
    total = total + float (t)
    
print ('Count:', count)
print ('Sum:' , total)


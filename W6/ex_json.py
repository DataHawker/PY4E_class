import urllib.request, json 
with urllib.request.urlopen("https://py4e-data.dr-chuck.net/comments_42.json") as url:
    data = json.load(url)
    #print(data)
    
print(data)
print('User count:', len(data))

for i in data:
    print('Name',i['name'])
   
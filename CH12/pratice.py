

from bs4 import BeautifulSoup
import requests

# HTML From Website
url = "http://books.toscrape.com/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc("product_pod")
print(prices)
# parent = prices[0].parent
# print(parent)
# strong = parent.find("strong")
# sup = parent.find("sup")
# print("$"+strong.string + sup.string)
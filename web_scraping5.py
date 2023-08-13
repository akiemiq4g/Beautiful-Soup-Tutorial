from bs4 import BeautifulSoup
import requests

url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=macbook+pro+m2+max&_sacat=0&LH_TitleDesc=0&SSD%2520Capacity=1%2520TB&_sop=16&rt=nc&RAM%2520Size=64%2520GB&_oaa=1&_dcat=111422"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

titles = doc.find(string="s-item__title")
#parent = titles[0].parent()
print(titles.string)
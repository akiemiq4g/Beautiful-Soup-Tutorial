from bs4 import BeautifulSoup
import requests

# HTML From File
with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("p")[0]

print(tags.find_all("b"))

# HTML From Website
url = """https://www.bhphotovideo.com/c/search?Ntt=Apple%20Macbook%20Pro%20M1%20Pro%2016&N=0&InitialSearch=
yes&ap=Y&gclid=Cj0KCQjwrMKmBhCJARIsAHuEAPSvPQvpNZYXwr7OxyYPWth9ncxicHMFLPzoSdFFPmueDBXrhZq_rGEaAq3eEALw_wcB"""

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent()
strong = parent.find("strong")
print(strong.string)

import requests
from bs4 import BeautifulSoup
with open("sample.html", "r") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title.string, type(soup.title))
print(soup.div)
print(soup.find_all('div'))
for link in soup.find_all("a"):
    print(link.get("href"))
    print(soup.select("div.italic"))
    container = soup.find(class_="container")
if container:
    for child in container.children:
        print(child)
else:
    print("Container nahi mila")
from bs4 import BeautifulSoup
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
url="https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
result = requests.get(url,headers=headers)
doc = BeautifulSoup(result.text, "html.parser")

# scraped the title of the book
Title=doc.find("h1")
print(Title.text)

# scraped the price of the book
price=doc.find("p",class_="price_color")
print(price.text)   

# availablity of the book 
stock = doc.find("p", class_="instock availability")
print(stock.text)

# Rating of the book 
rate=doc.find("p",class_="star-rating")
print(rate["class"])

desciption=doc.find("meta",attrs={"name":"description"})
print(desciption["content"])
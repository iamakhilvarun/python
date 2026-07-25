from bs4 import BeautifulSoup
import re
with open("web_scraping/index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
# Finding the tags
# tag = doc.find_all(["p",'div','li'])
# changing the attributes
# tag[0]['selected'] = "false"
# tag[0]['color']='blue'
# print(tag[0]) 
tags=doc.find_all("input",type="text")
for tag in tags:
    tag['placeholder']

with open("changed.html","w") as file:
    file.write(str(doc))

import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html

page=requests.get('http://www.boxofficemojo.com/yearly/chart/?yr=2016&p=.htm')
soup=BeautifulSoup(page.content,'html.parser')
webpage = html.fromstring(page.content)
akhil=webpage.xpath('//a/@href')


a=soup.find("table",bgcolor="#ffffff")

israel=[]
japan=[]
internal_links=[]

td_tags = a.find_all('td')
for i in td_tags:
    israel.append(i.text)



for link in akhil:
        if "page" in link:
            internal_links.append("http://www.boxofficemojo.com/"+link)


def all_data(link):
    page=requests.get(link)
    soup=BeautifulSoup(page.content,'html.parser')
    webpage = html.fromstring(page.content)
    akhil=webpage.xpath('//a/@href')
    a=soup.find("table",bgcolor="#ffffff")
    td_tags = a.find_all('td')
    for i in td_tags:
        israel.append(i.text)


for i in internal_links:
    all_data(i)

whole_list=israel[8:]
y = zip(*[iter(whole_list)]*9)
pa=list(y)

#

columns=["rank","Movie_Name","Studio","Gross","Theaters","opening","Theaters","Open","close"]
df=pd.DataFrame(pa,columns=columns)
print(df.tail(30))

print(df.describe())

movie_names=df['Movie_Name'].tolist()

for i in y:
    print(i)
    



























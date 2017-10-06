import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html

page=requests.get('http://www.boxofficemojo.com/yearly/chart/?yr=2016&p=.htm')
soup=BeautifulSoup(page.content,'html.parser')
webpage = html.fromstring(page.content)
akhil=webpage.xpath('//a/@href')


movie_links=[]
internal_links=[]
real_links=[]
b_list=[]
universal=[]
#this is for internal links
for link in akhil:
        if "page" in link:
            internal_links.append("http://www.boxofficemojo.com/"+link)



"""
#this is for first 100 links
for link in akhil:
    if "movies" in link:
        movie_links.append("http://www.boxofficemojo.com/"+link)
"""

for i in movie_links:
    print(i)

"""

#this is for rest of 635 links
def all_links(link):
    page=requests.get(link)
    soup=BeautifulSoup(page.content,'html.parser')
    webpage = html.fromstring(page.content)
    akhil=webpage.xpath('//a/@href')
    for link in akhil:
        if "movies" in link:
            movie_links.append("http://www.boxofficemojo.com/"+link)

for link in internal_links:
    all_links(link)

"""

       
#real scrapping
#for link in movie_links:
#    page=requests.get(link)
#    soup=BeautifulSoup(page.content,'html.parser')
#    all_bs=soup.findAll('b')
#    for t in all_bs:
#        b_list.append(t)

#for i in b_list:
#    universal.append(i.text)

#y = zip(*[iter(universal)]*8)
#pa=list(y)
#columns=["TDCJ_Number","Link","Last_Name","First_Name","Date_of_Birth","Gender","Race","Date_Received"]

#p=pd.DataFrame(pa,columns=columns)
#print(p.head())

#print(len(universal))






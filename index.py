import requests
from bs4 import BeautifulSoup


page=requests.get('http://www.boxofficemojo.com/movies/?id=tmnt2016.htm')
soup=BeautifulSoup(page.content,'html.parser')



israel=[]

links=[]

for tr in soup.find('table.b',width="95%"):
#    print(tr.text)
    links.append(tr.text)

#pop=soup.find('div',class_="mp_box_tab")
#print(pop)

for link in links:
    loc=link.index(':')
    print(link[loc+1:len(link)-1])

print(links)

print(soup.find('table.b',width="95%"))


all_bs=soup.findAll('b')
b_list=[] #lots of the information we want is in bold, and appears in the same order on each page
for t in all_bs:
    if 'Domestic Lifetime' not in t.encode_contents():#want to ignore the lifetime box office
        b_list.append(t.encode_contents())
    if len(b_list)>=10:#avoids bad entries with no box office data
            if '$'in b_list[2] or 'n/a' in b_list[9]:#avoid movies w/o box office data, or unadjustable box office data, if not caught above
                if 'n/a' in b_list[9]:#has a foreign release only, order is shifted
                    title=b_list[1]
                    domestic='N/A'
                    if 'N/A' not in b_list[2]:
                        distributor=b_list[2].split('>')[1].split('<')[0]
                    else:
                        distributor=b_list[2]
                    if len(b_list[3].split('>'))>3:#sometimes the release date is not in a hyperlink
                        release=b_list[3].split('>')[2].split('<')[0]
                    else:
                    release=b_list[3].split('>')[1].split('<')[0]
                    genre=b_list[4]
                    runtime=b_list[5]
                    rating=b_list[6]
                    budget=b_list[7]
                    worldwide=b_list[12]
                else:   #has a domestic release
                    title=b_list[1]
                    domestic=b_list[2]
                    if 'n/a' not in b_list[3]:
                    distributor=b_list[3].split('>')[1].split('<')[0]
                    else:
                    distributor=b_list[3]
                    if len(b_list[4].split('>'))>3:#sometimes the release date is not in a hyperlink
                    release=b_list[4].split('>')[2].split('<')[0]
                    else:
                    release=b_list[4].split('>')[1].split('<')[0]
                    genre=b_list[5]
                    runtime=b_list[6]
                    rating=b_list[7]
                    budget=b_list[8]
                    if len(b_list)==11 or '%' not in b_list[11]:#this means it only has a domestic release
                                                worldwide='N/A'
                   else:
                       return (title,director1,director2,domestic,distributor,release,genre,runtime,rating,budget,worldwide,actor1,actor2,actor3,actor4,actor5,actor6,producer1,producer2,producer3,producer4,producer5,producer6,writer1,writer2,composer1,composer2)


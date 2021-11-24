from bs4 import BeautifulSoup
import time
import csv
import requests
starturl="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser.get(starturl)
headers=["Name","Mass","Radius","Distance"]
Mt_list=[]
soup=beautifulSoup(page.content,"html.parcer")
table=soup.find_all("table")
tablerows=table[7].findall("tr")
radius=headers[3]
mass=headers[2]
df=df[df[radius].notna()]
for tr in tablerows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    Mt_list.append(row)
Star_name=[]
radius=[]
mass=[]
for i in range(1,len(Mt_list):
    star_name.append(Mt_list[i][0])
    distance.append(Mt_lsit[i][5])
    mass.append(Mt_list[i][7])
    radius.append(Mt_list[i][])
distance=[]
def scrapemodedata(hyperlink):
    page=requests.get(hyperlink)
   
    temlist=[]
    for trtag in soup.find_all("tr",attrs={"class":"fact_row"}):
        tdtag=trtag.find_all("td")
        for tdtags in tdtag:
            try:
                temlist.append(tdtags.find_all("td",attrs={"class":"value"})[0].contents[0])
            except:temlist.append("")
    newplanetdata.append(temlist)

    for index,data in enumerate(planetdata):
    scrapemodedata(data[5])

bababoeystar=[]
for index,data in enumerate(stardata):
    newstardataelement=newstardata[index]
    newpstardataelment=[elem.replace("\n", "") for elem in newstardataelement
    newpstardataelement=newplanetdataelement[:7]
    bababoeystar.append(data+newstardataelement)
with open("scraper2.csv","w") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)  
    csvwriter.writerows(finalplanetdata)
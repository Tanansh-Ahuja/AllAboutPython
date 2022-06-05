import bs4
import requests
from requests.models import encode_multipart_formdata
url='https://www.currentresults.com/Weather/India/average-annual-temperatures.php'
res = requests.get(url).text
soup = bs4.BeautifulSoup(res,'lxml')
gdp_table = soup.find_all("table", attrs={"class": "articletable"})
alltables=[]
#ab bhai gdp table me saari tables hai
#baari baari, eke ek table ko dictionary banana padega
#print(gdp_table)
#print(list(gdp_table)[0])
for table in gdp_table:
    #table contains 1 table from the list of 4 tables

    headings=[]
    tableheadings = table.thead.find_all('tr')
    #print(tableheadings)
    for th in tableheadings[0].find_all('th'):
        headings.append(th.text.replace('\n', ' ').strip())
    #print(headings)
    #break

    contents=[]
    tablecontent = table.tbody.find_all('tr')
    #print(tablecontent)
    for row in tablecontent:
        onerow=[]
        for element in row.find_all('td'):
            onerow.append(element.text.replace('\n',' ').strip())
        contents.append(onerow)
    #print(contents)
        
    x = dict()
    for heading in headings:
        x.update({heading:[]})
    for row in contents:
        for i in range(len(row)):
            temp = x[headings[i]]
            temp.append(row[i])
            x.update({headings[i]:temp})
    #print(x)
    alltables.append(x)
    

print(alltables)



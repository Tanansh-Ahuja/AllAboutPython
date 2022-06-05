import bs4
import requests
from requests.models import encode_multipart_formdata
url='https://www.currentresults.com/Weather/India/average-annual-temperatures.php'
res = requests.get(url).text
soup = bs4.BeautifulSoup(res,'lxml')
#print(soup.title.text)


gdp_table = soup.find("table", attrs={"class": "articletable"})

'''
for table in gdp_table:
    gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 5 colms
   
    print(list(gdp_table_data[0].find_all("td")))
        
    headings = []
    for td in gdp_table_data[0].find_all("td"):
        headings.append(td.text.replace('\n', ' ').strip())

    data = {}
    for table, heading in zip(gdp_table_data[1].find_all("table"), headings):
        t_headers = []
        for th in table.find_all("th"):
            t_headers.append(th.text.replace('\n', ' ').strip())
        # Get all the rows of table
        table_data = []
        for tr in table.tbody.find_all("tr"): 
            t_row = {}

            for td, th in zip(tr.find_all("td"), t_headers): 
                t_row[th] = td.text.replace('\n', '').strip()
            table_data.append(t_row)

        data[heading] = table_data

    print(data)
    break
'''
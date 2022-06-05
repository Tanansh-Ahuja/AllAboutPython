import bs4
import requests
res = requests.get('https://www.amazon.in/Mediker-Sanitizer-Alcohol-Instantly-Anywhere/dp/B086R35Z6G/ref=dp_prsubs_1?pd_rd_i=B086R35Z6G&psc=1')
print(res.raise_for_status)
#soup = bs4.BeautifulSoup(res.text)
soup = bs4.BeautifulSoup(res.text,'html.parser')
s=soup.select('#priceblock_ourprice')
print(s)

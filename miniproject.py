from selenium import webdriver
import requests,bs4



a=input("Enter song name: ")
url = "http://www.google.com/search?btnG=1&q=" +a
res=requests.get(url)
print(res.raise_for_status)
soup = bs4.BeautifulSoup(res.text , 'html.parser')
#soup.select('//div[@id="kp-wp-tab-overview"]/div[3]/div/div/div/div[1]/div/div')
chromedriver='E:\\PYTHON\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get(url)
name = driver.find_elements_by_xpath('//div[@id="kp-wp-tab-overview"]/div[3]/div/div/div/div[1]/div/div')

a=len(name)
for i in range(a):
    print(name[i].text)

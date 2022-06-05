from selenium import webdriver
#import webbrowser
chromedriver="C:\\Users\\com\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
#driver.get("http://econpy.pythonanywhere.com/ex/001.html")

maxpagenum=5
maxpagedig=3
for i in range(1,maxpagenum+1):
    page_num = (maxpagedig - len(str(i)) )*"0" + str(i)
    url = "http://econpy.pythonanywhere.com/ex/"+page_num+".html"
    print(url)
    driver.get(url)
    buyers = driver.find_elements_by_xpath('//div[@title = "buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class = "item-price"]')
    a=len(buyers)
    for i in range(a):
        print(buyers[i].text," : ", prices[i].text)



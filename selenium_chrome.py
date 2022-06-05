from selenium import webdriver

#driver = webdriver.Firefox()
#driver.get("www.google.com")
# only works with firefox


#chrome
chromedriver="C:\\Users\\com\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("http:facebook.com")

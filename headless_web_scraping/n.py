from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

 
url = "http://hotels.com" 

options = webdriver.ChromeOptions() 
options.headless = False
with webdriver.Chrome(options=options) as driver: 
    
	driver.get(url) 
	input = driver.find_element(By.CSS_SELECTOR, "form[role='search'] input[type='text']")
	input.send_keys("London" + Keys.ENTER)
 
	print(driver.current_url) 
	print(driver.title)
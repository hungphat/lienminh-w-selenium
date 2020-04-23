from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/hungphat/Phat/SeleniumTrang/chromedriver")
driver.implicitly_wait(10)

url = 'https://google.com'

driver.get(url)
q = driver.find_element_by_name("q")
q.send_keys("lien minh huyen thoai")
q.submit()

c = driver.find_element_by_xpath("//div//h3").click()
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/hungphat/Phat/SeleniumTrang/chromedriver")
driver.implicitly_wait(10)

url = 'https://app.mobalytics.gg/champions'

driver.get(url)
c = driver.find_element_by_class_name('supportRole').click()


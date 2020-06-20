from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.implicitly_wait(10)

url = 'https://lienminh.garena.vn'

driver.get(url)

driver.find_element_by_xpath('//a[text()="Giới thiệu"]').click()
driver.find_element_by_xpath('//*[@id="toc"]/div[3]/div[2]/div[2]/div[4]/div[1]/a').click()
q = "/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div[2]/div[1]/div/div/div/ul/li"
champion_list = driver.find_elements_by_xpath(q)

for champion in champion_list:
    champion_name = champion.text

# driver.find_element_by_link_text("/game-info]").click()

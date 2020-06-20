from selenium import webdriver

wd = webdriver.Chrome(executable_path="./chromedriver")
wd.implicitly_wait(10)

url = 'https://lienminh.garena.vn'

wd.get(url)

wd.find_element_by_xpath('//a[text()="Giới thiệu"]').click()
wd.find_element_by_xpath('//*[@id="toc"]/div[3]/div[2]/div[2]/div[4]/div[1]/a').click()
q = "/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div[2]/div[1]/div/div/div/ul/li"
champion_list = wd.find_elements_by_xpath(q)

for champion in champion_list:
    champion_name = champion.text
wd.quit()

from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.implicitly_wait(10)

url = 'https://app.mobalytics.gg/lol/champions'

driver.get(url)

q = '//*[@id="app-content"]/div/div[4]/div[2]/div[4]/a'
champion_list = driver.find_elements_by_xpath(q)

for champion in champion_list:
    champion_name = champion.text

# driver.find_element_by_link_text("/game-info]").click()

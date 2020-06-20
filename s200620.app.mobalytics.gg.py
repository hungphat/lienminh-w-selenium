from selenium import webdriver

wd = webdriver.Chrome(executable_path="./chromedriver")
wd.implicitly_wait(10)

url = 'https://app.mobalytics.gg/lol/champions'

wd.get(url)

q = '//*[@id="app-content"]/div/div[4]/div[2]/div[4]/a'
champion_list = wd.find_elements_by_xpath(q)

for champion in champion_list:
    champion_name = champion.text

wd.quit()

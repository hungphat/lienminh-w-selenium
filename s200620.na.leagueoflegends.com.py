from selenium import webdriver

wd = webdriver.Chrome(executable_path="./chromedriver")  # wd aka web_driver
wd.implicitly_wait(10)

url = 'https://na.leagueoflegends.com/en-us/champions/'

wd.get(url)

q = '//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[2]/div[2]/a'
champion_list = wd.find_elements_by_xpath(q)

for champion in champion_list:
    champion_name = champion.text
    i =122

# driver.find_element_by_link_text("/game-info]").click()

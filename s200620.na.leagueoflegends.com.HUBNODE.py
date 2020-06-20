from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


#region wd from selenium hubnode
SELENIUM_HUB = 'http://localhost:4444/wd/hub'
wd = webdriver.Remote(
  command_executor=SELENIUM_HUB,
  desired_capabilities=DesiredCapabilities.CHROME,
)
wd.implicitly_wait(10)
#endregion

url = 'https://na.leagueoflegends.com/en-us/champions/'

wd.get(url)

q = '//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[2]/div[2]/a'
champion_list = wd.find_elements_by_xpath(q)

champion_name_all = []
for champion in champion_list:
    champion_name = champion.text
    if champion_name:
        champion_name_all.append(champion_name)

wd.quit()

print(champion_name_all)
print(f'{len(champion_name_all)} found.')

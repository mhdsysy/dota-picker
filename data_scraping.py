import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure the chromedriver options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# Create a driver
driver = webdriver.Chrome("SET_THE_PATH_FOR_CHROME_DRIVER_HERE", chrome_options=options)


# An array that holds the names of all heroes
def find_hero_names(hero_names):
    driver.get("https://www.dotabuff.com/heroes")

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    names = soup.find_all("div", {"class": "name"})
    for row in names:
        for name in row:
            helper = ((((name.encode('ascii'))).decode('ascii')).replace(' ', '-').lower()).replace("'", '')
            hero_names.append(helper)

    return hero_names


def find_counters(hero_name):
    hero_names = []
    # Set path to Chrome driver, so that our web driver will use it
    url = "https://www.dotabuff.com/heroes/" + hero_name + "/counters?date=week"

    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    table = (soup.find("table", {"class": "sortable"}))
    rows = table.find_all("td", {"class": "cell-xlarge"})

    for row in rows:
        for element in row:
            if len(hero_names) < 20:
                hero_names.append(element.text.strip())
            else:
                break

    return hero_names


# Create the hero names column


def create_data():
    all_heroes = []
    find_hero_names(all_heroes)
    helper = {}
    for hero in all_heroes:
        helper[hero] = find_counters(hero)

    df = pd.DataFrame(helper).melt(var_name="hero_name", value_name="counters")

    return df.to_csv("counters.csv", index=False)


create_data()

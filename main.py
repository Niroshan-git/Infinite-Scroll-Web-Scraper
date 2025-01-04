from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from bs4 import BeautifulSoup

url = "https://www.fintastico.com/fintech-uk/"

path_to_file = r"D:\Projects\Web Scraping Projects\Web Scraping- Infinit Scrolling\\"

mode = "extract" #mode=extract/scrape/""

if mode != "extract":

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(url)

    last_height = 0

    while True:
        driver.execute_script('window.scrollBy(0,2000)')
        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")
        print(str(new_height)+"-"+str(last_height))

        if(new_height == last_height):
            break

        else:
            last_height = new_height


    page_source =  driver.page_source

    f = open(path_to_file+"source.txt", "w", encoding="utf-8")
    f.write(page_source)
    f.close()

if mode != "scrape":
    data = []

    f = open(path_to_file+"source.txt", "r", encoding="utf-8")
    page_source = f.read()
    f.close()

    soup = BeautifulSoup(page_source,features="lxml")

    items = soup.findAll("a", class_="card")

    for item in items:
        item_out = {}

        item_out['Title'] =  item.find("h4").text
        item_out['Link'] = item.attrs['href']
        item_out['Description'] = item.find("p").text

        data.append(item_out)

df = pd.DataFrame(data)
df.to_excel(path_to_file+"startups.xlsx")
df.to_json(path_to_file+"startups.json")
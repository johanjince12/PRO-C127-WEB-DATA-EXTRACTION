from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Edge("D:\Shashwat Namdev\PRO-C127-Project-Boilerplate-main\msedgedriver.exe")
browser.get(START_URL)

time.sleep(6)

star_data=[]
scrapped_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")

    bright_star_table = soup.find('table',attrs={'class','wikitable'})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        temp_list = []

        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)
        
        scrapped_data.append(temp_list)

scrape()

for i in range(0,len(scrapped_data)):
    star_name = scrapped_data[i][1]
    distance = scrapped_data[i][3]
    mass = scrapped_data[i][5]
    radius = scrapped_data[i][6]
    lum = scrapped_data[i][7]

    required_data = [star_name,distance,mass,radius,lum]
    star_data.append(required_data)

print(star_data)

headers = ['Star Name', 'Distance','Mass','Radius','Luminosity']
star_df_1 = pd.DataFrame(star_data,columns=headers)
star_df_1.to_csv('scraped_data.csv',index=True,index_label='id')
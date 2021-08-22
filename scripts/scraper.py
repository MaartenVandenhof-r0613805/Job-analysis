import glob
import pandas as pd
import json
import configparser
import re
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4

# Initialize variables
# Windows PC:
PATH = "../drivers/chromedriver.exe"

# LINUX PC:
# PATH = "./drivers/chromedriver"

chrome_options = Options()
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome(PATH, options=chrome_options)
url_login = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
url_jobs = "https://www.linkedin.com/jobs/search/?geoId=100565514&keywords=data%20science&location=Belgi%C3%AB"
driver.get(url_login)

dataJSON = {'resultData': []}


# FUNCTIONS

# SCRIPT

# Remove Agree button and grayed out background
# jsname = "bF1uUb"
# driver.execute_script("document.querySelector('[jsname=" + jsname + "]').style.display = 'none'")
# className = "bErdLd aID8W wwYr3"
# driver.execute_script("document.getElementsByClassName('" + className + "')[0].style.display = 'none'")
# driver.execute_script("document.getElementsByTagName('html')[0].style.overflow = 'auto'")

# Variables
soup = bs4.BeautifulSoup()
jobs_class = "jobs-search-results__list-item occludable-update p0 relativeember-view"
df = pd.DataFrame(columns=["Title", "Company", "Location", "Description"])

# Add LinkedIn Jobs to DF
def addJobToDF(soup_element):


jobList = soup.findAll('li', {'class': jobs_class})
for el in jobList:
    addJobToDF(el)

# GET LINKEDIN DATA COMPANIES
# Initialize LinkedIn with local account details
# (create your own config.ini with account details local and point to that path)
accountDetailsConfig = configparser.ConfigParser()
#accountDetailsConfig.read('C:/Users/Maarten Van den hof/Documents/config.ini')
accountDetailsConfig.read('C:/Users/maart/Documents/config.ini')
driver.get("https://www.linkedin.com/")
driver.find_element_by_id("session_key").send_keys(accountDetailsConfig['CREDS']['USERNAME'])
driver.find_element_by_id("session_password").send_keys(accountDetailsConfig['CREDS']['PASSWORD'])
driver.find_elements_by_class_name("sign-in-form__submit-button")[0].click()
print('wait')
time.sleep(10)
driver.get(url_jobs)
scraper_df = pandas.DataFrame(columns=['Name', 'ScraperCategory', 'Jobs', 'Category', 'Date'])
# Get linkedin links


print(scraper_df)

# Write JSON file
with open('./data/WebscrapeData.json', 'w') as out:
    parsed = json.loads(scraper_df.to_json(orient="table"))
    json.dump(parsed, out, indent=4)

# Close browser
driver.quit()

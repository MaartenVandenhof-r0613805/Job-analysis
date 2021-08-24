import pandas as pd
import configparser
import time
import json
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4

# Initialize variables
# Windows PC:
PATH = "../drivers/chromedriver.exe"

# LINUX PC:
# PATH = "./drivers/chromedriver"

chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(PATH, options=chrome_options)
url_login = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
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
jobs_class = "jobs-search-results__list-item"
jobs_list = []


# Add LinkedIn Jobs to DF
def addJobToDF(soup_element):
    time.sleep(1)
    if soup_element.select("h3[class*=_title]"):
        return
    try:
        title = soup_element.select("a[class*=_title]")[0].getText().strip("',/\n")
    except:
        print(soup_element)
        title = None
    try:
        company = soup_element.select("a[class*=_company-name]")[0].getText().strip("',/\n")
    except:
        company = None
    try:
        location = soup_element.select("li[class*=job-card-container__metadata-item]")[0].getText().strip("',/\n")
    except:
        location = None

    try:
        t_el = driver.find_element_by_id(soup_element.select("a[class*=_title]")[0].get("id"))
        t_el.click()
        time.sleep(0.5)
        description = bs4.BeautifulSoup(driver.page_source).select("div[class*=jobs-description-content__text]")[0] \
            .getText().strip("',/\n")
    except:
        description = None

    new_row = {"Title": title,
               "Company": company,
               "Location": location,
               "Description": description}

    # print(new_row)
    jobs_list.append(new_row)


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

i = 25
url_jobs = "https://www.linkedin.com/jobs/search/?geoId=100565514&keywords=data%20science&location=Belgi%C3%AB"

while i <= 1000:
    driver.get(url_jobs)
    time.sleep(7)

    try:
        # Get linkedin jobs
        soup = bs4.BeautifulSoup(driver.page_source)
        card_list = soup.select('li[class*="jobs-search-results_"]')
        middle_card = driver.find_element_by_id(card_list[7].get("id"))
        driver.execute_script("arguments[0].scrollIntoView()", middle_card)
        time.sleep(1)
        middle_card_2 = driver.find_element_by_id(card_list[14].get("id"))
        driver.execute_script("arguments[0].scrollIntoView()", middle_card_2)
        time.sleep(1)
        middle_card_3 = driver.find_element_by_id(card_list[21].get("id"))
        driver.execute_script("arguments[0].scrollIntoView()", middle_card_3)
        time.sleep(1)
        last_card = driver.find_element_by_id(card_list[len(card_list) - 2].get("id"))
        driver.execute_script("arguments[0].scrollIntoView()", last_card)
        time.sleep(1)

        soup = bs4.BeautifulSoup(driver.page_source)
        loaded_list = soup.select('li[class*="jobs-search-results_"]')

        # For each job card, get data
        for el in loaded_list:
            addJobToDF(el)
    except:
        print("page source error")

    url_jobs = "https://www.linkedin.com/jobs/search/?alertAction=viewjobs&geoId=100565514&keywords=data%20science" \
               "&location=Belgi%C3%AB&start=" + str(i)
    i = i + 25

jobs_df: DataFrame = pd.DataFrame(jobs_list)
print(jobs_df.head())
print(jobs_df.info())

# Close browser
driver.quit()

# Make Json
js = jobs_df.to_json(orient="records")
with open("../data/Jobcards.json", "w") as outfile:
    json.dump(js, outfile)

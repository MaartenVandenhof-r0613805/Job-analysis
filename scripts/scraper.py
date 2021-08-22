import pandas as pd
import configparser
import time
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
jobs_class = "jobs-search-results__list-item"
jobs_list = []


# Add LinkedIn Jobs to DF
def addJobToDF(soup_element):
    try:
        title = soup_element.select("a[class*=_title]")[0].getText()
    except:
        title = "None"
    try:
        company = soup_element.select("a[class*=_company-name]")[0].getText()
    except:
        company = "None"
    try:
        location = soup_element.select("li[class*=job-card-container__metadata-item]")[0].getText()
    except:
        location = "None"
    new_row = {"Title": title,
                    "Company": company,
                    "Location": location}
    print(new_row)
    jobs_list.append(new_row)


# GET LINKEDIN DATA COMPANIES
# Initialize LinkedIn with local account details
# (create your own config.ini with account details local and point to that path)
accountDetailsConfig = configparser.ConfigParser()
accountDetailsConfig.read('C:/Users/Maarten Van den hof/Documents/config.ini')
# accountDetailsConfig.read('C:/Users/maart/Documents/config.ini')
driver.get("https://www.linkedin.com/")
driver.find_element_by_id("session_key").send_keys(accountDetailsConfig['CREDS']['USERNAME'])
driver.find_element_by_id("session_password").send_keys(accountDetailsConfig['CREDS']['PASSWORD'])
driver.find_elements_by_class_name("sign-in-form__submit-button")[0].click()
driver.get(url_jobs)
time.sleep(10)

# Get linkedin jobs
print("go")
soup = bs4.BeautifulSoup(driver.page_source)
for el in soup.select('li[class*="jobs-search-results_"]'):
    addJobToDF(el)
print("done")
jobs_df = pd.DataFrame(jobs_list)
print(jobs_df.head())
# Close browser
driver.quit()

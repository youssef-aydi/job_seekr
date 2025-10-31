from selenium import webdriver
import pandas as pd
import time
import os
import selenium
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.firefox.service import Service as Firefox_Service
from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.common.by import By


use_chrome = "chrome"
use_firefox = "firefox"

# set this to one of the variables above: use_{your browser} 
mywebdriver = use_firefox

def initialize():
    global mywebdriver
    if mywebdriver == use_chrome:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        s = Chrome_Service(executable_path=r"./drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=option)
        return driver
    elif mywebdriver == use_firefox:
        option = Firefox_Options()
        option.headless = True
        s = Firefox_Service(executable_path=r"./drivers/geckodriver.exe", log_path= os.path.devnull)
        driver = webdriver.Firefox(service=s, options=option)

        return driver    
    else:
        print("Variable mywebdriver set to an unsupported browser.")
        return

def find_all_jobs():
    driver = initialize()
    url = "https://www.linkedin.com/jobs/search?keywords=&location=Tunis%2C%20Tunis%2C%20Tunisia&geoId=104991847&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    driver.get(url)
    content = driver.page_source
    
    print("LINKEDIN: Scraping all..")
    
    no_of_jobs = int(driver.find_element(By.CSS_SELECTOR, 'h1>span').get_attribute('innerText'))
    if no_of_jobs > 200:
        no_of_jobs = 200
    i = 2
    while i <= int(no_of_jobs/25)+1:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight );")
        i = i + 1
        try:
            driver.find_element(By.XPATH, '/html/body/div/div/main/section/button').click()
            time.sleep(2)
        except:
            pass
            time.sleep(2)

    job_lists = driver.find_element(By.CLASS_NAME, "jobs-search__results-list")
    jobs = job_lists.find_elements(By.TAG_NAME, 'li')

    job_id = []
    job_title = []
    company_name = []
    location = []
    date = []
    job_link = []
    for job in jobs:

        job_id.append(job.get_attribute('data - id'))
        job_title.append(job.find_element(By.CSS_SELECTOR, 'h3').get_attribute('innerText'))
        company_name.append(job.find_element(By.CSS_SELECTOR, 'h4').get_attribute('innerText'))
        location.append(job.find_element(By.CSS_SELECTOR, '[class="job-search-card__location"]').get_attribute('innerText'))
        date.append(job.find_element(By.CSS_SELECTOR, 'div > div > time').get_attribute('datetime'))
        job_link.append(job.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))

    job_data = pd.DataFrame({
        'Title': job_title,       
        'Company': company_name,
        'Location': location,
        'Date': date,
        'Apply Here': job_link
    })
    job_data.to_csv("./results/LINKEDIN_A_Results.csv",index=False)
    driver.quit()
    print("LINKEDIN: Finished scraping.")
    return job_data

def find_keyword_jobs(keyword):
    
    driver = initialize()
    url = "https://www.linkedin.com/jobs/search?keywords=" + keyword + "&location=Tunis%2C%20Tunis%2C%20Tunisia&geoId=104991847&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    driver.get(url)
    content = driver.page_source

    print("LINKEDIN: Scraping by keyword..")
    
    no_of_jobs = int(driver.find_element(By.CSS_SELECTOR, 'h1>span').get_attribute('innerText'))
    if no_of_jobs > 200:
        no_of_jobs = 200    
    
    i = 2
    while i <= int(no_of_jobs/25)+1:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight );")
        i = i + 1
        try:
            driver.find_element(By.XPATH, '/html/body/div/div/main/section/button').click()
            time.sleep(2)
        except:
            pass
            time.sleep(2)

    job_lists = driver.find_element(By.CLASS_NAME, "jobs-search__results-list")
    jobs = job_lists.find_elements(By.TAG_NAME, 'li')

    job_id = []
    job_title = []
    company_name = []
    location = []
    date = []
    job_link = []
    i = 0
    length = len(jobs)
    for job in jobs:
        print(str(i*100/length) + "%")
        i =i + 1
        job_id.append(job.get_attribute('data - id'))
        job_title.append(job.find_element(By.CSS_SELECTOR, 'h3').get_attribute('innerText'))
        company_name.append(job.find_element(By.CSS_SELECTOR, 'h4').get_attribute('innerText'))
        location.append(job.find_element(By.CSS_SELECTOR, '[class="job-search-card__location"]').get_attribute('innerText'))
        date.append(job.find_element(By.CSS_SELECTOR, 'div > div > time').get_attribute('datetime'))
        job_link.append(job.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))

    job_data = pd.DataFrame({
        'Title': job_title,
        'Company': company_name,
        'Location': location,
        'Date': date,
        'Apply Here': job_link
    })
    job_data.to_csv("./results/LINKEDIN_K_Results.csv",index=False)
    driver.quit()
    print("LINKEDIN: Finished scraping.")
    return job_data

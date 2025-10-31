from bs4 import BeautifulSoup
import pandas
import requests

def find_all_jobs():
    url = "https://www.indeed.com/jobs?q=job&l=United%20States"
    jobs_title = []
    companies_name = []
    locations = []
    jobs_link = []
    #Extract Data
    print("INDEED: Scraping all..")
    sum=0
    while sum<=10:
        print(str(sum*10) + "%")
        sum=sum+1
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('div', 'job_seen_beacon')
        
        links = soup.find_all('div', 'slider_container')
        for l in links:
            a = l.find_parent('a')
            full_link = 'https://www.indeed.com' + a['href']
            jobs_link.append(full_link)
        
        for job in jobs:
            job_title = job.find('div', attrs={'class': "heading4 color-text-primary singleLineTitle tapItem-gutter"})
            company_name = job.find('span', attrs={'class': "companyName"})
            location = job.find('div', attrs={'class': "companyLocation"})
            
            jobs_title.append(job_title.text.strip())
            companies_name.append(company_name.text.strip())
            locations.append(location.text.strip())
        
        try:
            url = 'https://www.indeed.com' + soup.find('a', {'aria-label': "Next"}).get('href')
        except AttributeError:
            break

    #Save result
    df = pandas.DataFrame({"Jobs title": jobs_title, "Company title": companies_name, "Locations": locations, "Apply Here": jobs_link})
    df.to_csv("./results/INDEED_A_Results.csv",index=False)
    print("INDEED: Finished scraping.")
    return df

def find_keyword_jobs(keyword):
    url = "https://www.indeed.com/jobs?q=" + keyword + "&l=United%20States"
    jobs_title = []
    companies_name = []
    locations = []
    jobs_link = []
    #Extract Data
    print("INDEED: Scraping by keyword..")
    sum=0
    while sum<=10:
        print(str(sum*10) + "%")
        sum=sum+1
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('div', 'job_seen_beacon')
        
        links = soup.find_all('div', 'slider_container')
        for l in links:
            a = l.find_parent('a')
            full_link = 'https://www.indeed.com' + a['href']
            jobs_link.append(full_link)
        
        for job in jobs:
            job_title = job.find('div', attrs={'class': "heading4 color-text-primary singleLineTitle tapItem-gutter"})
            company_name = job.find('span', attrs={'class': "companyName"})
            location = job.find('div', attrs={'class': "companyLocation"})
            
            jobs_title.append(job_title.text.strip())
            companies_name.append(company_name.text.strip())
            locations.append(location.text.strip())
        
        try:
            url = 'https://www.indeed.com' + soup.find('a', {'aria-label': "Next"}).get('href')
        except AttributeError:
            break

    #Save result
    df = pandas.DataFrame({"Jobs title": jobs_title, "Company title": companies_name, "Locations": locations, "Apply Here": jobs_link})
    df.to_csv("./results/INDEED_K_Results.csv",index=False)
    print("INDEED: Finished scraping.")
    return df
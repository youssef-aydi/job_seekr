import requests
import pandas
from bs4 import BeautifulSoup


def initialize():
    url = "https://realpython.github.io/fake-jobs/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    return results


def find_all_jobs():
    results = initialize()
    print("RPJ: Scraping all..")
    job_elements = results.find_all("div", class_="card-content")
    title_element = []
    company_element = []
    location_element = []
    time_element = []
    # link_element = []
    for job_element in job_elements:
        title_element.append(job_element.find("h2", class_="title").text.strip())
        company_element.append(job_element.find("h3", class_="company").text.strip())
        location_element.append(job_element.find("p", class_="location").text.strip())
        time_element.append(job_element.find("p", class_="is-small has-text-grey").text.strip())
        # link_element.append(job_element.find_all("a")[1]["href"])

    # df = pandas.DataFrame({'Job Title': title_element, 'Company Name': company_element,
                           #'Location': location_element, 'Posted on': time_element, 'Apply here': link_element})
    df = pandas.DataFrame({'Job Title': title_element, 'Company Name': company_element,
                           'Location': location_element, 'Posted on': time_element})
    df.to_csv("./results/RPJ_A_Results.csv",index=False)
    print("RPJ: Finished scraping.")
    return df


def find_keyword_jobs(keyword):
    results = initialize()
    print("RPJ: Scraping by keyword..")
    job_keyword = results.find_all(
        "h2", string=lambda text: keyword.lower() in text.lower()
    )
    job_keyword_elements = [
        h2_element.parent.parent.parent for h2_element in job_keyword
    ]
    title_element = []
    company_element = []
    location_element = []
    time_element = []
    # link_element = []
    for element in job_keyword_elements:
        title_element.append(element.find("h2", class_="title").text.strip())
        company_element.append(element.find("h3", class_="company").text.strip())
        location_element.append(element.find("p", class_="location").text.strip())
        time_element.append(element.find("p", class_="is-small has-text-grey").text.strip())
        # link_element.append(element.find_all("a")[1]["href"])

    # df = pandas.DataFrame({'Job Title': title_element, 'Company Name': company_element,
                           #'Location': location_element, 'Posted on': time_element, 'Apply here': link_element})
    df = pandas.DataFrame({'Job Title': title_element, 'Company Name': company_element,
                           'Location': location_element, 'Posted on': time_element})

    df.to_csv("./results/RPJ_K_Results.csv",index=False)
    print("RPJ: Finished scraping.")
    return df
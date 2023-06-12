import warnings
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup as soup

warnings.filterwarnings("ignore")

search = str(input("What type of job are you looking for?"))
location = str(input("What location do you want to search around?"))

monster_url = f'https://www.monsterindia.com/srp/results?sort=1&limit=100&query={search.replace(" ", "%20")}&locations={location.replace(" ", "+")}'
print(monster_url)

filename = f"{search} jobs in {location} by monstercom.csv"

with open(filename, "w", newline='') as myfile:
    writer = csv.writer(myfile)
    writer.writerow(["Job Title", "Company", "Location", "Salary", "Link"])

    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
    except:
        binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        options = Options()
        options.set_headless(headless=True)
        options.binary = binary
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True  # optional
        driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path="C:/Program Files/geckodriver-v0.33.0-win-aarch64")

    driver.get(monster_url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    src = driver.page_source
    driver.close()

    page_soup = soup(src, "lxml")
    containers = page_soup.findAll("div", {"class": "job-tittle"})
    print("Number of jobs =", len(containers))

    for container in containers:
        name_container1 = container.find("h3", {"class": "medium"})
        link_container = name_container1.find("a")
        link = link_container.get('href')[2:]
        job_title = link_container.text

        spanner = container.find("span", {"class": "company-name"})
        link_container = spanner.find("a")
        if link_container is None:
            company = spanner.text
        else:
            company = link_container.text

        location = str(container.find("span", {"class": "loc"}).text).strip()
        sal = container.findAll("span", {"class": "loc"})
        salary = sal[2].text

        writer.writerow([str(job_title), str(company.strip()), str(location), str(salary), f'=HYPERLINK("{str(link).strip()}")'])

# Open the CSV file using the default application
import os
os.startfile(filename)

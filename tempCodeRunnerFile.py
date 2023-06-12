import requests
import json
from bs4 import BeautifulSoup

def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Error getting HTML content")

def scrape_job_roles(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    job_roles = ['Finance']
    for article in soup.find_all("article", class_="job-card"):
        title = article.find("h2").text
        company = article.find("span", class_="company").text
        location = article.find("span", class_="location").text
        experience = article.find("span", class_="experience").text
        salary = article.find("span", class_="salary").text
        job_roles.append({
            "title": title,
            "company": company,
            "location": location,
            "experience": experience,
            "salary": salary
        })
    return job_roles

def save_job_roles(job_roles, filename):
    with open(filename, "w") as f:
        json.dump(job_roles, f, indent=4)

if __name__ == "__main__":
    url = "https://www.naukri.com/"
    html_content = get_html_content(url)
    job_roles = scrape_job_roles(html_content)
    save_job_roles(job_roles, "job_roles.json")
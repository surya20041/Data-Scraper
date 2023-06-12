from selenium import webdriver
from bs4 import BeautifulSoup

# Launch the browser
browser = webdriver.Chrome()

# Navigate to the web page
browser.get('https://www.naukri.com/presales-bd-jobs?k=presales%2C%20bd&nignbevent_src=jobsearchDeskGNB')

# Retrieve the page source
page_source = browser.page_source

# Use Beautiful Soup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Extract the desired data from the parsed HTML
data = soup.find('div', {'class': 'list'}).text

# Close the browser
browser.quit()

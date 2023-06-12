from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Specify the path to the saved HTML file
html_file_path = "C:/Users/surya/OneDrive/Documents/Programs/She values/naukari.html"

# Specify the name to search for
search_name = "Marketing"

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Load the HTML file
driver.get("file://" + html_file_path)

# Find the search box element and enter the search name
search_box = driver.find_element_by_name("Presales")
search_box.send_keys(search_name)
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
# You may need to adjust the wait time based on the website and your internet connection speed
driver.implicitly_wait(10)

# Get the search results
search_results = driver.find_elements_by_xpath("//div[@class='search-result']")

# Loop through the search results and print the text
for result in search_results:
    print(result.text)

# Close the browser window
driver.quit()

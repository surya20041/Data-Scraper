from bs4 import BeautifulSoup
import csv


with open("C:/Users/surya/OneDrive/Documents/Programs/She values/graduation.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")


links = soup.find_all("div",class_='graduation')

with open("C:/Users/surya/OneDrive/Documents/Programs/She values/graduation.csv", mode='w', newline='') as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)
    for tag in links:
        writer.writerow([tag.text])




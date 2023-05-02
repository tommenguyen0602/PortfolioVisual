import requests
response = requests.get('https://www.mql5.com/en/signals')


from bs4 import BeautifulSoup

soup = BeautifulSoup(response.content, 'html.parser')

links = []

for link in soup.find_all("span", class_ ="signal-card__copy") :
    links.append(link.get('data-id'))



import csv

with open('links.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Link'])
    for link in links:
        writer.writerow([link])
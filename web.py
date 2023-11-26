import requests
from bs4 import BeautifulSoup
import csv

tittles = []
authors = []
references = []
abstracts = []
# URL de la página de Apple Store
url = "https://openweathermap.org/city/4014338"
# Realizamos la solicitud GET a la página
response = requests.get(url)

# Parseamos el contenido HTML de la página con BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
# Buscamos la sección correspondiente al estado
paperList = soup.findAll("div", {"class": "daily-container block mobile-padding"})

print(paperList);

for paper in paperList:
    tittle = paper.find("a", {"class": "docsum-title"}).text.strip()
    # author = paper.find("span", {"class": "docsum-authors full-authors"}).text.strip()
    # reference = paper.find("span", {"class": "docsum-journal-citation full-journal-citation"}).text.strip()
    # abstract = paper.find("div", {"class": "full-view-snippet"}).text.strip()
    # writer.writerow([tittle, author, reference, abstract])

   



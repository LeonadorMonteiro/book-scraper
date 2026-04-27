import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titulos = soup.find_all("h3")
precios = soup.find_all("p", class_="price_color")
calificaciones = soup.find_all("p", class_="star-rating")

with open("books.csv", "w", newline="", encoding="utf-8") as f:  
    writer = csv.writer(f)  
    writer.writerow(["Title", "Price", "Rating"])
    
    for titulo, precio, calificacion in zip(titulos, precios, calificaciones):
        print(f"Title: {titulo.find('a').text}")
        print(f"Price: {precio.text}")
        print(f"Rating: {calificacion['class'][1]}")
        print("-" * 20)
        writer.writerow([titulo.find('a').text, precio.text, calificacion["class"][1]])
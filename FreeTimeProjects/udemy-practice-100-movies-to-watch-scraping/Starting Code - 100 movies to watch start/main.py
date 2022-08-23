import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movies = soup.find_all(name="h3", class_="title")

with open(file="movies.txt", mode="w") as file:
    for i in movies[::-1]:
        file.write(f"{i.text}\n")


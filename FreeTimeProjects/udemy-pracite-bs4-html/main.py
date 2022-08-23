from bs4 import BeautifulSoup
import requests

# this practice wont work because the website has changed some tags and classes.
# and im not bothered to even find out what those tags are :)
response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_num = max(article_upvotes)
max_index = article_upvotes.index(max_num)

print(article_texts)
print(article_links)
print(article_upvotes)

# with open(file="website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchors = soup.find_all(name="a")
#
# for tag in all_anchors:
#     # print(tag.getText())
#     print(tag.get("href"))
#



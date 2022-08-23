from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)

    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<userinput>")
def guess(userinput):
    params = {
        "name": userinput
    }
    age_response = requests.get("https://api.agify.io", params=params)
    gender_response = requests.get("https://api.genderize.io", params=params)

    age_data = age_response.json()
    gender_data = gender_response.json()

    return render_template("guess.html", age=age_data["age"], gender=gender_data["gender"], name=userinput)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

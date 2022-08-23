from flask import Flask, render_template
import requests

app = Flask(__name__)



@app.route("/")
def start():
    response = requests.request(method="GET", url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("index.html", all_post=all_posts)


@app.route("/index.html")
def home_page():
    response = requests.request(method="GET", url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("index.html", all_post=all_posts)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:id>")
def get_post(id):
    response = requests.request(method="GET", url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    title = None
    body = None
    subtitle = None
    for i in all_posts:
        if i["id"] == id:
            body = i["body"]
            title = i["title"]
            subtitle = i["subtitle"]
    return render_template("post.html", id=id, post_title=title, post_body=body, post_subtitle=subtitle)


if __name__ == "__main__":
    app.run(debug=True)

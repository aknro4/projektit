from flask import Flask
app = Flask(__name__)


def make_bold(func):
    def bold():
        return f"<b>{func()}</b>"
    return bold


@app.route('/')
@make_bold
def hello_world():
    return '<h1>Hello, World!<h1>'


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number}, years old"


if __name__ == "__main__":
    app.run(debug=True)

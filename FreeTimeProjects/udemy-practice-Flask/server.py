from flask import Flask
app = Flask(__name__)


def title(func):
    def wrapper(userinput):
        title = "<h1>Guess number between 0 and 9</h1>"
        if userinput <= 4:
            return f"{title} " \
                   f"Too low"
        if userinput >= 6:
            return f"{title}" \
                   f"Too high"
        if userinput == 5:
            return f"{title}" \
                   f"Correct"
        func()

    return wrapper

@app.route("/")
def guess_number():
    return "<h1>Guess number between 0 and 9</h1>"


@app.route("/<int:userinput>")
@title
def user_guess(userinput):
    return userinput


if __name__ == "__main__":
    app.run(debug=True)


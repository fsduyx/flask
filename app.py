from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# логин и пароль для проверки
USERS = {"admin": "123456"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            username = request.form["username"]
            password = request.form["password"]

            if username == "" or password == "":
                return render_template("index.html", error="Заполните все поля")

            if USERS.get(username) == password:
                return redirect(url_for("login_page"))
            else:
                return render_template("index.html", error="Неверное имя пользователя или пароль")
        except Exception as e:
            print(e)
            return render_template("index.html", error="Произошла ошибка")

    return render_template("index.html")


@app.route("/login_page")
def login_page():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)

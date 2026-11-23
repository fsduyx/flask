from flask import Flask, render_template, request, redirect, url_for
from database import Database

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db = None
        try:
            username = request.form["username"]
            password = request.form["password"]

            if username == "" or password == "":
                return render_template("index.html", error="Заполните все поля")

            db = Database()
            user = db.get_user(username)

            if user is not None and user["user_password"] == password:
                return redirect(url_for("login_page"))
            else:
                return render_template("index.html", error="Неверное имя пользователя или пароль")
        except Exception as e:
            print(e)
            return render_template("index.html", error="Ошибка подключения к базе данных")
        finally:
            if db is not None:
                db.close()

    return render_template("index.html")


@app.route("/login_page")
def login_page():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)

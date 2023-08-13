import sqlite3

from flask import Flask, render_template_string, request

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("users.sqlite")
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
        )
        cursor.execute(
            "INSERT OR IGNORE INTO users (username, password) VALUES ('admin', '123')"
        )
        conn.commit()


@app.route("/")
def login():
    return render_template_string(
        """
    <form method="post" action="/authenticate">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
        """
    )


@app.route("/authenticate", methods=["POST"])
def authenticate():
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("users.sqlite")
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?", (username, password)
        )
        user = cursor.fetchone()

    if user:
        return "Logged in succesfully!"
    else:
        return "Login failed!"


if __name__ == "__main__":
    init_db()
    app.run()

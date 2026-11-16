from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, PaaS! Лабораторная работа №2. Студент: Калинин Д.В., группа Бз-ИСиТ-41"


if __name__ == "__main__":
    app.run()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("synthetic tester")

db = SQLAlchemy(app)


@app.get("/")
def main():
    return "asd"
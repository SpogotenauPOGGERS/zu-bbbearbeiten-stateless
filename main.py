import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    todos = helper.get_all()
    return render_template('index.html', todos=todos)  # frage 3

@app.route('/add', methods=["POST"])
def add():
    title = request.form.get("title")
    helper.add(title)                        #frage 2
    return redirect(url_for("index"))

@app.route('/update/<int:index>') #frage 4
def update(index):
    helper.update(index)
    return redirect(url_for("index"))

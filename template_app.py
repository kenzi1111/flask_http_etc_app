from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    # return "Hello from index"
    # index.htmlをレンダリングする
    return render_template("index.html")
@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html",name = name)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "My Flask App"

if __name__ == "__main__":
    app.run()

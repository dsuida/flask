from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "My Flask App"

if __name__ == "__main__":
    #  app.run(host='127.0.0.1', port=5600, debug=False)
    app.run()

#  test
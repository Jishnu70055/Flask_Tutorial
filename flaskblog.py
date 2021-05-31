from flask import Flask  #importing Flask class
app = Flask(__name__)   


@app.route("/")
@app.route("/home")
def home():
    return "Hiiisfddfsf"


@app.route("/about")
def about():
    return "about"


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template


app = Flask(__name__)

#criar página

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/users/<user_name>")
def users(user_name):
    return render_template("users.html",
                           user_name=user_name)

#colocar no ar
if __name__ == "__main__":
    app.run(debug=True)
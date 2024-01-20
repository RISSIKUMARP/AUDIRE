from flask import Flask,render_template,request,flash

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def login():
    return render_template("login.html")

@app.route("/signup", methods=['GET','POST'])
def signup():
    return render_template("signup.html")

@app.route("/otp", methods=['GET','POST'])
def otp():
    return render_template("otp.html")

@app.route("/home", methods=['GET','POST'])
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
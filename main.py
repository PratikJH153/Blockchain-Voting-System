from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/login_data', methods=['POST'])
def login_data():
    email = request.form['email']
    password = request.form['password']

    print(email)
    print(password)

    return "Signed in succesfully!"


@app.route("/register")
def register():
    return render_template("register.html")


@app.route('/register_data', methods=['POST'])
def register_data():
    email = request.form['email']
    password = request.form['password']

    print(email)
    print(password)

    return "Signed up succesfully!"


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)

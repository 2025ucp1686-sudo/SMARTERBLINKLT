from flask import Flask, render_template, request
from capture_face import capture_face
from face_login import recognize_face

app = Flask(__name__)


# HOME
@app.route("/")
def home():
    return render_template("index.html")


# LOGIN PAGE
@app.route("/login")
def login():
    return render_template("login.html")


# BUYER LOGIN
@app.route("/buyer_login")
def buyer_login_page():
    return render_template("buyer_login.html")


# SELLER LOGIN
@app.route("/seller_login")
def seller_login_page():
    return render_template("seller_login.html")


# SIGNUP
@app.route("/signup", methods=["GET","POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        mobile = request.form["mobile"]
        password = request.form["password"]

        capture_face(name)

        return "Signup successful!"

    return render_template("signup.html")


@app.route("/signup_face")
def signup_face():

    name = "temp_user"

    from capture_face import capture_face
    capture_face(name)

    return "Face captured successfully!"


# SAVE ADDRESS
@app.route("/saveaddress", methods=["GET", "POST"])
def saveaddress():

    if request.method == "POST":

        home = request.form["home"]
        area = request.form["area"]
        city = request.form["city"]
        nearby = request.form["nearby"]
        pincode = request.form["pincode"]

        print(home, area, city, nearby, pincode)

        return "Address Saved"

    return render_template("saveaddress.html")


# FACE LOGIN  ✅ MOVE HERE
@app.route("/face_login")
def face_login():

    user = recognize_face()

    if user:
        return f"Welcome {user}"
    else:
        return "Face not recognized"


if __name__ == "__main__":
    app.run(debug=True)
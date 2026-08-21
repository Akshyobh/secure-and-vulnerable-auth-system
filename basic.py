import mysql.connector, re
from flask import Flask, redirect, render_template, request, session, url_for, flash, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_limiter.errors import RateLimitExceeded
app = Flask(__name__)
app.secret_key = "mysecretkey"
limiter = Limiter(key_func=get_remote_address,app=app,default_limits=[])
db = mysql.connector.connect(host="YOUR_HOST",user="YOUR_USERNAME",password="YOUR_PASSWORD",database="YOUR_DATABASE")
cursor = db.cursor()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        username = request.form["username"]
        password = request.form["password"]

        email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        if not re.fullmatch(r"[A-Za-z ]{2,50}", name):
            return render_template("register.html",error="Name should contain only letters and spaces.")
        if not re.fullmatch(email_pattern, email):
            return render_template("register.html",error="Invalid email address.")
        if not re.fullmatch(r"\d{10}", phone):
            return render_template("register.html",error="Phone number must contain exactly 10 digits.")
        if not re.fullmatch(r"[A-Za-z0-9_]{4,20}", username):
            return render_template("register.html",error="Username must be 4-20 characters.")
        if not re.search(r"[A-Z]", password):
            return render_template("register.html",error="Password must contain an uppercase letter.")
        if not re.search(r"[a-z]", password):
            return render_template("register.html",error="Password must contain a lowercase letter.")
        if not re.search(r"\d", password):
            return render_template("register.html",error="Password must contain a number.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return render_template("register.html",error="Password must contain a special character.")
        if len(password) < 8:
            return render_template("register.html",error="Password must be at least 8 characters.")
        
        cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            return render_template("register.html",error="Username already exists. Please choose another username.")
        
        hashed_password = generate_password_hash(password)
        cursor.execute("INSERT INTO users (name,email,phone,username,password) VALUES(%s,%s,%s,%s,%s)",
                       (name, email, phone, username, hashed_password))
        db.commit()
        return render_template("register.html",success="User Registered Successfully")
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cursor.execute("SELECT * FROM users WHERE username=%s",(username,))
        user = cursor.fetchone()
        if user and check_password_hash(user[5], password):
            session["user_id"] = user[0]
            session["name"] = user[1]
            return render_template("login.html", success="Logged in Successfully")
        else:
            return render_template("login.html", error="Invalid Username or Password"),401

    return render_template("login.html")

@app.errorhandler(RateLimitExceeded)
def handle_rate_limit(e):
    return render_template(
        "login.html",
        error="Too many login attempts. Please try again after 1 minute."
    ), 429

@app.route("/welcome")
def welcome():
    if "user_id" not in session:
        flash("Access denied. Please log in to continue.", "warning")
        return redirect(url_for("login"))
                        
    return render_template("welcome.html",name=session["name"])

@app.route("/form", methods=["GET", "POST"])
def form():
    if "user_id" not in session:
        flash("Access denied. Please log in to continue.", "warning")
        return redirect(url_for("login"))
    
    if request.method == "POST":
        user_id = session["user_id"]
        name = request.form["name"]
        dob = request.form["dob"]
        email = request.form["email"]
        phone = request.form["phone"]
        gender = request.form["gender"]
        address = request.form["address"]
        doj = request.form["doj"]
        doc = request.form["doc"]
        institute = request.form["institute"]
        branch = request.form["branch"]
        cgpa = request.form["cgpa"]
        email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if not re.fullmatch(r"[A-Za-z ]{2,50}", name):
            return render_template("form.html",error="Invalid name.")
        if not re.fullmatch(email_pattern, email):
            return render_template("form.html",error="Invalid email.")
        if not re.fullmatch(r"\d{10}", phone):
            return render_template("form.html",error="Phone must contain exactly 10 digits.")
        if gender not in ["Male","Female","Other"]:
            return render_template("form.html",error="Invalid gender.")
        try:
            cgpa = float(cgpa)
            if cgpa < 0 or cgpa > 10:
                return render_template("form.html",error="CGPA must be between 0 and 10.")
        except:
            return render_template("form.html",error="Invalid CGPA.")
        cursor.execute("UPDATE users SET name=%s WHERE id=%s",(name, user_id))
        session["name"] = name
        cursor.execute("SELECT * FROM form WHERE id=%s",(user_id,))
        existing_form = cursor.fetchone()
        if existing_form:
            cursor.execute("""UPDATE form SET name=%s,dob=%s,email=%s,phone=%s,gender=%s,address=%s,doj=%s,doc=%s,institute_name=%s,branch=%s,cgpa=%s
                WHERE id=%s""",(name,dob,email,phone,gender,address,doj,doc,institute,branch,cgpa,user_id))
        else:
            cursor.execute("""INSERT INTO form(id,name,dob,email,phone,gender,address,doj,doc,institute_name,branch,cgpa)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user_id,name,dob,email,phone,gender,address,doj,doc,institute,branch,cgpa))
        db.commit()
        cursor.execute("SELECT * FROM form WHERE id=%s",(user_id,))
        form_data = cursor.fetchone()
        print(form_data)
        return render_template("form.html",success="Form Submitted Successfully",form_data=form_data,user_data=None)
    
    cursor.execute("SELECT * FROM form WHERE id=%s", (session["user_id"],))
    form_data = cursor.fetchone()
    user_data = None
    if not form_data:
        cursor.execute("SELECT name, email, phone FROM users WHERE id=%s",(session["user_id"],))
        user_data = cursor.fetchone()
    return render_template("form.html",form_data=form_data,user_data=user_data)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(port=5000)
import mysql.connector
from flask import Flask, redirect, render_template, request, session, url_for
app = Flask(__name__)
app.secret_key = "mysecretkey"
db = mysql.connector.connect(host="YOUR_HOST",user="YOUR_USERNAME",password="YOUR_PASSWORD",database="YOUR_DATABASE")
cursor = db.cursor(buffered=True)

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
        cursor.execute(
            "INSERT INTO vul_users (name, email, phone, username, password) VALUES ('"
            + name + "','"
            + email + "','"
            + phone + "','"
            + username + "','"
            + password + "')"
        )        
        db.commit()
        return render_template("vul_register.html",success="User Registered Successfully")
    
    return render_template("vul_register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        sqli_detected = False
        payloads = [
            "'",
            "--",
            "#",
            "/*",
            "*/",
            " or ",
            " and ",
            " union ",
            " select ",
            " drop ",
            " insert ",
            " update ",
            " delete "
        ]
        text = (username + " " + password).lower()
        if any(payload in text for payload in payloads):
            sqli_detected = True
    
        query = (
            "SELECT * FROM vul_users WHERE username='"
            + username +
            "' AND password='"
            + password + "'"
        )

        print("\n========================")
        print(query)
        print("========================\n")

        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            session["user_id"] = user[0]
            session["name"] = user[1]
            session["sqli_detected"] = sqli_detected
            return render_template("login.html",success="Logged in Successfully")
        else:
            return render_template("login.html",error="Invalid Username or Password"), 401

    return render_template("login.html")

@app.route("/welcome")
def welcome():
    sqli_detected = session.pop("sqli_detected", False)
    return render_template("welcome.html",name=session.get("name"), sqli_detected=sqli_detected)

@app.route("/form", methods=["GET", "POST"])
def form():
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
        cursor.execute(
            "UPDATE vul_users SET name='"
            + name +
            "' WHERE id='"
            + str(user_id) + "'"
        )
        session["name"] = name
        cursor.execute(
            "SELECT * FROM vul_form WHERE id='"
            + str(user_id) + "'"
        )
        existing_form = cursor.fetchone()
        if existing_form:
            query = f"""
            UPDATE vul_form SET
                name='{name}',
                dob='{dob}',
                email='{email}',
                phone='{phone}',
                gender='{gender}',
                address='{address}',
                doj='{doj}',
                doc='{doc}',
                institute_name='{institute}',
                branch='{branch}',
                cgpa='{cgpa}'
            WHERE id='{user_id}'
            """                        
        else:
            query = f"""
            INSERT INTO vul_form
            (
                id,
                name,
                dob,
                email,
                phone,
                gender,
                address,
                doj,
                doc,
                institute_name,
                branch,
                cgpa
            )
            VALUES
            (
                '{user_id}',
                '{name}',
                '{dob}',
                '{email}',
                '{phone}',
                '{gender}',
                '{address}',
                '{doj}',
                '{doc}',
                '{institute}',
                '{branch}',
                '{cgpa}'
            )
            """
        cursor.execute(query)
        db.commit()
        cursor.execute("SELECT * FROM vul_form WHERE id='" + str(user_id) + "'")
        form_data = cursor.fetchone()
        return render_template("vul_form.html",success="Form Submitted Successfully",form_data=form_data,user_data=None)

    cursor.execute("SELECT * FROM vul_form WHERE id='" + str(session["user_id"]) + "'")
    form_data = cursor.fetchone()
    user_data = None
    if not form_data:
        cursor.execute("SELECT name, email, phone FROM vul_users WHERE id='" + str(session["user_id"]) + "'")
        user_data = cursor.fetchone()
    return render_template("vul_form.html",form_data=form_data,user_data=user_data)

@app.route("/logout")
def logout():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
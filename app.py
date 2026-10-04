import os
import hmac
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or os.urandom(32)
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "purna010")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "Vamsi@010")
appointments = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            appointment = {
                "name": request.form["name"].strip(),
                "age": int(request.form["age"]),
                "gender": request.form["gender"].strip(),
                "doctor": request.form["doctor"].strip(),
                "date": datetime.strptime(
                    request.form["appointmentdate"], "%Y-%m-%d"
                ).strftime("%b %d, %Y"),
                "time": datetime.strptime(
                    request.form["appointmenttime"], "%H:%M"
                ).strftime("%I:%M %p"),
                "phone": request.form["tele"].strip(),
                "country_code": request.form["countryCode"].strip(),
                "reason": request.form["reason"].strip(),
            }
            appointments.append(appointment)
        except (KeyError, ValueError):
            flash("Please check the appointment details and submit again.", "error")
        else:
            flash(
                "Your appointment is booked. Remember to attend at the scheduled date and time.",
                "success",
            )
        return redirect(url_for("home"))

    return render_template("index.html")


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if hmac.compare_digest(username, ADMIN_USERNAME) and hmac.compare_digest(
            password, ADMIN_PASSWORD
        ):
            session["is_admin"] = True
            return redirect(url_for("admin_appointments"))
        flash("Incorrect username or password.", "error")

    return render_template("admin_login.html")


@app.route("/admin/appointments")
def admin_appointments():
    if not session.get("is_admin"):
        return redirect(url_for("admin_login"))
    return render_template("appointments.html", appointments=appointments)


@app.route("/admin/logout", methods=["POST"])
def admin_logout():
    session.pop("is_admin", None)
    return redirect(url_for("home"))


if __name__=="__main__":
    app.run(debug=True)
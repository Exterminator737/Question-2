from flask import Flask, render_template, redirect, url_for, request, flash
from forms import RegisterForm, UpdateForm
from database import init_db, add_user, get_user, update_user
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or "your_default_secret_key"

init_db()

@app.route("/")
def home():
    return redirect(url_for("register"))

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    existing_user = get_user()

    if form.validate_on_submit():
        if existing_user["name"]:
            flash("Warning: Registering will replace the existing user!", "warning")
        user_data = {
            "name": form.name.data,
            "email": form.email.data,
            "age": form.age.data
        }
        add_user(user_data)
        flash("User registered successfully!", "success")
        return redirect(url_for("profile"))

    return render_template("register.html", form=form)

@app.route("/profile")
def profile():
    user = get_user()
    return render_template("profile.html", user=user)

@app.route("/update", methods=["GET", "POST"])
def update():
    user = get_user()
    form = UpdateForm()

    if request.method == "GET":
        form.name.data = user.get("name")
        form.email.data = user.get("email")
        form.age.data = user.get("age")

    if form.validate_on_submit():
        updated_fields = {}
        if form.name.data != user.get("name"):
            updated_fields["name"] = form.name.data
        if form.email.data != user.get("email"):
            updated_fields["email"] = form.email.data
        if form.age.data != user.get("age"):
            updated_fields["age"] = form.age.data

        if updated_fields:
            update_user(updated_fields)
            flash("Profile updated successfully!", "success")
        else:
            flash("No changes detected.", "warning")

        return redirect(url_for("profile"))

    return render_template("update.html", form=form)
    
if __name__ == "__main__":
    app.run(debug=True)

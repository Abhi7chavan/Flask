from flask import render_template, request, redirect, url_for, flash, session
from flask.views import MethodView

class LoginController(MethodView):
    def get(self):
        return render_template("login.html")
    
    def post(self):
        username = request.form.get('email')
        password = request.form.get('password')

        if username == "abhishekchavan7ac@gmail.com" and password == "admin":  # Replace with DB check
            session["user"] = username  # Store user session
            return redirect(url_for("/"))  # Redirect to homepage

        flash("Invalid email or password", "error")  # Flash an error message
        return render_template("login.html")

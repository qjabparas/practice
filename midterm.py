import requests
from flask import Flask, request, redirect, url_for, render_template
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_envvar("ENV_FILE_LOCATION")
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

token = ''

app.config["MONGODB_SETTINGS"] = {
    "host": "mongodb://localhost/paras"
}
initialize_db(app)
initialize_routes(api)

@app.route("/")
def main():
    return render_template("login.html")

""" AUTHENTICATION ROUTES """
@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        creds = {"email": email, "password": password}
        response = requests.post(url="http://127.0.0.1:8080/api/auth/login",json=creds)
        if response.status_code == 200:
            token = response.json().get('token')
            return render_template("home.html")
        else:
            return "Invalid credentials"

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        creds = {"email": email, "password": password}
        response = requests.post(url="http://127.0.0.1:8080/api/auth/signup",json=creds)
        if response.status_code == 200:
            return render_template("login.html")
        else:
            return "Invalid credentials"
            return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
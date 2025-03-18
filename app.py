from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# init Firebase
cred = credentials.Certificate("vespera-db-key.json")  # Use your downloaded JSON file
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        phone = request.form["phone"]
        email = request.form["email"]

        # Save to db
        db.collection("users").add({
            "name": name,
            "address": address,
            "phone": phone,
            "email": email
        })

        return redirect(url_for("success"))

    return render_template("index.html")

@app.route("/success")
def success():
    return "<h2>Thank you! Your details have been saved.</h2>"

if __name__ == "__main__":
    app.run(debug=True)
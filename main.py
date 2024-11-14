from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("Home.html")

@app.route("/update_rating", methods=["GET", "POST"])
def update_rating():
    """Allows a user to update a location's accessibility rating"""
    
    if request.method == "POST":
        print("posted")
    return render_template("UpdateRating.html")
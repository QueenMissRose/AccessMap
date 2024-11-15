import os
import json
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    url_for,
    request,
    send_from_directory,
    make_response)

from add_records import add_new_rating_to_db
import add_gsheets
from models import Locations

# Configure application
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("Home.html")


@app.route("/update_rating", methods=["GET", "POST"])
def update_rating():
    """Allows a user to update a location's accessibility rating"""

    if request.method == "POST":
        # Get form information from the user
        location_name = request.form.get("location_name")
        address = request.form.get("location_address")
        sensory_rating = request.form.get("sensoryrating")
        mobility_rating = request.form.get("mobilityrating")
        service_dog_relief_rating = request.form.get("sdogreliefrating")
        wheelchair_rating = request.form.get("wheelchairrating")
        common_allergens_rating = request.form.get("commonallergens")

        new_rec = Locations(Name=location_name, Address=address, SensoryRating=sensory_rating,
                            MobilityRating=mobility_rating,
                            ServiceDogRelief=service_dog_relief_rating, WheelchairAccessible=wheelchair_rating,
                            CommonAllergenRisk=common_allergens_rating)

        add_new_rating_to_db(new_rec)

        # Flask won't let me call both functions and update both places
        add_gsheets.write_to_gsheet()

    return render_template("UpdateRating.html")


# TODO: Get what the user input for the location name
# TODO: Find similar location names to what the user input using database query (SQL, CS50, or ORM)
# TODO: Make a dropdown with similar location names
# TODO: Index dropdown with actual location
# TODO: Edit the row that matches the unique location ID only

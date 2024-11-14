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

# Configure application
app = Flask(__name__)

# ------------------- Google Sheets API Setup ------------------- #

import gspread

from oauth2client.service_account import ServiceAccountCredentials

# Use credentials to create a client to interact with the Google Drive API
# scope = ["https://spreadsheets.google.com/feeds"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name(
#     "client_secret.json", scope)
# client = gspread.authorize(credentials)

# # Find a workbook by name and open the first sheet
# sheet = client.open("LocationsAccessMap").sheet2

# print(sheet.get_all_values())


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("Home.html")

@app.route("/find_location", methods=["GET", "POST"])
def find_a_location():
    """Allows a user to search for a location by name or address"""
    return render_template("FindLocation.html")

@app.route("/update_rating", methods=["GET", "POST"])
def update_rating():
    """Allows a user to update a location's accessibility rating"""
    
    if request.method == "POST":
        print("posted")
        
        # Get form information from the user
        location_name = request.form.get("location_name")
        address = request.form.get("location_address")
        sensory_rating = request.form.get("sensoryrating")
        mobility_rating = request.form.get("mobilityrating")
        service_dog_relief_rating = request.form.get("sdogreliefrating")
        wheelchair_rating = request.form.get("wheelchairrating")
        common_allergens_rating = request.form.get("commonallergens")
        
        # Check information
        print(f"Location Name: {location_name}",
              f"Address: {address}",
              f"Sensory Rating: {sensory_rating}",
              f"Mobility Rating: {mobility_rating}",
              f"Service Dog Relief Rating: {service_dog_relief_rating}",
              f"Wheelchair Rating: {wheelchair_rating}",
              f"Common Allergens Rating: {common_allergens_rating}")
        
    return render_template("UpdateRating.html")

# TODO: Get what the user input for the location name
# TODO: Find similar location names to what the user input using database query (SQL, CS50, or ORM)
# TODO: Make a dropdown with similar location names
    # TODO: Index dropdown with actual location 
# TODO: Edit the row that matches the unique location ID only
    
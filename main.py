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

# # Use credentials to create a client to interact with the Google Drive API
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

    if request.method == "POST":
        print("Looking for location")

        # Get form information from the user
        location_name = request.form.get("location_name")
        address = request.form.get("location_address")
        
        print(f"Location Name: {location_name}",
        f"Address: {address}")
        print(f"Location Name: {type(location_name)}",
        f"Address: {(address)}")

        if not location_name and not address:
            # TODO: User must choose either a location or an address in order to update
            # a location's accessibility rating
            print(f"Location Name: {location_name}",
                  f"Address: {address}")
            
            print("Please add either a location or an address to search for.")
        else:
            print("Either a location name or an address has been added!")
            
            # TODO: If the user searches by location name and not address:
                # TODO: Get what the user input for the location name
                # TODO: Find similar location names to what the user input using database query (SQL, CS50, or ORM)
                # TODO: Make a dropdown with similar location names
            # TODO: If the user searches by an address
                # TODO: Get the index of the location that matches the exact address
                # TODO: OR if there are multiple addressses that match the query
                    # TODO: Find similar addresses to what the user is searching for
                    # TODO: Make a dropdown with similar location addresses
            
            # TODO: Index the address or name that matches the unique dropdown ID
            
            # TODO: Edit the row that matches the unique location ID only
            
            # TODO: Redirect to update_rating if successful
            return redirect(url_for("update_rating"))

    return render_template("FindLocation.html")

@app.route("/update_rating", methods=["GET", "POST"])
def update_rating():
    """Allows a user to update a location's accessibility rating"""
    
    if request.method == "POST":
        print("posted")
        
        # Get form information from the user
        sensory_rating = request.form.get("sensoryrating")
        mobility_rating = request.form.get("mobilityrating")
        service_dog_relief_rating = request.form.get("sdogreliefrating")
        wheelchair_rating = request.form.get("wheelchairrating")
        common_allergens_rating = request.form.get("commonallergens")
        
        # Check information
        print(f"Sensory Rating: {sensory_rating}",
              f"Mobility Rating: {mobility_rating}",
              f"Service Dog Relief Rating: {service_dog_relief_rating}",
              f"Wheelchair Rating: {wheelchair_rating}",
              f"Common Allergens Rating: {common_allergens_rating}")
        
        if not sensory_rating and not mobility_rating and not service_dog_relief_rating \
            and not wheelchair_rating and not common_allergens_rating:
                # TODO: The user must choose to update either a sensory, mobility, service dog relief,
                # wheelchair, or common allergens rating 
                print("Please add a category rating.")
                
        else:
            # If the user puts an accessibility rating in, update database
            print("A category's rating has been updated!")
            
            # TODO: Use new rating to recalculate a location's average accessibility score
            ## for that category
            
            # TODO: Insert the new average into the database
            
            # TODO: Display new average on the success page
            
            # Redirect to the success page if successful
            return redirect(url_for("successfully_posted"))
        
    return render_template("UpdateRating.html")

@app.route("/success", methods=["GET"])
def successfully_posted():
    """Informs the user they have successfully updated the rating"""
    
    return render_template("SuccessfullyUpdated.html")

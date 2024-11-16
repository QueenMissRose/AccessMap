import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from scores import query_sensory_rating_sql, query_mobility_rating_sql, query_service_dog_relief_rating_sql, \
    query_wheelchair_accessible_rating_sql, query_allergen_risk_rating_sql

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# SPREADSHEET_ID = "1O01Exonl72cF3G5ZYZzYgYJ55ObHaqrp0dXCHeZ4L-E"

SPREADSHEET_ID = "1RctGomuhioyOC47IUoDBONAsKKKVUqMvTyTAimvtcLA"


def write_agg_scores_to_gsheets():
    
    # Authorizes editing of the spreadsheet
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        # Range reduced temporarily for API usage constraints
        for row in range(2, 50):

            # Gets all location data
            location_lookup = \
                sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"Sheet2!A{row}").execute().get("values")[0][0]

            # Calculates the average sensory rating
            avg_sensory_rating = query_sensory_rating_sql()
            for tuple in avg_sensory_rating:
                if tuple[0] == location_lookup:
                    print(f'Found {tuple[0]} Writing {tuple[1]} to gsheets')
                    
                    # Writes the aggregate score onto the sheet
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet2!C{row}",
                                           valueInputOption="USER_ENTERED",
                                           body={"values": [[f"{tuple[1]}"]]}).execute()

            # Calculates the average mobility rating
            avg_mobility_rating = query_mobility_rating_sql()
            for tuple in avg_mobility_rating:
                if tuple[0] == location_lookup:
                    print(f'Found {tuple[0]} Writing {tuple[1]} to gsheets')
                    
                    # Writes the aggregate score onto the sheet
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet2!D{row}",
                                           valueInputOption="USER_ENTERED",
                                           body={"values": [[f"{tuple[1]}"]]}).execute()

            # Calculates the average service drog relief rating
            avg_service_dog_relief_rating = query_service_dog_relief_rating_sql()
            for tuple in avg_service_dog_relief_rating:
                if tuple[0] == location_lookup:
                    print(f'Found {tuple[0]} Writing {tuple[1]} to gsheets')
                    
                    # Writes the aggregate score onto the sheet
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet2!E{row}",
                                           valueInputOption="USER_ENTERED",
                                           body={"values": [[f"{tuple[1]}"]]}).execute()

            # Calculates the average wheelchair mobility rating
            avg_wheelchair_accessible_rating = query_wheelchair_accessible_rating_sql()
            for tuple in avg_wheelchair_accessible_rating:
                if tuple[0] == location_lookup:
                    print(f'Found {tuple[0]} Writing {tuple[1]} to gsheets')
                    
                    # Writes the aggregate score onto the sheet
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet2!F{row}",
                                           valueInputOption="USER_ENTERED",
                                           body={"values": [[f"{tuple[1]}"]]}).execute()

            # Calculates the average allergen rating
            avg_allergen_risk_rating = query_allergen_risk_rating_sql()
            for tuple in avg_allergen_risk_rating:
                if tuple[0] == location_lookup:
                    print(f'Found {tuple[0]} Writing {tuple[1]} to gsheets')
                    
                    # Writes the aggregate score onto the sheet
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet2!G{row}",
                                           valueInputOption="USER_ENTERED",
                                           body={"values": [[f"{tuple[1]}"]]}).execute()


    except HttpError as error:
        print(error)

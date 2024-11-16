import sqlite3
import gspread
from add_records import add_new_rating_to_db

gc = gspread.service_account(filename='accessmap-441715-705d96e6c09e.json')

sh = gc.open_by_key("1O01Exonl72cF3G5ZYZzYgYJ55ObHaqrp0dXCHeZ4L-E")

worksheet = sh.worksheet("Sheet2")


def query_sql():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = 'select * from ratings'
    cursor.execute(sql)
    return cursor.fetchall()


def write_to_gsheet():
    # Finds everything from ratings table in the database
    results = query_sql()
    
    # For everything in results
    for i in results:
        
        location_name = i[1]
        address = i[2]
        
        # Get the new location name and addresses
        values = [location_name, address]

        # If there are any missing location names, add it to the sheet
        if not worksheet.findall(i[1]):
            worksheet.append_row(values)


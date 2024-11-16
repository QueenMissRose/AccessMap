import sqlite3

import gspread

gc = gspread.service_account(filename='accessmap-441715-705d96e6c09e.json')

sh = gc.open_by_key("1O01Exonl72cF3G5ZYZzYgYJ55ObHaqrp0dXCHeZ4L-E")

# TODO: Fix update location rating
def update_location_rating(location_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = (f'UPDATE ratings SET ')
    print(sql)
    cursor.execute(sql)
    return cursor.fetchall()


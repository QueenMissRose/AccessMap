import sqlite3

import gspread

gc = gspread.service_account(filename='accessmap-441715-705d96e6c09e.json')

sh = gc.open_by_key("1O01Exonl72cF3G5ZYZzYgYJ55ObHaqrp0dXCHeZ4L-E")

def query_find_by_location_name(location):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = (f'SELECT * FROM ratings WHERE Name LIKE "%{location}%"')
    print(sql)
    cursor.execute(sql)
    return cursor.fetchall()

def query_find_by_address(address):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = (f'SELECT * FROM ratings WHERE Address LIKE "%{address}%"')
    print(sql)
    cursor.execute(sql)
    return cursor.fetchall()


import sqlite3
import gspread
from add_records import add_new_rating_to_db

gc = gspread.service_account(filename='/Users/mermaid/PycharmProjects/AccessMap/accessmap-441715-705d96e6c09e.json')

sh = gc.open_by_key("1O01Exonl72cF3G5ZYZzYgYJ55ObHaqrp0dXCHeZ4L-E")

# print(sh.sheet1.get('A2:A1000'))

worksheet = sh.worksheet("Sheet2")


def query_sql():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = 'select * from ratings'
    cursor.execute(sql)
    return cursor.fetchall()


def write_to_gsheet():
    results = query_sql()
    for i in results:
        if i[0] != sh.sheet1.get('A2:A1000'):
            worksheet.append_row(i)

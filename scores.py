import sqlite3

import gspread

<<<<<<< HEAD
gc = gspread.service_account(filename='accessmap-441715-705d96e6c09e.json')
=======
gc = gspread.service_account(filename='/Users/mermaid/PycharmProjects/AccessMap/accessmap-441715-705d96e6c09e.json')
>>>>>>> 54ba336cc04df86805f7e315035a835b24045f79

sh = gc.open_by_key("1O01Exonl72cF3G5ZYZzYgYJ55ObHaqrp0dXCHeZ4L-E")



# print(sh.sheet1.get('A2:A1000'))

# worksheet = sh.worksheet("Sheet2")
#
# cell = worksheet.find("Chicago Yacht Club")
# print("Found something at R%sC%s" % (cell.row, cell.col))
#
# lookup_function = worksheet.findall('11', in_column=1)
# print(lookup_function)
#
# lookup_name = worksheet.find("Chicago Yacht Club", in_column=2)

def query_sensory_rating_sql():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = ('select Name, AVG(SensoryRating) from ratings group by 1')
    cursor.execute(sql)
    return cursor.fetchall()

result = query_sensory_rating_sql()

# for tuple in result:
#     print(tuple[0])
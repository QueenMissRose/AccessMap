import sqlite3

import gspread

gc = gspread.service_account(filename='accessmap-441715-705d96e6c09e.json')

sh = gc.open_by_key("1O01Exonl72cF3G5ZYZzYgYJ55ObHaqrp0dXCHeZ4L-E")


def query_sensory_rating_sql():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = ('select Name, AVG(SensoryRating) from ratings group by 1')
    cursor.execute(sql)
    return cursor.fetchall()


def query_mobility_rating_sql():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = ('select Name, AVG(MobilityRating) from ratings group by 1')
    cursor.execute(sql)
    return cursor.fetchall()


def query_service_dog_relief_rating_sql():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = ('select Name, AVG(ServiceDogRelief) from ratings group by 1')
    cursor.execute(sql)
    return cursor.fetchall()


def query_wheelchair_accessible_rating_sql():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = ('select Name, AVG(WheelchairAccessible) from ratings group by 1')
    cursor.execute(sql)
    return cursor.fetchall()


def query_allergen_risk_rating_sql():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = ('select Name, AVG(CommonAllergenRisk) from ratings group by 1')
    cursor.execute(sql)
    return cursor.fetchall()



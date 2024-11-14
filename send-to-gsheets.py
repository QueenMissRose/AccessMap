import gspread

gc = gspread.service_account(filename='/Users/mermaid/PycharmProjects/AccessMap/accessmap-441715-705d96e6c09e.json')

sh = gc.open_by_key("1O01Exonl72cF3G5ZYZzYgYJ55ObHaqrp0dXCHeZ4L-E")

print(sh.sheet1.get('A1'))



worksheet = sh.sheet1

# body = [location_name, address, sensory_rating, mobility_rating, service_dog_relief_rating,wheelchair_rating, common_allergens_rating]
values = [5, "Lincoln Park Branch Chicago Public Library", "1150 W Fullerton Ave, Chicago, IL 60614", 5, 4, 2, 5, 1]
worksheet.append_row(values)
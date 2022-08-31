import room as r

url_rc = "YOUR_SERVER_URL" # Without the end slash, example: https://chat.company.com
department = "DEPARTMENT" # Department name

###############################################################

count = 1 # How many rooms to open? 1s delay between each room.

for i in range(count):
  r.open_room(url_rc, department)
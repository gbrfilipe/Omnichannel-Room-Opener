import visitors as v
import room as r

url_rc = "https://xyz.com" # Without the end slash, example: https://chat.domain.com
department = "XYZ" # Department name

count = 1 # How many rooms to open? 1s delay between each room.

v.visitors(count, department, url_rc)
r.open_room(count, url_rc, token = v.token)

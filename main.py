import visitors as v
import room as r

url_rc = "https://xyz.com" # Without the end slash, example: https://chat.domain.com
department = "XYZ" # Department name

count = 1 # How many rooms to open? 1s delay between each room.

v.visitors(count)
r.open_room(url_rc, department, count, name = v.name, email = v.email, phone = v.phone, token = v.token)

import requests
import json
import time

def open_room(url_rc, department, count, name, email, phone, token):

  for i in range(count):

    time.sleep(1)

    visitor_endpoint = "/api/v1/livechat/visitor"
    room_endpoint = "/api/v1/livechat/room"
    url_visitor = url_rc + visitor_endpoint
    url_room = url_rc + room_endpoint + "?token=" + token[i]

    visitor_payload = json.dumps({
      "visitor": {
        "department": department,
        "name": name[i],
        "email": email[i],
        "token": token[i],
        "phone": phone[i]
      }
    })

    visitor_headers = {
      'Content-Type': 'application/json'
    }

    new_visitor = requests.post(url_visitor, headers = visitor_headers, data = visitor_payload)

    #print(new_visitor.text)

    room = requests.get(url_room)
    print(room.json())

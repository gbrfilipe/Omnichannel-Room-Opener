import requests
import json
import uuid
import time

def open_room(url_rc, department):

  time.sleep(1)

  token = str(uuid.uuid4())

  url_random_user = "https://randomuser.me/api/"

  visitor_endpoint = "/api/v1/livechat/visitor"
  room_endpoint = "/api/v1/livechat/room"
  url_visitor = url_rc + visitor_endpoint
  url_room = url_rc + room_endpoint + "?token=" + token
  

  requests_random_user = requests.get(url_random_user)
  random_user = requests_random_user.json()

  name = (random_user["results"][0]["name"]["first"] + " " + random_user["results"][0]["name"]["last"])
  email = random_user["results"][0]["email"]
  phone = random_user["results"][0]["phone"]

  

  visitor_payload = json.dumps({
    "visitor": {
      "department": department,
      "name": name,
      "email": email,
      "token": token,
      "phone": phone
    }
  })

  visitor_headers = {
    'Content-Type': 'application/json'
  }

  new_visitor = requests.post(url_visitor, headers = visitor_headers, data = visitor_payload)

  #print(new_visitor.text)

  

  room = requests.get(url_room)
  print(room.json())
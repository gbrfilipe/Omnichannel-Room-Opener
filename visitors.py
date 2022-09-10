import requests as req
import json

token = []

def visitors(count: int, department: str, url_rc: str):

  url_random_user = "https://randomuser.me/api/?results=" + str(count)
  url_visitor = url_rc + "/api/v1/livechat/visitor"

  random_user = req.get(url_random_user).json()

  for i in range(count):
    
    full_name = random_user["results"][i]["name"]["first"] + " " + random_user["results"][i]["name"]["last"]
    token.append(random_user["results"][i]["login"]["uuid"])

    visitor_payload = json.dumps({
      "visitor": {
        "department": department,
        "name": full_name,
        "email": random_user["results"][i]["email"],
        "token": random_user["results"][i]["login"]["uuid"],
        "phone": random_user["results"][i]["phone"]
      }
    })

    visitor_headers = {
      'Content-Type': 'application/json'
    }

    new_visitor = req.post(url_visitor, headers = visitor_headers, data = visitor_payload)

    # print(new_visitor.text)

  return token

import requests
import uuid
import json

name = []
email = []
phone = []
token = []

def visitors(count: int, department: str, url_rc: str):

  url_random_user = "https://randomuser.me/api/?results=" + str(count)
  url_visitor = url_rc + "/api/v1/livechat/visitor"

  requests_random_user = requests.get(url_random_user)
  random_user = requests_random_user.json()

  for i in range(count):
    name.append((random_user["results"][i]["name"]["first"] + " " + random_user["results"][i]["name"]["last"]))
    email.append(random_user["results"][i]["email"])
    phone.append(random_user["results"][i]["phone"])
    token.append(str(uuid.uuid4()))

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

  return token

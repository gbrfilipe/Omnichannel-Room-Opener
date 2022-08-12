import requests
import json

url_rc = "https://xyz"
url_random_user = "https://randomuser.me/api/"

department = "DEPARTMENT_NAME"

visitor_endpoint = "/api/v1/livechat/visitor"
agent_next_endpoint = "/api/v1/livechat/agent.next/"
room_endpoint = "/api/v1/livechat/room"

r = requests.get(url_random_user)
random_user = r.json()

name = (random_user["results"][0]["name"]["first"] + " " + random_user["results"][0]["name"]["last"])
city = random_user["results"][0]["location"]["city"]
state = random_user["results"][0]["location"]["state"]
country = random_user["results"][0]["location"]["country"]
gender = random_user["results"][0]["gender"]
token = random_user["results"][0]["login"]["uuid"]
email = random_user["results"][0]["email"]
phone = random_user["results"][0]["email"]

url_visitor = url_rc + visitor_endpoint

payload = json.dumps({
  "visitor": {
    "department": "GD",
    "name": name,
    "email": email,
    "token": token,
    "phone": phone,
    "customFields": [
      {
        "key": "City",
        "value": city,
        "overwrite": True
      },
      {
        "key": "Country",
        "value": country,
        "overwrite": True
      },
      {
        "key": "Gender",
        "value": gender,
        "overwrite": True
      },
      {
        "key": "State",
        "value": state,
        "overwrite": True
      }
    ]
  }
})

headers = {
  'Content-Type': 'application/json'
}

visitor_call = requests.post(url_visitor, headers = headers, data=payload)

#print(visitor_call.text)

url_next_agent = url_rc + agent_next_endpoint + token

response = requests.get(url_next_agent)
next_agent = response.json()
next_agent.keys()
#print(next_agent["agent"])
agent_id = next_agent["agent"]["_id"]

url_room = url_rc + room_endpoint + "?token=" + token + "&agentId=" + agent_id
#print(url_room)
room = requests.get(url_room)
print(room.json())

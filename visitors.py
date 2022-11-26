import requests as req
from faker import Faker
import uuid
import json

fake = Faker()

token = []

def visitors(count: int, department: str, url_rc: str):

  url_visitor = url_rc + "/api/v1/livechat/visitor"

  for i in range(count):

    visitor_token = str(uuid.uuid4())
    
    token.append(visitor_token)

    new_visitor_payload = json.dumps({
      "visitor": {
        "department": department,
        "name": fake.name(),
        "email": fake.email(),
        "token": visitor_token,
        "phone": fake.phone_number()
      }
    })

    new_visitor_headers = {
      'Content-Type': 'application/json'
    }

    new_visitor = req.post(url_visitor, headers = new_visitor_headers, data = new_visitor_payload, timeout=3)

    # print(new_visitor.text)

  return token

import requests
import uuid

count = 2

name = []
email = []
phone = []
token = []

def visitors(count):

  url_random_user = "https://randomuser.me/api/?results=" + str(count)

  requests_random_user = requests.get(url_random_user)
  random_user = requests_random_user.json()

  for i in range(count):
    name.append((random_user["results"][i]["name"]["first"] + " " + random_user["results"][i]["name"]["last"]))
    email.append(random_user["results"][i]["email"])
    phone.append(random_user["results"][i]["phone"])
    token.append(str(uuid.uuid4()))

  return name, email, phone, token
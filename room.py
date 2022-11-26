import requests as req
import time
import json

def open_room(count: int, url_rc: str, token: str):

  for i in range(count):

    time.sleep(1)

    url_room = url_rc + "/api/v1/livechat/room" + "?token=" + token[i]

    room = req.get(url_room, timeout=3)
    print(room.json())

    url_message = url_rc + "/api/v1/livechat/message"

    message = json.dumps({"token": token[i], "rid": room.json()["room"]["_id"], "msg": "test.."})


    message_headers = {
      'Content-Type': 'application/json'
    }

    time.sleep(3)

    send_message = req.post(url_message, headers = message_headers, data = message, timeout=3)
    print(send_message)

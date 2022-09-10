import requests as req
import time

def open_room(count: int, url_rc: str, token: str):

  for i in range(count):

    time.sleep(1)

    url_room = url_rc + "/api/v1/livechat/room" + "?token=" + token[i]

    room = req.get(url_room)
    print(room.json())

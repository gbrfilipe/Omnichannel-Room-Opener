# 🚀 Rocket.Chat - Omnichannel Room Opener

This script opens an omnichannel room and sends a message, perfect for mass testing omnichannel behaviors and bot integrations.

### **BE CAREFUL, use responsibly to not overload your server with too many rooms.**

Change the [**url_rc**](https://github.com/gbrfilipe/Omnichannel-Room-Opener/blob/main/main.py#L4), [**department**](https://github.com/gbrfilipe/Omnichannel-Room-Opener/blob/main/main.py#L5) and [**count**](https://github.com/gbrfilipe/Omnichannel-Room-Opener/blob/main/main.py#L7) variables at [**main**](https://github.com/gbrfilipe/Omnichannel-Room-Opener-Rocket.Chat/blob/main/main.py) file.

Have at least one omnichannel online agent.

External libraries: [requests](https://requests.readthedocs.io/) and [faker](https://faker.readthedocs.io/).

Rocket.Chat APIs used: 

- [Livechat Room Info](https://developer.rocket.chat/reference/api/rest-api/endpoints/omnichannel/livechat-endpoints/livechat-room/livechat-room-info) 
- [Register a new Livechat visitor](https://developer.rocket.chat/reference/api/rest-api/endpoints/omnichannel/livechat-endpoints/visitor/register-a-new-livechat-visitor)
- [Update a Livechat message](https://developer.rocket.chat/reference/api/rest-api/endpoints/omnichannel/livechat-endpoints/livechat-message/update-a-livechat-message)

PS: The department information must be in the visitor's payload, otherwise the room will not be allocated to any department.

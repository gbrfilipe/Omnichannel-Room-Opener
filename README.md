# Omnichannel Room Opener - Rocket.Chat

This script opens an omnichannel room and sends a message. 

### **BE CAREFUL, use responsibly to not overload your server with too many rooms.**

Change the **url_rc**, **department** and **count** variables at **main** file.

Have at least one omnichannel online agent.

External libraries: requests and faker.

APIs Documentation: 

- Rocket.Chat room: https://developer.rocket.chat/reference/api/rest-api/endpoints/omnichannel/livechat-endpoints/livechat-room/livechat-room-info 
- Rocket.Chat visitor: https://developer.rocket.chat/reference/api/rest-api/endpoints/omnichannel/livechat-endpoints/visitor/register-a-new-livechat-visitor
- Rocket.Chat livechat message: https://developer.rocket.chat/reference/api/rest-api/endpoints/omnichannel/livechat-endpoints/livechat-message/update-a-livechat-message

PS: The department information must be in the visitor's payload, otherwise the room will not be allocated to any department.

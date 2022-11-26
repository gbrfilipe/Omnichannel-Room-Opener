# Omnichannel Room Opener - Rocket.Chat

### **BE CAREFUL, use responsibly to not overload your server with too many rooms.**

*Change the **url_rc**, **department** and **count** variables at **main** file.*

Keep at least one livechat agent online.

External libraries: requests and faker.
Install the liraries using **pip install requests** and **pip install faker** in your cmd. 

APIs Documentation: 

- Rocket.Chat Room: https://developer.rocket.chat/reference/api/rest-api/endpoints/omnichannel/livechat-endpoints/livechat-room/livechat-room-info 
- Rocket.Chat Visitor: https://developer.rocket.chat/reference/api/rest-api/endpoints/omnichannel/livechat-endpoints/visitor/register-a-new-livechat-visitor

PS: The department information must be in the visitor's payload, otherwise the room will not be allocated to any department.

import vkapi
import time
import sys

user_id = "9844399";

friends = vkapi.executeApiRequest("friends.get", {"user_id": user_id})["items"];


subscriptionsFriendsList = [];
f = open('data.txt', 'wb')
for id in friends:
    subscriptions = vkapi.executeApiRequest("execute.Subscriptions", {"user_id": str(id)});
    subscriptionsNew = [elem for elem in subscriptions if (elem != None and elem.find("Подслушано") != -1)];
    if (len(subscriptionsNew) != 0):
        f.write((str(id) +" : " + str(subscriptionsNew) + "\r\n").encode(sys.stdout.encoding, errors='replace'));
    subscriptionsFriendsList.append({"id": id, "subsciptions": subscriptionsNew});
    time.sleep(0.3);
        
f.close();
print("OK"); 
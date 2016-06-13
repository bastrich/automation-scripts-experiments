import vkapi

user_id = "115958114";
club = "63712838";

friends = vkapi.executeApiRequest("friends.get", {"user_id": user_id})["items"];
members = vkapi.executeApiRequest("execute.GroupMembers", {"club": club});

friendsLen = len(friends);
membersLen = len(members);

if (friendsLen > membersLen):
    great = friends;
    greatLen = friendsLen;
    less = members;
    lessLen = membersLen;
else:
    great = members;
    greatLen = membersLen;
    less = friends;
    lessLen = friendsLen;

result = [];
for id in less:
    if(great.count(id) > 0):
        result.append(id);
        
print(result); 
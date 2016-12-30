import sys
import vkapi

user_id = "123"

targetUser = vkapi.executeApiRequest("users.get", {"user_ids": user_id, "fields": "last_seen"})['response']

friends = vkapi.executeApiRequest("friends.get", {"user_id": user_id, "fields": "last_seen"})['response']['items']

target_timestamp = targetUser[0]['last_seen']['time']


def compare(x):
    if 'last_seen' in x:
        return abs(x['last_seen']['time'] - target_timestamp)
    else:
        return sys.maxsize


friends = sorted(friends, key=compare, reverse=False)

a = 4

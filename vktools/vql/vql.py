from vql.key_word import KeyWord
from vql.object_type import ObjectType

access_token = ""
api_version = ""
query = '''
with user = user.{id=123}
select users from user.friends order by abs(user.last_seen.time-user.friends[*].last_seen.time)
'''

def buildQueryObject(query):

    return 0

def execute_request(query):
    queryDOM = buildQueryObject(query)

    return queryDOM
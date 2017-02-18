import urllib.request
import json

access_token = "aa098011eb50080d17eb89fa3b965c638ae0391584224e8abcd3247ad460c89aaf7318a03b50c191ee35d"

def executeApiRequest(methodName, params):
    paramsString = ""
    for k in params:
        paramsString += k + "=" + str(params[k]) + "&"
    return json.loads(urllib.request.urlopen("https://api.vk.com/method/" + methodName + "?" + paramsString+ "access_token=" + access_token + "&v=5.50").read().decode("utf-8"))


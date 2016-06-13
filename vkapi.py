import urllib.request
import json

access_token = "aasd"

def executeApiRequest(methodName, params):
    paramsString = "";
    for k in params:
        paramsString += k + "=" + str(params[k]) + "&";
    return json.loads(urllib.request.urlopen("https://api.vk.com/method/" + methodName + "?" + paramsString+ "access_token=" + access_token + "&v=5.50").read().decode("utf-8"))


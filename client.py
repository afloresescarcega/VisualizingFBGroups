from facepy import GraphAPI
from facepy import utils
import simplejson as json


def getAppSecretStuff():
    idAndSecret = open("appSecretStuff", 'r')
    return [line.strip() for line in idAndSecret]

secrets = getAppSecretStuff()
tokenAndExpiration = utils.get_application_access_token(secrets[0],secrets[1])
graph = GraphAPI(tokenAndExpiration[0])

# Hardcoded UT FB meme group
# graph.get('1218486471522469/posts')

"""
Returns the name of the group, the icon picture url, the cover picture url
Parameters: FBGroup type int : the facebook group id
"""
def getFBGroupInfo(FBGroup):
    assert(type(FBGroup) is type(int())) # Ensure that preconditions hold
    groupGraph = graph.get(str(FBGroup) + "?fields=icon,cover,name")
    name = groupGraph["name"]
    iconUrl = groupGraph["icon"]
    coverUrl = groupGraph["cover"]["source"]
    return (name, iconUrl, coverUrl)

# print(graph.get('1218486471522469_1378570272180754?fields=reactions'))
# print(graph)

# test group info
group_info = str(getFBGroupInfo(1218486471522469))
print(type(group_info))
print(group_info)





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

print(graph.get('1218486471522469_1378570272180754?fields=reactions'))
print(graph)


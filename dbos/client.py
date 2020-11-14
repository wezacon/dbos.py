import ujson as json
import requests

from .lib.util import objects, exceptions


class Client:
    def __init__(self):
        self.api = "https://dbos.glitch.me/api"
        self.version = json.loads(requests.get(f"{self.api}/b/version").text)["Version"]

    def get_user_info(self, userId: int, serverId: int = None):
        if serverId is not None: target = f"s/{serverId}"
        else: target = "global"

        response = requests.get(f"{self.api}/{target}/u/{userId}")
        if response.status_code != 200: raise exceptions.CheckException(json.loads(response.text))
        else: return objects.UserProfile(json.loads(response.text)["user"])

    def get_user_level(self, userId: int, serverId: int):
        response = requests.get(f"{self.api}/s/{serverId}/u/{userId}/level")
        if response.status_code != 200: raise exceptions.CheckException(json.loads(response.text))
        else: return objects.Level(json.loads(response.text)["user"])

    def get_server_info(self, guildId: int):
        response = requests.get(f"{self.api}/global/s/{guildId}")
        if response.status_code != 200: raise exceptions.CheckException(json.loads(response.text))
        else: return objects.Server(json.loads(response.text)["guild"])

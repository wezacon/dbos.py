import ujson as json
import requests

from .lib.util import objects, exceptions


class Client:
    def __init__(self):
        self.api = "https://dbos.glitch.me/api"
        self.version = json.loads(requests.get(f"{self.api}/b/version").text)["version"]

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

    def get_bot_info(self):
        response = requests.get(f"{self.api}/bot")
        if response.status_code != 200: raise exceptions.CheckException(json.loads(response.text))
        else: return objects.Bot(json.loads(response.text))

    def get_all_users(self, serverId: int = None):
        if serverId is not None: target = f"u/s/{serverId}/all"
        else: target = "g/u/all"

        response = requests.get(f"{self.api}/{target}")
        if response.status_code != 200: raise exceptions.CheckException(json.loads(response.text))
        else: return objects.UserProfileList(json.loads(response.text)["users"]).usersList

    def get_all_servers(self, isPremium: bool = False):
        if isPremium is True: target = "premium"
        else: target = "g"

        response = requests.get(f"{self.api}/{target}/s/all")
        if response.status_code != 200: raise exceptions.CheckException(json.loads(response.text))
        else: return objects.ServerList(json.loads(response.text)["guilds"]).serversList

    def get_server_levels(self, serverId: int):
        response = requests.get(f"{self.api}/s/{serverId}/levels")
        if response.status_code != 200: raise exceptions.CheckException(json.loads(response.text))
        else: return objects.LevelList(json.loads(response.text)["levels"]).levelsList
import ujson as json
import requests

from .lib.util import objects


class Client:
    def __init__(self):
        self.api = "https://dbos.glitch.me/api"

    def get_user_info(self, userId: int, guildId: int = None):
        if guildId is not None:
            target = f"g/{guildId}"
        else:
            target = "global"

        response = requests.get(f"{self.api}/{target}/u/{userId}")
        if response.status_code != 200: raise Exception(json.loads(response.text))
        else: return objects.UserProfile(json.loads(response.text)["user"])

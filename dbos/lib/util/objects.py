class UserProfile:
    def __init__(self, data):
        self.json = data

        try: self.bio: str = data["bio"]
        except (KeyError, TypeError): self.bio: str = "Undefined"
        try: self.occupation: str = data["occupation"]
        except (KeyError, TypeError): self.occupation: str = "Undefined"
        try: self.profileImage: str = data["profileImage"]
        except (KeyError, TypeError): self.profileImage: str = "Undefined"
        try: self.removeReason: str = data["removeReason"]
        except (KeyError, TypeError): self.removeReason: str = "Undefined"
        try: self.username: str = data["username"]
        except (KeyError, TypeError): self.username: str = "Undefined"

        try: self.allowListing: bool = data["allowListing"]
        except (KeyError, TypeError): self.allowListing: bool = False
        try: self.dataCleared: bool = data["dataCleared"]
        except (KeyError, TypeError): self.dataCleared: bool = False
        try: self.isAdmin: bool = data["admin"]
        except (KeyError, TypeError): self.isAdmin: bool = False
        try: self.isContributor: bool = data["contributor"]
        except (KeyError, TypeError): self.isContributor: bool = False
        try: self.isModerator: bool = data["moderator"]
        except (KeyError, TypeError): self.isModerator: bool = False
        try: self.isRemoved: bool = data["removed"]
        except (KeyError, TypeError): self.isRemoved: bool = False
        try: self.isVerified: bool = data["verified"]
        except (KeyError, TypeError): self.isVerified: bool = False
        try: self.isSuperAdmin: bool = data["serverSuperAdmin"]
        except (KeyError, TypeError): self.isSuperAdmin: bool = False
        try: self.isSiteAdmin: bool = data["siteAdmin"]
        except (KeyError, TypeError): self.isSiteAdmin: bool = False
        try: self.isSiteModerator: bool = data["siteModerator"]
        except (KeyError, TypeError): self.isSiteModerator: bool = False

        try: self.discordServer: int = data["discordServer"]
        except (KeyError, TypeError): self.discordServer: int = -1
        try: self.github: int = data["github"]
        except (KeyError, TypeError): self.github: int = -1
        try: self.userId: int = data["id"]
        except (KeyError, TypeError): self.userId: int = -1
        try: self.messages: int = data["messages"]
        except (KeyError, TypeError): self.messages: int = -1
        try: self.guildId: int = data["guildID"]
        except (KeyError, TypeError): self.guildId: int = -1

        self.badges = []
        if self.isAdmin: self.badges.append("Admin")
        if self.isModerator: self.badges.append("Moderator")
        if self.isContributor: self.badges.append("Contributor")
        if self.isSuperAdmin: self.badges.append("Super Admin")
        if self.isVerified: self.badges.append("Verified")

class Level:
    def __init__(self, data):
        self.json = data

        try: self.userTag: str = data["userTag"]
        except (KeyError, TypeError): self.userTag: str = "Undefined"
        try: self.profileImage: str = data["userImage"]
        except (KeyError, TypeError): self.profileImage: str = "Undefined"
        try: self.lastUpdated: str = data["lastUpdated"]
        except (KeyError, TypeError): self.lastUpdated: str = "Undefined"

        try: self.isSiteAdmin: bool = data["siteAdmin"]
        except (KeyError, TypeError): self.isSiteAdmin: bool = False
        try: self.isSiteModerator: bool = data["siteModerator"]
        except (KeyError, TypeError): self.isSiteModerator: bool = False

        try: self.xp: int = data["xp"]
        except (KeyError, TypeError): self.xp: int = -1
        try: self.nxp: int = data["nxp"]
        except (KeyError, TypeError): self.nxp: int = -1
        try: self.level: int = data["level"]
        except (KeyError, TypeError): self.level: int = -1
        try: self.serverId: int = data["guildID"]
        except (KeyError, TypeError): self.serverId: int = -1
        try: self.userId: int = data["userID"]
        except (KeyError, TypeError): self.userId: int = -1


class Server:
    def __init__(self, data):
        self.json = data

        try: self.prefix: str = data["prefix"]
        except (KeyError, TypeError): self.prefix: str = "Undefined"
        try: self.name: str = data["name"]
        except (KeyError, TypeError): self.name: str = "Undefined"
        try: self.icon: str = data["icon"]
        except (KeyError, TypeError): self.icon: str = "Undefined"
        try: self.invite: str = data["invite"]
        except (KeyError, TypeError): self.invite: str = "Undefined"

        try: self.blacklisted: bool = data["blacklisted"]
        except (KeyError, TypeError): self.blacklisted: bool = False
        try: self.premium: bool = data["premium"]
        except (KeyError, TypeError): self.premium: bool = False

        try: self.logChannel: int = data["logChannel"]
        except (KeyError, TypeError): self.logChannel: int = -1
        try: self.serverId: int = data["id"]
        except (KeyError, TypeError): self.serverId: int = -1
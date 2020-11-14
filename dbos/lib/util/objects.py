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
        try: self.id: int = data["id"]
        except (KeyError, TypeError): self.id: int = -1
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
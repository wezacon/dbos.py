class UserProfile:
    def __init__(self, data):
        self.json = data

        try: self.allowListing: bool = data["allowListing"]
        except (KeyError, TypeError): self.allowListing: bool = False
        try: self.bio: str = data["bio"]
        except (KeyError, TypeError): self.bio: str = "Undefined"
        try: self.dataCleared: bool = data["dataCleared"]
        except (KeyError, TypeError): self.dataCleared: bool = False
        try: self.discordServer: int = data["discordServer"]
        except (KeyError, TypeError): self.discordServer: int = -1
        try: self.github: int = data["github"]
        except (KeyError, TypeError): self.github: int = -1
        try: self.id: int = data["id"]
        except (KeyError, TypeError): self.id: int = -1
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
        try: self.messages: int = data["messages"]
        except (KeyError, TypeError): self.messages: int = -1
        try: self.occupation: str = data["occupation"]
        except (KeyError, TypeError): self.occupation: str = "Undefined"
        try: self.profileImage: str = data["profileImage"]
        except (KeyError, TypeError): self.profileImage: str = "Undefined"
        try: self.removeReason: str = data["removeReason"]
        except (KeyError, TypeError): self.removeReason: str = "Undefined"
        try: self.username: str = data["username"]
        except (KeyError, TypeError): self.username: str = "Undefined"
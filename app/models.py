class User:
    def __init__(self, user_id, username, password, name):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.name = name

    def to_dict(self):
        return {
            "id": self.user_id,
            "username": self.username,
            "name": self.name,
        }

from models.users import User

class Admin(User):

    def __init__(self, id, name, email, password, phone):
        super().__init__(id, name, email, password, phone,"admin")

    @classmethod
    def from_dict(cls,d):
        return cls(d["id"],d["name"],d["email"],d["password"],d["phone"])
    
    def to_dict(self):
        data = super().to_dict()
        return data
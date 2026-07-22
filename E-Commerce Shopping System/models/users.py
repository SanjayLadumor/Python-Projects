class User:

    def __init__(self,id,name,email,password,phone,role):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.role = role

    def to_dict(self):
        a = {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "password":self.password,
            "phone":self.phone,
            "role":self.role
        }
        return a
    
    @classmethod
    def from_dict(cls,d):
        return cls(d["id"],d["name"],d["email"],d["password"],d["phone"],d["role"])
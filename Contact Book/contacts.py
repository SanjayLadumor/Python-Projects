class Contact:

    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def display(self):
        print(f"""Name : {self.name}
Phone : {self.phone}
Email : {self.email}
Address : {self.address}""")
        
    def to_dict(self):
        a = {
            "name":self.name,
            "phone":self.phone,
            "email":self.email,
            "address":self.address
        }
        return a
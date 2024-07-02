class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email
        

    def get_id(self):
        return self.id

    def set_id(self, user_id):
        self.id = user_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

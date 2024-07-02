class UserRepository:
    def __init__(self):
        self.user_database = {}

    def get_user_by_id(self, user_id):
        return self.user_database.get(user_id)

    def save_user(self, user):
        self.user_database[user.get_id()] = user

    def delete_user(self, user_id):
        if user_id in self.user_database:
            del self.user_database[user_id]

    def get_all_users(self):
        return list(self.user_database.values())
from service.user_service import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def get_user_by_id(self, user_id):
        return self.user_service.get_user_by_id(user_id)

    def save_user(self, user):
        self.user_service.save_user(user)

    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)

    def get_all_users(self):
        return self.user_service.get_all_users()

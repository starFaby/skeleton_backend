from flask_login import UserMixin
from services.serviUser import onGetUserByid
class UserModel(UserMixin):
    def __init__(self, userData):
        self.id = userData.username
        self.password = userData.password
        self.avatar = userData.avatar

    @staticmethod
    def get(username):
        userData = onGetUserByid(username)
        return UserModel(userData)
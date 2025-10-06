from ..dao.user_dao import UserDAO
from passlib.hash import pbkdf2_sha256

class UserService:
    @staticmethod
    def register(username: str, password: str):
        hashed_password = pbkdf2_sha256.hash(password)
        return UserDAO.create_user(username, hashed_password)

    @staticmethod
    def authenticate(username: str, password: str):
        user = UserDAO.get_by_username(username)
        if user and pbkdf2_sha256.verify(password, user.password):
            return user
        return None

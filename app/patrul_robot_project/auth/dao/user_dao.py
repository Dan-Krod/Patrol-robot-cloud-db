from ..domain.models import User, db

class UserDAO:
    @staticmethod
    def get_by_username(username: str):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username: str, password: str):
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user

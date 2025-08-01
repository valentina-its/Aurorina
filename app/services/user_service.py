from app.models.user import User

class UserService:
    @staticmethod
    def authenticate(username, password):
        return User.query.filter_by(username=username, password=password).first()
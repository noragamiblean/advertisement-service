from repositories.repository import Repository
from models.user import User
from models.advertisement import Advertisement

class UserService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_user(self, id) -> User:
        result = self.repository.get_user(id)
        if result is None:
            raise Exception("Пользователя с таким ID не существует.")
        else:
            return result

    def get_ads_by_user_id(self, user_id) -> list[Advertisement] | None:
        result = self.repository.get_advertisements_by_user_id(user_id)
        if result is None:
            raise Exception("У данного пользователя нет объявлений.")
        else:
            return result
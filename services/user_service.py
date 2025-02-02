from repositories.repository import Repository

class UserService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_ads_by_user_id(self, user_id):
        result = self.repository.get_advertisements_by_user_id(user_id)
        if result is None:
            raise Exception("У данного пользователя нет объявлений.")
        else:
            return result
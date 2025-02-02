from repositories.repository import Repository

class AdvertisementCategoryService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_category(self, id):
        result = self.repository.get_ad_category(id)
        if result is None:
            raise Exception("Категории с данным ID не существует.")
        else:
            return result
class AdvertisementCategory:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def print(self):
        print(f"Категория '{self.title}'")
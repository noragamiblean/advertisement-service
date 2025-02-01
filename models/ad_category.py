class AdvertisementCategory:
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title

    def print(self):
        print(f"Категория '{self.title}'")
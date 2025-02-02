class AdvertisementCategory:
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title

    def __eq__(self, other):
        if isinstance(other, AdvertisementCategory):
            return self.id == other.id
        else:
            return False

    def print(self):
        print(f"Категория '{self.title}'")
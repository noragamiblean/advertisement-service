from datetime import datetime
from models.location import Location

class Advertisement:
    def __init__(self,
                 id: int,
                 title: str,
                 description: str,
                 photo_url: str,
                 category_id: int,
                 price: int,
                 created_at: datetime,
                 updated_at: datetime,
                 expired_at: datetime,
                 created_by_id: int,
                 location: Location):
        self.id = id
        self.title = title
        self.description = description
        self.photo_url = photo_url
        self.category_id = category_id
        self.price = price
        self.created_at = created_at
        self.updated_at = updated_at
        self.expired_at = expired_at
        self.created_by_id = created_by_id
        self.location = location
        self.is_expired = False
        self.is_redeemed = False

    def __eq__(self, other):
        if isinstance(other, Advertisement):
            return self.id == other.id
        else:
            return False

    def to_print(self):
        return (f"Название: {self.title}"
                f"\nОписание: {self.description}"
                f"\nСсылка на фото: {self.photo_url}"
                f"\nСоздано {self.created_at}\tОбновлено {self.updated_at}"
                f"\nЗаканчивается {self.expired_at}"
                f"\nКоординаты: x={self.location.x}, y={self.location.y}")

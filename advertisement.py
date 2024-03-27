class Advertisement:
    def __init__(self, id, title, description, photo_url, category_id, created_at, updated_at, expired_at, created_by_id):
        self.id = id
        self.title = title
        self.description = description
        self.photo_url = photo_url
        self.category_id = category_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.expired_at = expired_at
        self.created_by_id = created_by_id
        self.questions_ids = []

    def to_print(self):
        return (f"Название: {self.title}"
                f"\nОписание: {self.description}"
                f"\nСсылка на фото: {self.photo_url}"
                f"\nСоздано {self.created_at}\tОбновлено {self.updated_at}"
                f"\nЗаканчивается {self.expired_at}")

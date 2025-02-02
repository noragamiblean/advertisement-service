from datetime import datetime

class Question:
    def __init__(self, id: int, text: str, created_by_id: int, advertisement_id: int, created_at: datetime):
        self.id = id
        self.text = text
        self.created_by_id = created_by_id
        self.advertisement_id = advertisement_id
        self.created_at = created_at

    def __eq__(self, other):
        if isinstance(other, Question):
            return self.id == other.id
        else:
            return False

    def to_print(self):
        return f"{self.text}\tот {self.created_at}"

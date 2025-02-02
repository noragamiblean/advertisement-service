from datetime import datetime

class Answer:
    def __init__(self, id: int, text: str, created_by_id: int, question_id: int, created_at: datetime):
        self.id = id
        self.text = text
        self.created_by_id = created_by_id
        self.question_id = question_id
        self.created_at = created_at

    def __eq__(self, other):
        if isinstance(other, Answer):
            return self.id == other.id
        else:
            return False

    def to_print(self):
        return f"{self.text}\tот {self.created_at}"
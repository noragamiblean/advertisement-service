class Question:
    def __init__(self, id, text, created_by_id, advertisement_id, created_at):
        self.id = id
        self.text = text
        self.created_by_id = created_by_id
        self.advertisement_id = advertisement_id
        self.created_at = created_at
        self.answers_ids = []

    def to_print(self):
        return f"{self.text}\tот {self.created_at}"

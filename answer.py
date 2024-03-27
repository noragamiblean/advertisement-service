class Answer:
    def __init__(self, id, text, created_by_id, question_id, created_at):
        self.id = id
        self.text = text
        self.created_by_id = created_by_id
        self.question_id = question_id
        self.created_at = created_at

    def to_print(self):
        return f"{self.text}\tот {self.created_at}"
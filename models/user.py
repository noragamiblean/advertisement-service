from datetime import datetime, date

class User:
    def __init__(self,
                 id: int,
                 username: str,
                 first_name: str,
                 last_name: str,
                 email: str,
                 phone_number: str,
                 birth_date: date,
                 register_at: datetime):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.register_at = register_at
        self.rating = 0
        self.rating_avg = 0
        self.sold = 0
        self.bought = 0

    def to_print(self):
        return (f"Псевдоним: {self.username}\n{self.first_name} {self.last_name}"
                f"\nАдрес эл. почты: {self.email}"
                f"\nНомер телефона: {self.phone_number}"
                f"\nДата рождения: {self.birth_date}"
                f"\nЗарегистрирован: {self.register_at}"
                f"\nПродал: {self.sold}"
                f"\nКупил: {self.bought}"
                f"\nРейтинг: {self.rating}"
                f"\nСредняя оценка: {self.rating_avg}")

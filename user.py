class User:
    def __init__(self, id, username, first_name, last_name, email, phone_number, birth_date, register_at):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.register_at = register_at
        self.ads_ids = []

    def to_print(self):
        return f"Псевдоним: {self.username}\n{self.first_name} {self.last_name}\nАдрес эл. почты: {self.email}\nНомер телефона: {self.phone_number}\nДата рождения: {self.birth_date}\nЗарегистрирован: {self.register_at}"

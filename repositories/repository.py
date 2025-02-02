import abc

class Repository(abc.ABC):
    @abc.abstractmethod
    def get_users(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, username, first_name, last_name, email, phone_number, birth_date):
        raise NotImplementedError

    @abc.abstractmethod
    def update_user(self, user_id, attrib, value):
        raise NotImplementedError

    @abc.abstractmethod
    def get_advertisements(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_advertisement(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_advertisements_by_user_id(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_advertisement(self, title, description, photo_url, category_id, price, validity, user_id, location):
        raise NotImplementedError

    @abc.abstractmethod
    def get_ad_category(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_ad_category(self, title):
        raise NotImplementedError

    @abc.abstractmethod
    def get_question(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_questions_by_ad_id(self, ad_id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_question(self, text, ad_id, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_answer(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_answers_by_question_id(self, question_id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_answer(self, text, question_id, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_deal(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_deal_by_ad_id(self, ad_id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_deal(self, ad_id, redeemer_id, rating, text):
        raise NotImplementedError
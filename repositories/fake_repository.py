from datetime import datetime, timedelta
from repositories.repository import Repository
from models.user import User
from models.advertisement import Advertisement
from models.ad_category import AdvertisementCategory
from models.question import Question
from models.answer import Answer
from models.location import Location
from models.deal import Deal


class FakeRepository(Repository):
    def __init__(self):
        self.__users: list[User] = []
        self.__ads: list[Advertisement] = []
        self.__questions: list[Question] = []
        self.__answers: list[Answer] = []
        self.__categories: list[AdvertisementCategory] = []
        self.deals: list[Deal] = []
        (self.__max_user_id,
         self.__max_ad_id,
         self.__max_category_id,
         self.__max_question_id,
         self.__max_answer_id,
         self.__max_deal_id) = 0, 0, 0, 0, 0, 0

    def get_user(self, id) -> User | None:
        for selected_user in self.__users:
            if selected_user.id == id: return selected_user

    def add_user(self, username, first_name, last_name, email, phone_number, birth_date) -> User:
        self.__users.append(User(
            id=self.__max_user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            birth_date=datetime.strptime(birth_date, "%d.%m.%Y").date(),
            register_at=datetime.now()
        ))
        self.__max_user_id += 1
        return self.__users[self.__max_user_id - 1]

    def get_advertisement(self, id) -> Advertisement | None:
        for ad in self.__ads:
            if ad.id == id: return ad

    def add_advertisement(self, title, description, photo_url, category_id, price, validity, user_id, location: Location) -> Advertisement:
        if price < 0:
            raise Exception("Стоимость выкупа объявления не может быть ниже нуля.")

        current_datetime = datetime.now()
        self.__ads.append(Advertisement(
            id=self.__max_ad_id,
            title=title,
            description=description,
            photo_url=photo_url,
            category_id=category_id,
            price=price,
            created_at=current_datetime,
            updated_at=current_datetime,
            expired_at=current_datetime + timedelta(days=validity),
            created_by_id=user_id,
            location=location
        ))
        self.__max_ad_id += 1
        new_ad = self.__ads[self.__max_ad_id - 1]
        return new_ad

    def get_ad_category(self, id) -> AdvertisementCategory | None:
        for category in self.__categories:
            if category.id == id: return category

    def add_ad_category(self, title) -> AdvertisementCategory:
        self.__categories.append(AdvertisementCategory(
            id=self.__max_category_id,
            title=title
        ))
        self.__max_category_id += 1
        new_category = self.__categories[self.__max_category_id - 1]
        return new_category

    def get_question(self, id) -> Question | None:
        for question in self.__questions:
            if question.id == id: return question

    def add_question(self, text, ad_id, user_id) -> Question:
            self.__questions.append(Question(
                id=self.__max_question_id,
                text=text,
                created_by_id=user_id,
                advertisement_id=ad_id,
                created_at=datetime.now()
            ))
            self.__max_question_id += 1
            new_question = self.__questions[self.__max_question_id - 1]
            return new_question

    def get_answer(self, id) -> Answer | None:
        for answer in self.__answers:
            if answer.id == id: return answer

    def add_answer(self, text, question_id, user_id) -> Answer:
            self.__answers.append(Answer(
                id=self.__max_answer_id,
                text=text,
                created_by_id=user_id,
                question_id=question_id,
                created_at=datetime.now()
            ))
            self.__max_answer_id += 1
            new_answer = self.__answers[self.__max_answer_id - 1]
            return new_answer

    def get_deal(self, ad_id) -> Deal | None:
        for deal in self.deals:
            if deal.ad_id == ad_id: return deal

    def add_deal(self, ad_id, redeemer_id, rating, text) -> Deal:
        self.deals.append(Deal(
            ad_id=ad_id,
            redeemer_id=redeemer_id,
            rating=rating,
            text=text,
            redeemed_at=datetime.now()
        ))
        self.__max_deal_id += 1
        new_deal = self.deals[self.__max_deal_id - 1]
        return new_deal
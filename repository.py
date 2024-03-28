from user import User
from advertisement import Advertisement
from ad_category import AdvertisementCategory
from question import Question
from answer import Answer
from datetime import datetime, timedelta
from typing import List


class AdvertisementServiceRepository:
    def __init__(self):
        self.__users = []
        self.__ads = []
        self.__ads_editable_attrs = ["title", "description", "photo_url", "category_id"]
        self.__questions = []
        self.__answers = []
        self.__categories = [AdvertisementCategory(0, "Одежда"), AdvertisementCategory(1, "Техника"), AdvertisementCategory(2, "Недвижимость")]
        self.__max_user_id, self.__max_ad_id, self.__max_question_id, self.__max_answer_id = 0, 0, 0, 0

    # User
    def get_users(self) -> List[User]:
        return self.__users

    def get_user_by_id(self, id) -> User:
        for selected_user in self.__users:
            if selected_user.id == id: return selected_user

    def create_user(self, username, first_name, last_name, email, phone_number, birth_date) -> User:
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

    def delete_user(self, user: User):
        for selected_user in self.__users:
            if selected_user is user:
                self.__users.remove(selected_user)

    # Advertisement
    def get_ads(self) -> List[Advertisement]:
        return self.__ads

    def get_ads_by_user(self, user: User) -> List[Advertisement]:
        if len(user.ads_ids) > 0:
            user_ads = []
            for id in user.ads_ids:
                user_ads.append(self.get_ad_by_id(id))
            return user_ads
        else :
            print(f"У пользователя {user.username} нет объявлений!")

    def get_ad_by_id(self, id) -> Advertisement:
        for ad in self.__ads:
            if ad.id == id: return ad

    def create_ad(self, title, description, photo_url, category_id, validity, user: User) -> Advertisement:
        current_datetime = datetime.now()
        self.__ads.append(Advertisement(
            id=self.__max_ad_id,
            title=title,
            description=description,
            photo_url=photo_url,
            category_id=category_id,
            created_at=current_datetime,
            updated_at=current_datetime,
            expired_at=current_datetime + timedelta(days=validity),
            created_by_id=user.id
        ))
        self.__max_ad_id += 1
        new_ad = self.__ads[self.__max_ad_id - 1]
        user.ads_ids.append(new_ad.id)
        return new_ad

    def update_ad(self, ad: Advertisement, user: User, **kwargs):
        if ad.id in user.ads_ids:
            for key in kwargs.keys():
                key_title = key.title().lower()
                if key_title in self.__ads_editable_attrs:
                    setattr(ad, key_title, kwargs.get(key))
                else:
                    print(f"Advertisement не имеет атрибутов с названием '{key_title}'!")
            setattr(ad, "updated_at", datetime.now())

    def delete_ad(self, ad: Advertisement, user: User):
        if ad.id in user.ads_ids:
            for selected_ad in self.__ads:
                if selected_ad is ad:
                    for id in ad.questions_ids:
                        self.delete_question(self.get_question_by_id(id), user)
                    self.__ads.remove(selected_ad)

    # Question
    def get_question_by_id(self, id) -> Question:
        for question in self.__questions:
            if question.id == id: return question

    def get_questions_by_ad(self, ad: Advertisement) -> List[Question]:
        if len(ad.questions_ids) > 0:
            ad_questions = []
            for id in ad.questions_ids:
                ad_questions.append(self.get_question_by_id(id))
            return ad_questions
        else:
            print(f"У объявления '{ad.title}' нет вопросов!")

    def create_question(self, text, ad: Advertisement, user: User) -> Question:
        if ad.created_by_id != user.id:
            self.__questions.append(Question(
                id=self.__max_question_id,
                text=text,
                created_by_id=user.id,
                advertisement_id=ad.id,
                created_at=datetime.now()
            ))
            self.__max_question_id += 1
            new_question = self.__questions[self.__max_question_id - 1]
            ad.questions_ids.append(new_question.id)
            return new_question
        else: print(f"Создатель объявления '{user.username}' не может создавать вопросы для своего же объявления!")

    def delete_question(self, question: Question, user: User):
        if question.advertisement_id in user.ads_ids:
            for selected_question in self.__questions:
                if selected_question is question:
                    for id in question.answers_ids:
                        self.delete_answer(self.get_answer_by_id(id), user)
                    self.__questions.remove(selected_question)

    # Answer
    def get_answer_by_id(self, id) -> Answer:
        for answer in self.__answers:
            if answer.id == id: return answer

    def get_answers_by_question(self, question: Question) -> List[Answer]:
        if len(question.answers_ids) > 0:
            question_answers = []
            for id in question.answers_ids:
                question_answers.append(self.get_answer_by_id(id))
            return question_answers
        else:
            print(f"У вопроса '{question.text}' нет ответов!")

    def create_answer(self, text, question: Question, user: User) -> Answer:
        if question.created_by_id != user.id:
            self.__answers.append(Answer(
                id=self.__max_answer_id,
                text=text,
                created_by_id=user.id,
                question_id=question.id,
                created_at=datetime.now()
            ))
            self.__max_answer_id += 1
            new_answer = self.__answers[self.__max_answer_id - 1]
            question.answers_ids.append(new_answer.id)
            return new_answer
        else: print(f"Создатель вопроса '{user.username}' не может отвечать на свой же вопрос!")

    def delete_answer(self, answer: Answer, user: User):
        if answer.created_by_id == user.id:
            for selected_answer in self.__answers:
                if selected_answer is answer:
                    self.__answers.remove(selected_answer)
    
    # Print
    def print_user_ads(self, user: User):
        print(f"Пользователь:\n{user.to_print()}\n")
        for ad_id in user.ads_ids:
            selected_ad = self.get_ad_by_id(ad_id)
            print(f"Объявление №{selected_ad.id}\n{selected_ad.to_print()}\n")
            for question_id in selected_ad.questions_ids:
                selected_question = self.get_question_by_id(question_id)
                print(f"\tВопрос №{selected_question.id}:\n\t{selected_question.to_print()}\n")
                for answer_id in selected_question.answers_ids:
                    selected_answer = self.get_answer_by_id(answer_id)
                    print(f"\t\tОтвет №{selected_answer.id}\n\t\t{selected_answer.to_print()}")
            


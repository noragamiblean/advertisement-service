from repositories.repository import Repository
from lxml import etree
from lxml.etree import Element, SubElement
from datetime import datetime, timedelta
from models.user import User
from models.advertisement import Advertisement
from models.location import Location
from models.ad_category import AdvertisementCategory
from models.question import Question
from models.answer import Answer
from models.deal import Deal
import json

class XmlRepository(Repository):
    def __init__(self):
        (self.__max_user_id,
         self.__max_ad_id,
         self.__max_category_id,
         self.__max_question_id,
         self.__max_answer_id,
         self.__max_deal_id) = 0, 0, 0, 0, 0, 0

        self.xml_path = "repo.xml"
        self.root = Element("root")
        self.doc = etree.ElementTree(self.root)
        self.doc.write(self.xml_path)

    def get_users(self) -> list[User] | None:
        users_elements = self.root.findall(".//user")
        users_objects = []
        for user_element in users_elements:
            user_object = User(
            id=int(user_element.attrib["id"]),
            username=user_element.find("username").text,
            first_name=user_element.find("first_name").text,
            last_name=user_element.find("last_name").text,
            email=user_element.find("email").text,
            phone_number=user_element.find("phone_number").text,
            birth_date=user_element.find("birth_date").text,
            register_at=datetime.fromisoformat(user_element.find("register_at").text)
            )
            user_object.rating = float(user_element.find("rating").text)
            user_object.rating_avg = float(user_element.find("rating_avg").text)
            user_object.sold = int(user_element.find("sold").text)
            user_object.bought = int(user_element.find("bought").text)
            users_objects.append(user_object)
        return users_objects

    def get_user(self, id) -> User:
        user_element = self.root.find(f".//user[@id='{id}']")
        user_object = User(
            id=id,
            username=user_element.find("username").text,
            first_name=user_element.find("first_name").text,
            last_name=user_element.find("last_name").text,
            email=user_element.find("email").text,
            phone_number=user_element.find("phone_number").text,
            birth_date=user_element.find("birth_date").text,
            register_at=datetime.fromisoformat(user_element.find("register_at").text)
        )
        user_object.rating = float(user_element.find("rating").text)
        user_object.rating_avg = float(user_element.find("rating_avg").text)
        user_object.sold = int(user_element.find("sold").text)
        user_object.bought = int(user_element.find("bought").text)
        return user_object

    def add_user(self, username, first_name, last_name, email, phone_number, birth_date) -> User:
        if not self.root.find("users"):
            self.root.append(Element("users"))
            self.doc.write(self.xml_path)

        user = Element("user")
        user.set("id", str(self.__max_user_id))
        SubElement(user, "username").text = username
        SubElement(user, "first_name").text = first_name
        SubElement(user, "last_name").text = last_name
        SubElement(user, "email").text = email
        SubElement(user, "phone_number").text = phone_number
        SubElement(user, "birth_date").text = birth_date
        SubElement(user, "register_at").text = str(datetime.now())
        SubElement(user, "rating").text = str(0)
        SubElement(user, "rating_avg").text = str(0)
        SubElement(user, "sold").text = str(0)
        SubElement(user, "bought").text = str(0)

        self.__max_user_id += 1
        self.root.find("users").append(user)
        self.doc.write(self.xml_path)

        return self.get_user(self.__max_user_id - 1)

    def update_user(self, user_id, attrib, value):
        user_element = self.root.find(f".//user[@id='{user_id}']")
        user_element.find(f".//{attrib}").text = str(value)

    def get_advertisements(self) -> list[Advertisement] | None:
        ads_elements = self.root.findall(".//ad")
        ads_objects = []
        for ad_element in ads_elements:
            ad_object = Advertisement(
                id=int(ad_element.attrib["id"]),
                title=ad_element.find("title").text,
                description=ad_element.find("description").text,
                photo_url=ad_element.find("photo_url").text,
                category_id=int(ad_element.find("category_id").text),
                price=int(ad_element.find("price").text),
                created_at=datetime.fromisoformat(ad_element.find("created_at").text),
                updated_at=datetime.fromisoformat(ad_element.find("updated_at").text),
                expired_at=datetime.fromisoformat(ad_element.find("expired_at").text),
                created_by_id=int(ad_element.find("created_by_id").text),
                location=Location(int(ad_element.find("location").attrib["x"]),
                                  int(ad_element.find("location").attrib["y"]))
            )
            ad_object.is_expired = json.loads(ad_element.find("is_expired").text.lower())
            ad_object.is_redeemed = json.loads(ad_element.find("is_redeemed").text.lower())
            ads_objects.append(ad_object)
        return ads_objects

    def get_advertisement(self, id) -> Advertisement:
        ad_element = self.root.find(f".//ad[@id='{id}']")
        ad_object = Advertisement(
            id=id,
            title=ad_element.find("title").text,
            description=ad_element.find("description").text,
            photo_url=ad_element.find("photo_url").text,
            category_id=int(ad_element.find("category_id").text),
            price=int(ad_element.find("price").text),
            created_at=datetime.fromisoformat(ad_element.find("created_at").text),
            updated_at=datetime.fromisoformat(ad_element.find("updated_at").text),
            expired_at=datetime.fromisoformat(ad_element.find("expired_at").text),
            created_by_id=int(ad_element.find("created_by_id").text),
            location=Location(int(ad_element.find("location").attrib["x"]), int(ad_element.find("location").attrib["y"]))
        )
        ad_object.is_expired = json.loads(ad_element.find("is_expired").text.lower())
        ad_object.is_redeemed = json.loads(ad_element.find("is_redeemed").text.lower())
        return ad_object

    def get_advertisements_by_user_id(self, user_id) -> list[Advertisement] | None:
        ads_elements = self.root.findall(".//ad")
        ads_objects = []
        for ad_element in ads_elements:
            if int(ad_element.find("created_by_id").text) == user_id:
                ad_object = Advertisement(
                    id=int(ad_element.attrib["id"]),
                    title=ad_element.find("title").text,
                    description=ad_element.find("description").text,
                    photo_url=ad_element.find("photo_url").text,
                    category_id=int(ad_element.find("category_id").text),
                    price=int(ad_element.find("price").text),
                    created_at=datetime.fromisoformat(ad_element.find("created_at").text),
                    updated_at=datetime.fromisoformat(ad_element.find("updated_at").text),
                    expired_at=datetime.fromisoformat(ad_element.find("expired_at").text),
                    created_by_id=int(ad_element.find("created_by_id").text),
                    location=Location(int(ad_element.find("location").attrib["x"]),
                                      int(ad_element.find("location").attrib["y"]))
                )
                ad_object.is_expired = json.loads(ad_element.find("is_expired").text.lower())
                ad_object.is_redeemed = json.loads(ad_element.find("is_redeemed").text.lower())
                ads_objects.append(ad_object)
        return ads_objects

    def add_advertisement(self, title, description, photo_url, category_id, price, validity, user_id, location) -> Advertisement:
        if price < 0:
            raise Exception("Стоимость выкупа объявления не может быть ниже нуля.")

        if not self.root.find("ads"):
            self.root.append(Element("ads"))
            self.doc.write(self.xml_path)

        current_datetime = datetime.now()
        ad = Element("ad")
        ad.set("id", str(self.__max_ad_id))
        SubElement(ad, "title").text = title
        SubElement(ad, "description").text = description
        SubElement(ad, "photo_url").text = photo_url
        SubElement(ad, "category_id").text = str(category_id)
        SubElement(ad, "price").text = str(price)
        SubElement(ad, "created_at").text = str(current_datetime)
        SubElement(ad, "updated_at").text = str(current_datetime)
        SubElement(ad, "expired_at").text = str(current_datetime + timedelta(days=validity))
        SubElement(ad, "created_by_id").text = str(user_id)
        SubElement(ad, "location", {"x": str(location.x), "y": str(location.y)})
        SubElement(ad, "is_expired").text = str(False)
        SubElement(ad, "is_redeemed").text = str(False)

        self.__max_ad_id += 1
        self.root.find("ads").append(ad)
        self.doc.write(self.xml_path)
        return self.get_advertisement(self.__max_ad_id - 1)

    def get_ad_category(self, id) -> AdvertisementCategory:
        category_element = self.root.find(f".//category[@id='{id}']")
        category_object = AdvertisementCategory(
            id=id,
            title=category_element.find("title").text
        )
        return category_object

    def add_ad_category(self, title) -> AdvertisementCategory:
        if not self.root.find("categories"):
            self.root.append(Element("categories"))
            self.doc.write(self.xml_path)

        category = Element("category")
        category.set("id", str(self.__max_category_id))
        SubElement(category, "title").text = title

        self.__max_category_id += 1
        self.root.find("categories").append(category)
        self.doc.write(self.xml_path)
        return self.get_ad_category(self.__max_category_id - 1)

    def get_question(self, id) -> Question:
        question_element = self.root.find(f".//question[@id='{id}']")
        question_object = Question(
            id=id,
            text=question_element.find("text").text,
            created_by_id=question_element.find("created_by_id").text,
            advertisement_id=question_element.find("advertisement_id").text,
            created_at=question_element.find("created_at").text,
        )
        return question_object

    def get_questions_by_ad_id(self, ad_id) -> list[Question] | None:
        questions_elements = self.root.findall(f".//question")
        questions_objects = []
        for question_element in questions_elements:
            if int(question_element.find("advertisement_id").text) == ad_id:
                question_object = Question(
                    id=int(question_element.attrib["id"]),
                    text=question_element.find("text").text,
                    created_by_id=question_element.find("created_by_id").text,
                    advertisement_id=question_element.find("advertisement_id").text,
                    created_at=question_element.find("created_at").text,
                )
                questions_objects.append(question_object)
        return questions_objects

    def add_question(self, text, ad_id, user_id) -> Question:
        if not self.root.find("questions"):
            self.root.append(Element("questions"))
            self.doc.write(self.xml_path)

        current_datetime = datetime.now()
        question = Element("question")
        question.set("id", str(self.__max_question_id))
        SubElement(question, "text").text = text
        SubElement(question, "created_by_id").text = str(user_id)
        SubElement(question, "advertisement_id").text = str(ad_id)
        SubElement(question, "created_at").text = str(current_datetime)

        self.__max_question_id += 1
        self.root.find("questions").append(question)
        self.doc.write(self.xml_path)
        return self.get_question(self.__max_question_id - 1)

    def get_answer(self, id) -> Answer:
        answer_element = self.root.find(f".//answer[@id='{id}']")
        answer_object = Answer(
            id=id,
            text=answer_element.find("text").text,
            created_by_id=int(answer_element.find("created_by_id").text),
            question_id=int(answer_element.find("question_id").text),
            created_at=datetime.fromisoformat(answer_element.find("created_at").text),
        )
        return answer_object

    def get_answers_by_question_id(self, question_id) -> list[Answer] | None:
        answers_elements = self.root.findall(f".//answer")
        answers_objects = []
        for answer_element in answers_elements:
            if int(answer_element.find("question_id").text) == question_id:
                answer_object = Answer(
                    id=int(answer_element.attrib["id"]),
                    text=answer_element.find("text").text,
                    created_by_id=int(answer_element.find("created_by_id").text),
                    question_id=int(answer_element.find("question_id").text),
                    created_at=datetime.fromisoformat(answer_element.find("created_at").text),
                )
                answers_objects.append(answer_object)
        return answers_objects

    def add_answer(self, text, question_id, user_id) -> Answer:
        if not self.root.find("answers"):
            self.root.append(Element("answers"))
            self.doc.write(self.xml_path)

        current_datetime = datetime.now()
        answer = Element("answer")
        answer.set("id", str(self.__max_answer_id))
        SubElement(answer, "text").text = text
        SubElement(answer, "created_by_id").text = str(user_id)
        SubElement(answer, "question_id").text = str(question_id)
        SubElement(answer, "created_at").text = str(current_datetime)

        self.__max_answer_id += 1
        self.root.find("answers").append(answer)
        self.doc.write(self.xml_path)
        return self.get_answer(self.__max_answer_id - 1)

    def get_deal(self, id) -> Deal:
        pass

    def get_deal_by_ad_id(self, ad_id) -> Deal:
        deal = self.root.find(f".//deal[@id='{ad_id}']")
        deal_object = Deal(
            ad_id=ad_id,
            redeemer_id=int(deal.find("redeemer_id").text),
            rating=float(deal.find("rating").text),
            text=deal.find("text").text,
            redeemed_at=datetime.fromisoformat(deal.find("redeemed_at").text),
        )
        return deal_object

    def add_deal(self, ad_id, redeemer_id, rating, text) -> Deal:
        if not self.root.find("deals"):
            self.root.append(Element("deals"))
            self.doc.write(self.xml_path)

        current_datetime = datetime.now()
        deal = Element("deal")
        deal.set("ad_id", str(self.__max_deal_id))
        SubElement(deal, "redeemer_id").text = str(redeemer_id)
        SubElement(deal, "rating").text = str(rating)
        SubElement(deal, "text").text = text
        SubElement(deal, "redeemed_at").text = str(current_datetime)

        self.__max_deal_id += 1
        self.root.find("deals").append(deal)
        self.doc.write(self.xml_path)
        return self.get_deal(self.__max_deal_id - 1)

from repositories.repository import Repository
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.dtos.user import User
from models.dtos.advertisement import Advertisement
from models.dtos.ad_category import AdvertisementCategory
from models.dtos.question import Question
from models.dtos.answer import Answer
from models.dtos.deal import Deal

class SQLAlchemyRepository(Repository):
    def __init__(self, session: Session):
        self.session = session

    def get_users(self):
        return self.session.query(User).all()

    def get_user(self, id):
        return self.session.query(User).get(id)

    def add_user(self, username, first_name, last_name, email, phone_number, birth_date):
        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            birth_date=datetime.strptime(birth_date, "%d.%m.%Y").date(),
            register_at=datetime.now())
        self.session.add(user)
        self.session.commit()
        return user

    def update_user(self, user_id, attrib, value):
        pass

    def get_advertisements(self):
        return self.session.query(Advertisement).all()

    def get_advertisement(self, id):
        return self.session.query(Advertisement).get(id)

    def get_advertisements_by_user_id(self, user_id):
        return self.session.query(Advertisement).filter(Advertisement.created_by_id == user_id).all()

    def add_advertisement(self, title, description, photo_url, category_id, price, validity, user_id, location):
        current_datetime = datetime.now()
        ad = Advertisement(
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
        )
        self.session.add(ad)
        self.session.commit()
        return ad

    def get_ad_category(self, id):
        return self.session.query(AdvertisementCategory).get(id)

    def add_ad_category(self, title):
        category = AdvertisementCategory(
            title=title
        )
        self.session.add(category)
        self.session.commit()
        return category

    def get_question(self, id):
        return self.session.query(Question).get(id)

    def get_questions_by_ad_id(self, ad_id):
        return self.session.query(Question).filter(Question.advertisement_id == ad_id).all()

    def add_question(self, text, ad_id, user_id):
        question = Question(
                text=text,
                created_by_id=user_id,
                advertisement_id=ad_id,
                created_at=datetime.now()
            )
        self.session.add(question)
        self.session.commit()
        return question

    def get_answer(self, id):
        return self.session.query(Answer).get(id)

    def get_answers_by_question_id(self, question_id):
        return self.session.query(Answer).filter(Answer.question_id == question_id).all()

    def add_answer(self, text, question_id, user_id):
        answer = Answer(
                text=text,
                created_by_id=user_id,
                question_id=question_id,
                created_at=datetime.now()
            )
        self.session.add(answer)
        self.session.commit()
        return answer

    def get_deal(self, id):
        return self.session.query(Deal).get(id)

    def get_deal_by_ad_id(self, ad_id):
        return self.session.query(Deal).filter(Deal.ad_id == ad_id).all()

    def add_deal(self, ad_id, redeemer_id, rating, text):
        deal = Deal(
            ad_id=ad_id,
            redeemer_id=redeemer_id,
            rating=rating,
            text=text,
            redeemed_at=datetime.now()
        )
        self.session.add(deal)
        self.session.commit()
        return deal
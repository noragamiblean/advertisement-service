from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.dtos.base import Base
from repositories.sql_repository import SQLAlchemyRepository
from services.user_service import UserService
from services.advertisement_service import AdvertisementService
from services.category_service import AdvertisementCategoryService
from services.question_service import QuestionService
from usecase.show_advertisement import ShowAdvertisement

def main():
    engine = create_engine("sqlite:///sql_repository.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session(bind=engine) as session:
        repository = SQLAlchemyRepository(session)
        repository.add_user(
            username="test",
            first_name="john",
            last_name="doe",
            email="test@gmail.com",
            phone_number="+79029474349",
            birth_date="19.12.2001"
        )
        repository.add_user(
            username="test2",
            first_name="jane",
            last_name="doe",
            email="test2@gmail.com",
            phone_number="+79029474349",
            birth_date="21.12.2001")
        repository.add_user(
            username="test3",
            first_name="tom",
            last_name="hanks",
            email="test3@gmail.com",
            phone_number="+79029412344",
            birth_date="5.12.2001"
        )
        repository.add_ad_category("Hardware")
        repository.add_advertisement(
            title="title1",
            description="desc1",
            photo_url="url1",
            category_id=1,
            price=500,
            validity=10,
            user_id=1,
            location=1
        )
        repository.add_advertisement(
            title="title2",
            description="desc2",
            photo_url="url2",
            category_id=1,
            price=750,
            validity=15,
            user_id=1,
            location=1
        )
        repository.add_advertisement(
            title="title3",
            description="desc3",
            photo_url="url3",
            category_id=1,
            price=150,
            validity=21,
            user_id=1,
            location=1
        )

    user_service = UserService(repository)
    ad_service = AdvertisementService(repository)
    question_service = QuestionService(repository)
    category_service = AdvertisementCategoryService(repository)

    question1 = question_service.ask_question(1, 3, "question text1?")
    question2 = question_service.ask_question(1, 3, "question text2?")
    question3 = question_service.ask_question(1, 3, "question text3?")
    answer1 = question_service.answer_question(question1.id, 1, "answer test1!")
    answer2 = question_service.answer_question(question3.id, 1, "answer test2!")

    ad_service.redeem_advertisement(1, 2, 1, 5, "text1")
    ad_service.redeem_advertisement(2, 2, 1, 4, "text2")

    show_advertisement = ShowAdvertisement(user_service, ad_service, question_service, category_service)
    show_advertisement.show_all_ads_by_user_id(1)

if __name__ == '__main__':
    main()

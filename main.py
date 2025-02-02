from repositories.fake_repository import FakeRepository
from models.location import Location
from services.question_service import QuestionService
from services.user_service import UserService
from services.advertisement_service import AdvertisementService

def main():
    repository = FakeRepository()

    user_service = UserService(repository)
    ad_service = AdvertisementService(repository)
    question_service = QuestionService(repository)

    repository.add_ad_category("Одежда")
    repository.add_ad_category("Техника")

    user1 = repository.add_user(
        username="test",
        first_name="john",
        last_name="doe",
        email="test@gmail.com",
        phone_number="+79029474349",
        birth_date="19.12.2001"
    )
    user2 = repository.add_user(
        username="test2",
        first_name="jane",
        last_name="doe",
        email="test2@gmail.com",
        phone_number="+79029474444",
        birth_date="21.12.2001"
    )
    user3 = repository.add_user(
        username="test3",
        first_name="tom",
        last_name="hanks",
        email="test3@gmail.com",
        phone_number="+79029412344",
        birth_date="5.12.2001"
    )

    ad1 = repository.add_advertisement(
        title="title1",
        description="desc1",
        photo_url="url1",
        category_id=1,
        price=500,
        validity=10,
        user_id=user1.id,
        location=Location(10, 15)
    )
    ad2 = repository.add_advertisement(
        title="title2",
        description="desc2",
        photo_url="url2",
        category_id=2,
        price=750,
        validity=15,
        user_id=user1.id,
        location=Location(10, 15)
    )
    ad3 = repository.add_advertisement(
        title="title3",
        description="desc3",
        photo_url="url3",
        category_id=1,
        price=150,
        validity=21,
        user_id=user2.id,
        location=Location(10, 21)
    )

    question1 = question_service.ask_question(ad1.id, user3.id, "question text1?")
    answer1 = question_service.answer_question(question1.id, user1.id, "answer test1!")

    ad_service.redeem_advertisement(ad1.id, user2.id, user1.id, 5, "text1")
    ad_service.redeem_advertisement(ad2.id, user2.id, user1.id, 4, "text2")

    print(repository.get_advertisements_by_user(0))


if __name__ == '__main__':
    main()

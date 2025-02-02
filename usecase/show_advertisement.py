from services.user_service import UserService
from services.advertisement_service import AdvertisementService
from services.question_service import QuestionService
from services.category_service import AdvertisementCategoryService

class ShowAdvertisement:
    def __init__(self, user_service: UserService,
                 ad_service: AdvertisementService,
                 question_service: QuestionService,
                 category_service: AdvertisementCategoryService):
        self.user_service = user_service
        self.ad_service = ad_service
        self.question_service = question_service
        self.category_service = category_service
        self.xl_divider = ("─" * 128)
        self.l_divider = ("-" * 128)
        self.s_divider = ("- " * 64)


    def show_all_ads_by_user_id(self, user_id):
        user = self.user_service.get_user(user_id)
        ads = self.user_service.get_ads_by_user_id(user_id)
        print(f"Объявления пользователя {user.username} | {user.first_name} {user.last_name} | Продано {user.sold} Выкуплено {user.bought} | Рейтинг {user.rating} Сред. {user.rating_avg}")
        for ad in ads:
            print(self.xl_divider)
            print(f"\nОбьявление №{ad.id} | Создано: {ad.created_at} | Обновлено: {ad.updated_at}|  Истекает: {ad.expired_at}"
                  f"\nНазвание: {ad.title}"
                  f"\nОписание: {ad.description}"
                  f"\nСсылка на фото: {ad.photo_url}"
                  f"\nКатегория: {self.category_service.get_category(ad.id).title}"
                  f"\nСтоимость выкупа: {ad.price}")
            if ad.is_expired:
                print(f"\nСРОК ВЫКУПА ИСТЕК")
            elif ad.is_redeemed:
                print(f"\n ВЫКУПЛЕНО")

            questions = self.ad_service.get_questions_by_ad_id(ad.id)
            for question in questions:
                print(self.l_divider)
                print(f"\nВопрос №{question.id} от пользователя {self.user_service.get_user(question.created_by_id).username} | Дата {question.created_at}"
                      f"\n{question.text}")

                answers = self.question_service.get_answers_by_question_id(question.id)
                for answer in answers:
                    print(self.s_divider)
                    print(f"\n\t Ответ №{answer.id} от пользователя {self.user_service.get_user(answer.created_by_id).username} | Дата {answer.created_at}"
                          f"\n\t {answer.text}")
from services.user_service import UserService
from services.advertisement_service import AdvertisementService
from services.question_service import QuestionService

class ShowAdvertisement:
    def __init__(self, user_service: UserService, ad_service: AdvertisementService, question_service: QuestionService):
        self.user_service = user_service
        self.ad_service = ad_service
        self.question_service = question_service

    def show_all_ads_by_user_id(self, user_id):
        pass
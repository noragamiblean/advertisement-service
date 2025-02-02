from repositories.repository import Repository
from models.question import Question
from models.deal import Deal

class AdvertisementService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_questions_by_ad_id(self, ad_id) -> list[Question] | None:
        result = self.repository.get_questions_by_ad_id(ad_id)
        if result is None:
            raise Exception("Под данным объявлением отсутствуют вопросы.")
        else:
            return result

    def redeem_advertisement(self, ad_id, redeemer_id, seller_id, rating, text ) -> Deal:
        ad = self.repository.get_advertisement(ad_id)
        redeemer = self.repository.get_user(redeemer_id)
        seller = self.repository.get_user(seller_id)

        if ad.is_expired:
            raise Exception("Срок выкупа объявления истек.")
        if ad.is_redeemed:
            raise Exception("Объявление уже выкуплено.")
        if ad.created_by_id == redeemer.id:
            raise Exception("Пользователь не может выкупить свое объявление.")
        else:
            ad.is_redeemed = True

            seller.sold += 1
            seller.rating += rating
            seller.rating_avg = seller.rating/seller.sold

            redeemer.bought += 1

            return self.repository.add_deal(ad.id, redeemer.id, rating, text)


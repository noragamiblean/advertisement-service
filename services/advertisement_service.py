from models.deal import Deal
from models.question import Question
from repositories.fake_repository import FakeRepository


def redeem_advertisement(ad_id, redeemer_id, seller_id, rating, text, repository: FakeRepository) -> Deal:
    ad = repository.get_advertisement(ad_id)
    redeemer = repository.get_user(redeemer_id)
    seller = repository.get_user(seller_id)

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

        return repository.add_deal(ad.id, redeemer.id, rating, text)

def ask_question(ad_id, user_id, text, repository: FakeRepository) -> Question:
    ad = repository.get_advertisement(ad_id)
    user = repository.get_user(user_id)

    if ad.is_expired:
        raise Exception("Вы не можете задавать вопрос под объявлением с истекшим сроком выкупа.")
    if ad.is_redeemed:
        raise Exception("Вы не можете задавать вопрос под выкупленным объявлением.")
    if ad.created_by_id == user.id:
        raise Exception("Вы не можете задавать вопрос к собственному объявлению.")
    else:
        return repository.add_question(text, ad.id, user.id)
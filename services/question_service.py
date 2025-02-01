from models.answer import Answer
from repositories.fake_repository import FakeRepository

def answer_question(question_id, user_id, text, repository: FakeRepository) -> Answer:
    question = repository.get_question(question_id)
    user = repository.get_user(user_id)
    ad = repository.get_advertisement(question.advertisement_id)

    if ad.is_expired:
        raise Exception("Вы не можете отвечать на вопрос под объявлением с истекшим сроком выкупа.")
    if ad.is_redeemed:
        raise Exception("Вы не можете отвечать на вопрос под выкупленным объявлением.")
    if question.created_by_id == user.id:
        raise Exception("Вы не можете отвечать на собственный вопрос.")
    if ad.created_by_id != user_id:
        raise Exception("Вы не можете отвечать на вопрос под чужим объявлением.")
    else:
        return repository.add_answer(text, question.id, user.id)
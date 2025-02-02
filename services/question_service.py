from models.question import Question
from models.answer import Answer
from repositories.repository import Repository


class QuestionService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_answers_by_question_id(self, question_id):
        result = self.repository.get_answers_by_question_id(question_id)
        if result is None:
            raise Exception("Под данным вопросом отсутсвуют ответы.")
        else:
            return result

    def ask_question(self, ad_id, user_id, text) -> Question:
        ad = self.repository.get_advertisement(ad_id)
        user = self.repository.get_user(user_id)

        if ad.is_expired:
            raise Exception("Вы не можете задавать вопрос под объявлением с истекшим сроком выкупа.")
        if ad.is_redeemed:
            raise Exception("Вы не можете задавать вопрос под выкупленным объявлением.")
        if ad.created_by_id == user.id:
            raise Exception("Вы не можете задавать вопрос к собственному объявлению.")
        else:
            return self.repository.add_question(text, ad.id, user.id)

    def answer_question(self, question_id, user_id, text) -> Answer:
        question = self.repository.get_question(question_id)
        user = self.repository.get_user(user_id)
        ad = self.repository.get_advertisement(question.advertisement_id)

        if ad.is_expired:
            raise Exception("Вы не можете отвечать на вопрос под объявлением с истекшим сроком выкупа.")
        if ad.is_redeemed:
            raise Exception("Вы не можете отвечать на вопрос под выкупленным объявлением.")
        if question.created_by_id == user.id:
            raise Exception("Вы не можете отвечать на собственный вопрос.")
        if ad.created_by_id != user_id:
            raise Exception("Вы не можете отвечать на вопрос под чужим объявлением.")
        else:
            return self.repository.add_answer(text, question.id, user.id)

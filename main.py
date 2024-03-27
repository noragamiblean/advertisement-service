from repository import AdvertisementServiceRepository


def main():
    repo = AdvertisementServiceRepository()

    user = repo.create_user("username", "tom", "hanks", "tom@gmail.com", "+1234454655", "10.12.1995")

    user_2 = repo.create_user("username2", "john", "doe", "john@gmail.com", "+1234454655", "10.12.2001")

    ad_1 = repo.create_ad("title", "desc", "URL", 1, 10, user)

    question_1 = repo.create_question("question text?", ad_1, user_2)
    answer_1 = repo.create_answer("answer text!", question_1, user)
    question_2 = repo.create_question("question text 2?", ad_1, user_2)
    answer_2 = repo.create_answer("answer text 2!", question_2, user)

    print(f"{ad_1.to_print()}")
    for question_id in ad_1.questions_ids:
        question = repo.get_question_by_id(question_id)
        print(f"\t{question.to_print()}")
        for answer_id in question.answers_ids:
            answer = repo.get_answer_by_id(answer_id)
            print(f"\t\t{answer.to_print()}")


if __name__ == '__main__':
    main()

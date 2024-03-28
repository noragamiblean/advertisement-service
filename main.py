from repository import AdvertisementServiceRepository


def main():
    repo = AdvertisementServiceRepository()

    user = repo.create_user("username", "tom", "hanks", "tom@gmail.com", "+1234454655", "10.12.1995")

    user_2 = repo.create_user("username2", "john", "doe", "john@gmail.com", "+1234454655", "10.12.2001")

    ad_1 = repo.create_ad("title", "desc", "URL", 1, 10, user)
    ad_2 = repo.create_ad("title 2", "desc 2", "URL 2", 3, 10, user)

    question_1 = repo.create_question("question text?", ad_1, user_2)
    answer_1 = repo.create_answer("answer text!", question_1, user)
    question_2 = repo.create_question("question text 2?", ad_1, user_2)
    answer_2 = repo.create_answer("answer text 2!", question_2, user)
    question_3 = repo.create_question("question text 3?", ad_2, user_2)
    answer_3 = repo.create_answer("answer text 3!", question_3, user)

    repo.print_user_ads(user)


if __name__ == '__main__':
    main()

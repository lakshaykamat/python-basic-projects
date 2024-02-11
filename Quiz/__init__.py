from Quiz.QuestionSet import QuestionSet,show_sets
from Quiz.User import User
from Quiz.quiz_data import get_question_set

if __name__ == '__main__':
    # Get user's name
    user_name = input("Enter your name: ")
    user = User(user_name)

    show_sets()

    # Choose a question set
    chosen_question_set_name = input("Choose any one question set: ")

    try:
        # Get the chosen question set
        quiz = get_question_set(QuestionSet[chosen_question_set_name])
    except KeyError:
        print("Invalid question set name. Exiting.")
        exit()

    # Take the quiz and get the user's result
    user_result = quiz.take_quiz()

    # Increment user's score for correct answers
    for ans in user_result:
        if ans is True:
            user.increment_score()

    # Display the user's score
    user.display_score(user_result)

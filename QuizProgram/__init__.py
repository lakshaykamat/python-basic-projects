from QuizProgram.QuestionSet import QuestionSet
from QuizProgram.User import User
from QuizProgram.quiz_data import get_question_set


def read_user_name():
    name = input("Enter your name: ")
    while len(name) <= 3:
        print("Name length should be greater than 3")
        name = input("Enter your name: ")
    return name


if __name__ == '__main__':
    user_name = read_user_name()  # Get user's name

    user = User(user_name)

    QuestionSet.show_sets()

    # Choose a question set
    chosen_question_set_name = input("Choose any one question set: ")
    try:
        # Get the chosen question set
        quiz = get_question_set(QuestionSet[chosen_question_set_name])
    except KeyError:
        print("Invalid question set name. Exiting.")
        exit()

    # Take the quiz and get the user's result in List of boolean
    user_result = quiz.take_quiz()

    # Increment user's score for correct answers
    for ans in user_result:
        if ans is True:
            user.increment_score()

    # Display the user's score
    user.display_score(user_result)

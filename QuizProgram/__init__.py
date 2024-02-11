import csv

from QuizProgram.QuestionSet import QuestionSet, show_sets
from QuizProgram.User import User
from QuizProgram.quiz_data import get_question_set


def load_questions(file_name):
    questions = []

    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header
        for row in csv_reader:
            question = {
                'Question': row[0],
                'Options': row[1:5],
                'CorrectIndex': int(row[5])
            }
            questions.append(question)

    print(questions)
    return question


if __name__ == '__main__':
    load_questions('QuizProgram/questions/general.csv')
    # Get user's name
    user_name = input("Enter your name: ")
    while len(user_name) <= 3:
        print("Name length should be greater than 3")
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

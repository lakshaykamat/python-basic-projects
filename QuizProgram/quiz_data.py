import csv

from QuizProgram.QuestionSet import QuestionSet
from QuizProgram.Quiz import Quiz

# Define a dictionary containing questions for each QuestionSet
questions_list = {
    QuestionSet.General: [
        ("What is the capital of France?", ["Paris", "Berlin", "London", "Rome"], 0),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 1),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], 1),
    ],
    QuestionSet.Music: [
        ("What is the capital of France?", ["Paris", "Berlin", "London", "Rome"], 0),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 1),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], 1),
    ]
}


def load_questions(file_name):
    questions = []

    with open(f"QuizProgram/questions/{file_name}", 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header
        for row in csv_reader:
            questions.append((row[0], row[1:5], int(row[5])))

    return questions


def get_question_set(prompt: QuestionSet):
    """
    Fetches questions list based on the given prompt (QuestionSet) and returns a Quizs instance.

    :param prompt: The QuestionSet for which questions are requested.
    :return: Quiz instance with questions for the specified QuestionSet.
    """

    all_questions = load_questions(prompt.value)

    # Create a Quiz instance with the questions for the specified QuestionSet
    quiz_instance = Quiz(questions=all_questions)
    return quiz_instance

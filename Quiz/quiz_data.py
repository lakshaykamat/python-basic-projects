from Quiz.QuestionSet import QuestionSet
from Quiz import QuizClass

# Define a dictionary containing questions for each QuestionSet
questions_list = {
    QuestionSet.General: (
        ("What is the capital of France?", ["Paris", "Berlin", "London", "Rome"], 0),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 1),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], 1),
    ),
    QuestionSet.Music: (
        ("What is the capital of France?", ["Paris", "Berlin", "London", "Rome"], 0),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 1),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], 1),
    )
}


def get_question_set(prompt):
    """
    Fetches questions list based on the given prompt (QuestionSet) and returns a Quizs instance.

    :param prompt: The QuestionSet for which questions are requested.
    :return: Quizs instance with questions for the specified QuestionSet.
    """
    # Create a Quizs instance with the questions for the specified QuestionSet
    quiz_instance = Quiz(questions_list[prompt])
    return quiz_instance

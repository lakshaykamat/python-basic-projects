from Quiz.QuizClass import QuizClass


class User:
    score = 0

    def __init__(self, name):
        self.name = name

    def increment_score(self):
        self.score += QuizClass.right_answer_point

    def decrement_score(self):
        if self.score > 0:
            self.score -= QuizClass.right_answer_point

    def display_score(self, user_result):
        total_questions = len(user_result)
        print(f"{self.name} has {self.score} out of {total_questions * QuizClass.right_answer_point}")
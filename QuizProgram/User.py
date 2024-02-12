from QuizProgram.Quiz import Quiz


class User:
    score = 0

    def __init__(self, name):
        self.name = name

    def increment_score(self):
        self.score += Quiz.get_answer_point()

    def decrement_score(self):
        if self.score > 0:
            self.score -= Quiz.get_answer_point()

    def display_score(self, user_result: list[bool]):
        total_questions = len(user_result)
        print(f"{self.name} has {self.score} out of {total_questions * Quiz.get_answer_point()}")

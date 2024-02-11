class QuizClass:
    # Class variable to define the points for a right answer
    right_answer_point = 5

    def __init__(self, questions):
        """
        Initialize the Quizs with a list of questions.
        Each question should be a tuple in the format:
        (question_text, options_list, correct_option_index)
        """
        self.questions = questions

    def display_question(self, question_number):
        """
        Display the question and options for the given question number.
        """
        question_text, options, _ = self.questions[question_number]
        print(f"{question_number + 1}. {question_text}")
        for i, option in enumerate(options, start=1):
            print(f"   {i}. {option}")

    def submit_answer(self, question_number, user_answer):
        """
        Submit the user's answer for the given question number and
        update the score if the answer is correct.
        """
        _, _, correct_option_index = self.questions[question_number]
        if user_answer == correct_option_index + 1:
            print("Correct!")
            return True
        else:
            print("Incorrect. The correct answer is:", correct_option_index + 1)
            return False

    def take_quiz(self):
        """
        Take the entire quiz, displaying questions one by one and
        allowing the user to submit answers.
        """
        result = []
        for question in range(len(self.questions)):
            self.display_question(question)
            user_answer = int(input("Your answer (enter the option number): "))
            # Submit the answer and store the result
            answer = self.submit_answer(question, user_answer)
            result.append(answer)

        return result

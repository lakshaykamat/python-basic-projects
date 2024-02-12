from enum import Enum


# Define an enumeration class for question sets
class QuestionSet(Enum):
    General = 'general.csv'
    Music = 'music.csv'

    @staticmethod
    def show_sets():
        """
        Display available question sets
        """
        print("Available question sets:")
        # Iterate over each enum member and print its name
        for question_set in QuestionSet:
            print(question_set.name)

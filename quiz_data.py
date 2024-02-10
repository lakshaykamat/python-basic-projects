from Quiz import Quiz

questions_list = {
    'general': (
        ("What is the capital of France?", ["Paris", "Berlin", "London", "Rome"], 0),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 1),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], 1),
    )
}

quiz_instance = Quiz(questions_list['general'])

# Project_03
import json
# Question bank
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
        "answer": 3
    },
    {
        "question": "Which programming language is known as the backbone of web development?",
        "options": ["1. Python", "2. JavaScript", "3. C++", "4. Java"],
        "answer": 2
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["1. Isaac Newton", "2. Nikola Tesla", "3. Albert Einstein", "4. Galileo Galilei"],
        "answer": 3
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["1. H2O", "2. O2", "3. CO2", "4. N2"],
        "answer": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
        "answer": 2
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["1. Atlantic Ocean", "2. Indian Ocean", "3. Arctic Ocean", "4. Pacific Ocean"],
        "answer": 4
    },
    {
        "question": "Which programming language is used for data analysis and visualization?",
        "options": ["1. Python", "2. C", "3. Java", "4. JavaScript"],
        "answer": 1
    },
    {
        "question": "What is 15 + 25?",
        "options": ["1. 30", "2. 35", "3. 40", "4. 50"],
        "answer": 3
    },
    {
        "question": "Which country is famous for the Great Wall?",
        "options": ["1. India", "2. China", "3. Japan", "4. Korea"],
        "answer": 2
    },
    {
        "question": "What does CPU stand for in computers?",
        "options": ["1. Central Processing Unit", "2. Central Program Unit", "3. Control Processing Unit", "4. Core Program Unit"],
        "answer": 1
    }
]

def ask_question(question):
    """Ask a question and get the user's answer."""
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    while True:
        try:
            user_answer = int(input("Enter the option number (1-4): "))
            if 1 <= user_answer <= 4:
                return user_answer
            else:
                print("Please select a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def run_quiz():
    """Run the quiz."""
    print("Welcome to the Quiz Application!")
    score = 0
    total_questions = len(questions)

    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}/{total_questions}")
        user_answer = ask_question(question)
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was option {question['answer']}.")

    print("\nQuiz Completed!")
    print(f"Your final score is {score}/{total_questions}.")
    percentage = (score / total_questions) * 100
    print(f"You scored {percentage:.2f}%.")

if __name__ == "__main__":
    run_quiz()

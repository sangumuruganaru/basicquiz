# Quiz data: list of tuples with questions and answers
quiz_data = [
    ("What is the capital of France?", "Paris"),
    ("What is 2 + 2?", "4"),
    ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("In which year did the Titanic sink?", "1912")
]

def ask_question(question, correct_answer):
    """
    Asks a single quiz question to the user and returns whether the user's answer was correct.

    Parameters:
        question (str): The question to ask.
        correct_answer (str): The correct answer to the question.

    Returns:
        bool: True if the user's answer was correct, False otherwise.
    """
    print(question)
    user_answer = input("Your answer: ").strip().lower()
    
    if user_answer == correct_answer.lower():
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect! The correct answer is {correct_answer}.\n")
        return False

def main():
    """
    Main function to run the quiz game.
    """
    score = 0
    
    for question, correct_answer in quiz_data:
        if ask_question(question, correct_answer):
            score += 1
    
    print(f"Your final score is {score} out of {len(quiz_data)}")

if __name__ == "__main__":
    main()






from typing import List
import time

class Quiz:
    def __init__(self) -> None:
        self.questions = []
        self.score = 0
    
    def add_question(self, question, options, answer):
        self.questions.append({
            "question": question,
            "options" :  options,
            "answer":answer
        })
    
    def display_welcome_message(self):
        print("Welcome to Console Based Quiz App")
        print("You have to chose one from (a, b, c, d)")
    

    def display_question(self, question_date):
        print(f"Question: {question_date["question"]}")

        for key, option in question_date["options"].items():
            print(f"{key} : {option}")

    def start_quiz(self):
        
        self.display_welcome_message()

        for question in self.questions:
            self.display_question(question)

            user_input = input("Yout answer: ")

            if user_input == question["answer"]:
                self.score+=1
            else:
                print("Wrong", question["answer"])
            time.sleep(1)
        self.display_results()
    

    def display_results(self):
        """Display the final results."""
        print("\nQuiz Over!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")

        if self.score == len(self.questions):
            print("Amazing! You got a perfect score! 🎉")
        elif self.score > len(self.questions) / 2:
            print("Great job! You did well. 👍")
        else:
            print("Don't worry, keep practicing! You'll improve. 😊")




if __name__ == '__main__':

    quiz = Quiz()


    quiz.add_question(
        "What is the output of 2 ** 3 in Python?",
        {"a": "6", "b": "8", "c": "9", "d": "10"},
        "b"
    )
    quiz.add_question(
        "Which data type is immutable in Python?",
        {"a": "List", "b": "Dictionary", "c": "Set", "d": "Tuple"},
        "d"
    )
    quiz.add_question(
        "What does the 'len()' function return?",
        {"a": "Length of a list", "b": "Number of elements", "c": "Both a and b", "d": "None of the above"},
        "c"
    )
    quiz.add_question(
        "Which keyword is used to define a function in Python?",
        {"a": "func", "b": "def", "c": "lambda", "d": "define"},
        "b"
    )
    quiz.add_question(
        "What is the purpose of the 'break' statement?",
        {"a": "Exit a loop", "b": "Skip an iteration", "c": "Stop execution", "d": "Restart the loop"},
        "a"
    )


    quiz.start_quiz()
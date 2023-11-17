import tkinter as tk
from PIL import Image, ImageTk

class GeoguesserGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Geoguesser Game")

        self.questions = [
            {
                "question": "What is the capital of Germany?",
                "options": ["1 - Berlin", "2 - Madrid", "3 - Paris", "4 - Rome"],
                "correct_answer": "1",
                "hint": "Chancellor Hitler's Capital",
                "attempts": 1,
                "penalty": 0,
            },
            {
                "question": "Which river is the longest in the world?",
                "options": ["1 - Amazon", "2 - Nile", "3 - Yangtze", "4 - Mississippi"],
                "correct_answer": "2",
                "hint": "It flows through northeastern Africa.",
                "attempts": 1,  # Optional: Set the maximum number of attempts
                "penalty": 0,   # Optional: Set the penalty for incorrect answers
            },
            {
                "question": "Greenland belongs to which country?",
                "options": ["1 - Russia", "2 - Canada", "3 - Denmark", "4 - USA"],
                "correct_answer": "3",
                "hint": "It's the biggest island on Earth.",
                "attempts": 1,  # Optional: Set the maximum number of attempts
                "penalty": 0,   # Optional: Set the penalty for incorrect answers
            },
            {
                "question": "Which country links the North and South America?",
                "options": ["1 - Gautemala", "2 - Panama", "3 - Suez", "4 - Peru"],
                "correct_answer": "2",
                "hint": "It's one of the busiest canals in the world.",
                "attempts": 1,  # Optional: Set the maximum number of attempts
                "penalty": 0,   # Optional: Set the penalty for incorrect answers
            },
            {
                "question": "Which country among these is not in Africa?",
                "options": ["1 - Algeria", "2 - Brazil", "3 - Sudan", "4 - Libya"],
                "correct_answer": "2",
                "hint": "Think about continents.",
                "attempts": 1,  # Optional: Set the maximum number of attempts
                "penalty": 0,   # Optional: Set the penalty for incorrect answers
            },
            {
                "question": "On which city, IST timings based for India?",
                "options": ["1 - Agra", "2 - Kolkata", "3 - Delhi", "4 - Allahabad", "5 - Mumbai"],
                "correct_answer": "4",
                "hint": "IST stands for Indian Standard Time.",
                "attempts": 1,  # Optional: Set the maximum number of attempts
                "penalty": 0,   # Optional: Set the penalty for incorrect answers
            },
            {
                "question": "India's only living volcano is in?",
                "options": ["1 - Minikoy", "2 - GangesDelta", "3 - Himalaya", "4 - BarrenIsland", "5 - LakshaDeep"],
                "correct_answer": "4",
                "hint": "Andaman Nicobar Islands",
                "attempts": 1,  # Optional: Set the maximum number of attempts
                "penalty": 0,   # Optional: Set the penalty for incorrect answers
            },
            {
                "question": "Which Among the following is the longest Railway route in the World? ",
                "options": ["1 - Trans-Siberian", "2 - RajdhaniExpressRoute", "3 - UK-RoyalRailway", "4 - Trans-Manchurian"],
                "correct_answer": "1",
                "hint": " ",
                "attempts": 1,  # Optional: Set the maximum number of attempts
                "penalty": 0,   # Optional: Set the penalty for incorrect answers
            },
            {
                "question": "Which continent have the most no. of countries",
                "options": ["1 - Asia", "2 - Africa", "3 - Europe", "4 - SouthAmerica"],
                "correct_answer": "2",
                "hint": " ",
                "attempts": 1,  # Optional: Set the maximum number of attempts
                "penalty": 0,   # Optional: Set the penalty for incorrect answers
            },
            {
                "question": "The Ancient University of Taxila was in today's ",
                "options": ["1 - India", "2 - Nepal", "3 - Pakistan", "4 - Bangladesh","5 - Tibet"],
                "correct_answer": "3",
                "hint": " ",
                "attempts": 1,  # Optional: Set the maximum number of attempts
                "penalty": 0,   # Optional: Set the penalty for incorrect answers
            }
            # Add other questions here
        ]

        self.score = 0
        self.current_question_index = 0
        self.remaining_attempts = 1

        self.setup_ui()

    def setup_ui(self):
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.question_label.pack(pady=10)

        self.options_label = tk.Label(self.root, text="", font=("Helvetica", 10))
        self.options_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.answer_entry.pack(pady=10)

        submit_img = Image.open("submit.png")
        submit_img = submit_img.resize((30, 30), Image.LANCZOS)  # Resize image if needed
        submit_img = ImageTk.PhotoImage(submit_img)
        
        self.submit_button = tk.Button(self.root, text="Submit Answer", command=self.check_answer, image=submit_img, font=("Helvetica", 12), compound=tk.LEFT)
        self.submit_button.image = submit_img
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Next Question", command=self.next_question, font=("Helvetica", 12))
        self.next_button.pack(pady=10)

        self.update_question()

    def update_question(self):
        if self.current_question_index < len(self.questions):
            current_question = self.questions[self.current_question_index]
            self.question_label.config(text=f"Question: {current_question['question']}")
            self.options_label.config(text=f"Options: {', '.join(current_question['options'])}")
            self.answer_entry.delete(0, tk.END)
            self.feedback_label.config(text="")
            self.remaining_attempts = current_question.get('attempts', 1)

        else:
            self.end_game()

    def check_answer(self):
        if self.current_question_index < len(self.questions):
            current_question = self.questions[self.current_question_index]
            user_answer = self.answer_entry.get().strip().lower()
            correct_answer = current_question["correct_answer"].lower()

            if user_answer == correct_answer:
                self.feedback_label.config(text="Correct! Well done.")
                self.score += 1
                self.remaining_attempts = 0
            else:
                self.feedback_label.config(text=f"Incorrect. Hint: {current_question['hint']}")
                #self.remaining_attempts -= 1
                self.score -= current_question.get('penalty', 0)

                if self.remaining_attempts == 0:
                    self.update_question()

    def next_question(self):
        if self.remaining_attempts == 0:
            self.current_question_index += 1
            self.update_question()

    def end_game(self):
        self.feedback_label.config(text=f"Game over! Your final score is: {self.score}/{len(self.questions)}")
        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    geoguesser_game = GeoguesserGame(root)
    root.mainloop()

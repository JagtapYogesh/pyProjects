from quiz_brain import QuizBrain
from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text="Score : 0", bg=THEME_COLOR, fg="white")
        self.question_canvas = Canvas(height=250, width=300)
        self.question_text = self.question_canvas.create_text(150, 125, text="Question text goes here", font=("Arial", 20, "italic"), width=280)

        right_button_photo = PhotoImage(file="images/true.png")
        wrong_button_photo = PhotoImage(file="images/false.png")
        self.right_button = Button(image=right_button_photo, highlightthickness=0, command=self.right_button_clicked)
        self.wrong_button = Button(image=wrong_button_photo, highlightthickness=0, command=self.wrong_button_clicked)

        self.score_label.grid(row=0, column=1)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=30)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You have reached the end of quiz")
            self.right_button.config(state="disable")
            self.wrong_button.config(state="disable")

    def right_button_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right)

    def wrong_button_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
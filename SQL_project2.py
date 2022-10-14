from SQL_project2_models import engine, Questions, Answers, QuestionHistory, \
    AnswerHistory, Player
from sqlalchemy.orm import sessionmaker
import datetime
import random
from tkinter import *
from tkinter import ttk, messagebox
from SQL_project2_control import *

Session = sessionmaker(bind=engine)
session = Session()


class MyButton(Button):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(
            bg="white",
            fg="black",
            font=("courier", 12, "bold"),
            relief="groove",
            height=4,
            width=20,
            activebackground="#0a0a0a",
            activeforeground="#e6d415",
        )


class MyLabel(Label):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(font=("courier", 22, "bold"))


class MyEntry(Entry):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(font=("courier", 14, "bold"), width=23)


class MyCheckbutton(Checkbutton):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(font=("courier", 22, "bold"))


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.currentPlayerID = IntVar()
        self.checkBox1 = IntVar()
        self.checkBox2 = IntVar()
        self.checkBox3 = IntVar()
        self.checkBox4 = IntVar()

        self.buttonGame = MyButton(text="Register",
                                   command=self.player_entry_fields)
        self.buttonTop10 = MyButton(text="Top Scores",
                                    command=self.top_10_table)
        self.buttonScoreHistory = MyButton(text="Score history",
                                           command=self.search_by_date)

        self.menu = Menu(master)
        self.master.config(menu=self.menu)
        self.submenu = Menu(self.menu, tearoff=False)

        self.menu.add_cascade(label="Menu", menu=self.submenu)
        self.submenu.add_separator()
        self.submenu.add_command(label="Exit", command=master.destroy)

        self.buttonGame.place(x=435, y=300, anchor="center")
        self.buttonTop10.place(x=635, y=300, anchor="center")
        self.buttonScoreHistory.place(x=835, y=300, anchor="center")

    def get_questions_answers(self):
        global answer
        global question
        self.answers, self.questions = shuffle_questions_answers()
        answer = iter(self.answers)
        question = iter(self.questions)

    def show_question(self):
        global questionText
        questionText = next(question)
        self.labelQuestion.config(text=questionText)

    def show_answers(self):
        global answerText
        answerText = next(answer).split(",")
        random.shuffle(answerText)
        self.answer1.config(text=answerText[0].lstrip(),
                            variable=self.checkBox1)
        self.answer2.config(text=answerText[1].lstrip(),
                            variable=self.checkBox2)
        self.answer3.config(text=answerText[2].lstrip(),
                            variable=self.checkBox3)
        self.answer4.config(text=answerText[3].lstrip(),
                            variable=self.checkBox4)

    def write_answers(self):
        self.choice = self.get_my_choice()
        write_answer_history(
            self.currentPlayerID.get(), get_question_id(questionText),
            self.choice
        )

    def get_my_choice(self):
        self.choice = ""
        if self.checkBox1.get() == 1:
            self.choice += answerText[0].lstrip() + ", "
        if self.checkBox2.get() == 1:
            self.choice += answerText[1].lstrip() + ", "
        if self.checkBox3.get() == 1:
            self.choice += answerText[2].lstrip() + ", "
        if self.checkBox4.get() == 1:
            self.choice += answerText[3].lstrip() + ", "
        return self.choice.rstrip(", ")

    def write_questions(self):
        self.score = self.get_answer_score()
        write_questions_history(
            self.currentPlayerID.get(), get_question_id(questionText),
            self.score
        )

    def get_my_answers_list(self):
        self.answerList = []
        self.myAnswer = self.get_my_choice()
        for i in self.myAnswer.split(","):
            self.answerList.append(i.lstrip())
        return self.answerList

    def get_correct_answer_list(self):
        self.correctAnswerList = []
        self.correctAnswer = get_correct_answer(get_question_id(questionText))
        for i in self.correctAnswer.split(","):
            self.correctAnswerList.append(i.lstrip())
        return self.correctAnswerList

    def get_answer_score(self):
        self.correctAnswer = self.get_correct_answer_list()
        self.myAnswer = self.get_my_answers_list()
        self.score = 0
        if all(i in self.correctAnswer for i in self.myAnswer):
            self.score = 1
        if len(self.correctAnswer) == 1:
            if sum(i in self.correctAnswer for i in
                   self.myAnswer) == 1 and len(self.myAnswer) == 2:
                self.score = 0.5
        elif len(self.correctAnswer) == 2:
            if sum(i in self.correctAnswer for i in
                   self.myAnswer) == 1 and len(self.myAnswer) == 1:
                score = 0.5
            elif sum(i in self.correctAnswer for i in
                     self.myAnswer) == 1 and len(self.myAnswer) == 2:
                self.score = 0.33
        elif len(self.correctAnswer) == 3:
            if sum(i in self.correctAnswer for i in
                   self.myAnswer) == 1 and len(self.myAnswer) == 1:
                self.score = 0.33
            elif sum(i in self.correctAnswer for i in
                     self.myAnswer) == 2 and len(self.myAnswer) == 2:
                self.score = 0.66
        elif len(self.correctAnswer) == 4:
            if sum(i in self.correctAnswer for i in
                   self.myAnswer) == 1 and len(self.myAnswer) == 1:
                self.score = 0.25
            elif sum(i in self.correctAnswer for i in self.myAnswer) == 2:
                if len(self.myAnswer) == 2:
                    self.score = 0.5
                elif len(self.myAnswer) == 3:
                    self.score = 0.33
            elif sum(i in self.correctAnswer for i in self.myAnswer) == 3:
                if len(self.myAnswer) == 3:
                    self.score = 0.75
                elif len(self.myAnswer) == 4:
                    self.score = 0.33
        return self.score

    def next_question(self):
        try:
            self.write_answers()
            self.write_questions()
            self.answer1.deselect()
            self.answer2.deselect()
            self.answer3.deselect()
            self.answer4.deselect()
            self.show_question()
            self.show_answers()
        except:
            self.buttonBack3 = MyButton(text="Back to Main menu",
                                        command=self.back_from_game)
            self.labelQuestion.place_forget()
            self.answer1.place_forget()
            self.answer2.place_forget()
            self.answer3.place_forget()
            self.answer4.place_forget()
            self.buttonNextQuestion.place_forget()
            self.final_score()
            self.results_table()
            self.buttonBack3.place(x=635, y=420, anchor="center")

    def final_score(self):
        self.labelFinalScore = MyLabel(
            text=f"Your final score is: {get_final_score(self.currentPlayerID.get())}/10"
        )
        self.labelFinalScore.place(x=650, y=50, anchor="center")

    def game_start(self):
        self.get_questions_answers()
        self.buttonBack2.place_forget()
        self.currentPlayerID.set(get_last_player_id())
        self.answer1 = MyCheckbutton()
        self.answer2 = MyCheckbutton()
        self.answer3 = MyCheckbutton()
        self.answer4 = MyCheckbutton()
        self.buttonNextQuestion = MyButton(text="Next",
                                           command=self.next_question)
        self.labelQuestion = MyLabel()
        self.answer1.place(x=100, y=300)
        self.answer2.place(x=400, y=300)
        self.answer3.place(x=700, y=300)
        self.answer4.place(x=1000, y=300)
        self.labelQuestion.place(x=635, y=100, anchor="center")
        self.buttonNextQuestion.place(x=635, y=470, anchor="center")
        self.show_question()
        self.show_answers()
        self.forget_player_entry_fields()
        self.buttonGame.place_forget()

    def forget_player_entry_fields(self):
        self.labelEditName.place_forget()
        self.labelEditLastName.place_forget()
        self.labelEditDate.place_forget()
        self.entryFieldName.place_forget()
        self.entryFieldLastName.place_forget()
        self.entryFieldDate.place_forget()

    def player_entry_fields(self):
        self.buttonTop10.place_forget()
        self.buttonScoreHistory.place_forget()
        self.buttonBack2 = MyButton(text="Back to Main menu",
                                    command=self.back_from_player)
        self.buttonGame.config(text="Start Game", command=self.player_entry)

        self.labelEditName = MyLabel(text="Enter name: ")
        self.labelEditLastName = MyLabel(text="Enter last name: ")
        self.labelEditDate = MyLabel(text="Date: ")

        self.entryFieldName = MyEntry()
        self.entryFieldLastName = MyEntry()
        self.entryFieldDate = MyEntry()
        self.entryFieldDate.insert(
            END, f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        )
        self.entryFieldDate.config(state="disabled")

        self.entryFieldName.place(x=300, y=0)
        self.entryFieldLastName.place(x=300, y=50)
        self.entryFieldDate.place(x=300, y=100)

        self.labelEditName.place(x=0, y=0)
        self.labelEditLastName.place(x=0, y=50)
        self.labelEditDate.place(x=0, y=100)

        self.buttonBack2.place(x=735, y=300, anchor="center")

    def search_by_date(self):
        self.labelEnterDateRange = MyLabel(
            text="Enter date range (YYYY-MM-DD):")
        self.entryFieldDate1 = MyEntry()
        self.entryFieldDate2 = MyEntry()
        self.labelDate1 = MyLabel(text="From:")
        self.labelDate2 = MyLabel(text="To:")
        self.buttonSearchByDate = MyButton(text="Search",
                                           command=self.search_date_table)
        self.buttonBack3 = MyButton(text="Back to Main menu",
                                    command=self.back_from_search)
        self.entryFieldDate1.place(x=300, y=100)
        self.entryFieldDate2.place(x=700, y=100)
        self.labelDate1.place(x=200, y=100)
        self.labelDate2.place(x=600, y=100)
        self.labelEnterDateRange.place(x=635, y=50, anchor="center")
        self.buttonSearchByDate.place(x=635, y=200, anchor="center")
        self.buttonBack3.place(x=1000, y=200)
        self.buttonGame.place_forget()
        self.buttonTop10.place_forget()
        self.buttonScoreHistory.place_forget()

    def player_entry(self):
        self.name = self.entryFieldName.get().capitalize()
        self.last_name = self.entryFieldLastName.get().capitalize()
        self.date = self.entryFieldDate.get()
        if self.name.lstrip() == "" or self.last_name == "":
            messagebox.showerror(title="Error",
                                 message="Incorrect data entered")
            self.forget_player_entry_fields()
            self.buttonBack2.place_forget()
            self.player_entry_fields()
        else:
            register_player(self.name, self.last_name, self.date)
            self.game_start()

    def results_table(self):
        self.tree1 = ttk.Treeview(column=("c1", "c2", "c3"), show="headings")
        self.tree1.column("#1", anchor=CENTER, width=500)
        self.tree1.heading("#1", text="Question")
        self.tree1.column("#2", anchor=CENTER, width=250)
        self.tree1.heading("#2", text="Chosen answer(-s)")
        self.tree1.column("#3", anchor=CENTER, width=250)
        self.tree1.heading("#3", text="Correct answer(-s)")
        self.tree1.place(x=625, y=250, anchor="center")
        self.rows = last_player_score(self.currentPlayerID.get())
        for row in self.rows:
            self.tree1.insert("", END, values=row)

    def top_10_table(self):
        self.buttonGame.place_forget()
        self.buttonTop10.place_forget()
        self.buttonScoreHistory.place_forget()
        self.buttonBack1 = MyButton(text="Back to Main menu",
                                    command=self.back_from_top)
        self.labelTop10 = MyLabel(text="Top 10 scores")
        self.buttonBack1.place(x=635, y=450, anchor="center")
        self.labelTop10.place(x=635, y=70, anchor="center")
        self.tree2 = ttk.Treeview(column=("c1", "c2", "c3", "c4"),
                                  show="headings")
        self.tree2.column("#1", anchor=CENTER, width=150)
        self.tree2.heading("#1", text="Date")
        self.tree2.column("#2", anchor=CENTER, width=150)
        self.tree2.heading("#2", text="Name")
        self.tree2.column("#3", anchor=CENTER, width=150)
        self.tree2.heading("#3", text="Last name")
        self.tree2.column("#4", anchor=CENTER, width=100)
        self.tree2.heading("#4", text="Score")
        self.tree2.place(x=625, y=250, anchor="center")
        self.rows = top_10_scores()
        for row in self.rows:
            self.tree2.insert("", END, values=row)

    def search_date_table(self):
        try:
            self.tree3.place_forget()
            self.tree3 = ttk.Treeview(column=("c1", "c2", "c3", "c4"),
                                      show="headings")
            self.tree3.column("#1", anchor=CENTER, width=150)
            self.tree3.heading("#1", text="Date")
            self.tree3.column("#2", anchor=CENTER, width=150)
            self.tree3.heading("#2", text="Name")
            self.tree3.column("#3", anchor=CENTER, width=150)
            self.tree3.heading("#3", text="Last name")
            self.tree3.column("#4", anchor=CENTER, width=100)
            self.tree3.heading("#4", text="Score")
            self.tree3.place(x=625, y=400, anchor="center")
            self.rows = get_date_range(self.entryFieldDate1.get(),
                                       self.entryFieldDate2.get())
            for row in self.rows:
                self.tree3.insert("", END, values=row)
        except:
            self.tree3 = ttk.Treeview(column=("c1", "c2", "c3", "c4"),
                                      show="headings")
            self.tree3.column("#1", anchor=CENTER, width=150)
            self.tree3.heading("#1", text="Date")
            self.tree3.column("#2", anchor=CENTER, width=150)
            self.tree3.heading("#2", text="Name")
            self.tree3.column("#3", anchor=CENTER, width=150)
            self.tree3.heading("#3", text="Last name")
            self.tree3.column("#4", anchor=CENTER, width=100)
            self.tree3.heading("#4", text="Score")
            self.tree3.place(x=625, y=400, anchor="center")
            self.rows = get_date_range(self.entryFieldDate1.get(),
                                       self.entryFieldDate2.get())
            for row in self.rows:
                self.tree3.insert("", END, values=row)

    def back_from_top(self):
        self.labelTop10.place_forget()
        self.tree2.place_forget()
        self.buttonBack1.place_forget()
        self.buttonGame.place(x=435, y=300, anchor="center")
        self.buttonTop10.place(x=635, y=300, anchor="center")
        self.buttonScoreHistory.place(x=835, y=300, anchor="center")

    def back_from_player(self):
        self.buttonGame.config(text="Register",
                               command=self.player_entry_fields)
        self.forget_player_entry_fields()
        self.buttonBack2.place_forget()
        self.buttonGame.place(x=435, y=300, anchor="center")
        self.buttonTop10.place(x=635, y=300, anchor="center")
        self.buttonScoreHistory.place(x=835, y=300, anchor="center")

    def back_from_game(self):
        self.labelFinalScore.place_forget()
        self.tree1.place_forget()
        self.buttonBack3.place_forget()
        self.buttonGame.config(text="Register",
                               command=self.player_entry_fields)
        self.buttonGame.place(x=435, y=300, anchor="center")
        self.buttonTop10.place(x=635, y=300, anchor="center")
        self.buttonScoreHistory.place(x=835, y=300, anchor="center")

    def back_from_search(self):
        try:
            self.tree3.place_forget()
            self.entryFieldDate1.place_forget()
            self.entryFieldDate2.place_forget()
            self.labelDate1.place_forget()
            self.labelDate2.place_forget()
            self.labelEnterDateRange.place_forget()
            self.buttonSearchByDate.place_forget()
            self.buttonBack3.place_forget()
            self.buttonGame.place(x=435, y=300, anchor="center")
            self.buttonTop10.place(x=635, y=300, anchor="center")
            self.buttonScoreHistory.place(x=835, y=300, anchor="center")
        except:
            self.entryFieldDate1.place_forget()
            self.entryFieldDate2.place_forget()
            self.labelDate1.place_forget()
            self.labelDate2.place_forget()
            self.labelEnterDateRange.place_forget()
            self.buttonSearchByDate.place_forget()
            self.buttonBack3.place_forget()
            self.buttonGame.place(x=435, y=300, anchor="center")
            self.buttonTop10.place(x=635, y=300, anchor="center")
            self.buttonScoreHistory.place(x=835, y=300, anchor="center")


def main():
    window = Tk()
    MainWindow(window)
    window.geometry("1270x550+520+400")
    window.resizable(False, False)
    window.title("Quiz Game")
    window.mainloop()


if __name__ == "__main__":
    main()

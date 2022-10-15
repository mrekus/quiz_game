import tkinter as tk
import Control
import Widgets
import Game
import random


class PlayGame:
    """
    Sukuria visus žaidimui naudojamus elementus bei metodus jiem
    valdyti.
    """
    def __init__(self, master):
        self.master = master

        self.currentPlayerID = tk.IntVar()
        self.checkBox1 = tk.IntVar()
        self.checkBox2 = tk.IntVar()
        self.checkBox3 = tk.IntVar()
        self.checkBox4 = tk.IntVar()

        self.buttonNextQuestion = Widgets.MyButton(
            text="Next", command=self.next_question
        )

        self.labelQuestion = Widgets.MyLabel()

        self.checkAnswer1 = Widgets.MyCheckbutton()
        self.checkAnswer2 = Widgets.MyCheckbutton()
        self.checkAnswer3 = Widgets.MyCheckbutton()
        self.checkAnswer4 = Widgets.MyCheckbutton()

        self.buttonNextQuestion.place(x=635, y=470, anchor="center")

        self.labelQuestion.place(x=635, y=100, anchor="center")

        self.checkAnswer1.place(x=100, y=300)
        self.checkAnswer2.place(x=400, y=300)
        self.checkAnswer3.place(x=700, y=300)
        self.checkAnswer4.place(x=1000, y=300)

        self.currentPlayerID.set(Control.get_last_player_id())

        self.answer, self.question = Control.get_questions_answers()
        self.show_question()
        self.show_answers()

    def next_question(self):
        """
        Įrašo žaidėjo klausimą bei atsakymą, parodo sekantį
        klausimą. Jei visi klausimai jau parodyti, sunaikina visus žaidimo
        elementus ir kviečia FinalScore langą.
        Returns: None

        """
        try:
            self.write_answers()
            self.write_questions()
            self.checkAnswer1.deselect()
            self.checkAnswer2.deselect()
            self.checkAnswer3.deselect()
            self.checkAnswer4.deselect()
            self.show_question()
            self.show_answers()
        except StopIteration:
            self.destroy_game_widgets()
            Game.FinalScore(self.master, self.currentPlayerID.get())

    def show_question(self):
        """
        Parodo sekantį klausimą.
        Returns: None

        """
        question_text = next(self.question)
        self.labelQuestion.config(text=question_text)

    def show_answers(self):
        """
        Parodo klausimo atsakymus juos pirma išmaišius.
        Returns: None

        """
        answer_text = next(self.answer).split(",")
        random.shuffle(answer_text)
        self.checkAnswer1.config(text=answer_text[0].lstrip(), variable=self.checkBox1)
        self.checkAnswer2.config(text=answer_text[1].lstrip(), variable=self.checkBox2)
        self.checkAnswer3.config(text=answer_text[2].lstrip(), variable=self.checkBox3)
        self.checkAnswer4.config(text=answer_text[3].lstrip(), variable=self.checkBox4)

    def write_answers(self):
        """
        Įrašo pasirinktus atsakymus į DB.
        Returns: None

        """
        choice = self.get_my_choice()
        Control.write_answer_history(
            self.currentPlayerID.get(),
            Control.get_question_id(self.labelQuestion["text"]),
            choice,
        )

    def get_my_choice(self):
        """
        Gauna visus checkbox pasirinkimus
        Returns: Pasirinktų checkbox sąrašą.

        """
        choice = ""
        if self.checkBox1.get() == 1:
            choice += self.checkAnswer1["text"] + ", "
        if self.checkBox2.get() == 1:
            choice += self.checkAnswer2["text"] + ", "
        if self.checkBox3.get() == 1:
            choice += self.checkAnswer3["text"] + ", "
        if self.checkBox4.get() == 1:
            choice += self.checkAnswer4["text"] + ", "
        return choice.rstrip(", ")

    def write_questions(self):
        """
        Įrašo klausimą į DB.
        Returns: None

        """
        score = self.get_answer_score()
        Control.write_questions_history(
            self.currentPlayerID.get(),
            Control.get_question_id(self.labelQuestion["text"]),
            score,
        )

    def get_answer_score(self):
        """
        Apskaičiuoja taškus priklausomai nuo pasirinktų atsakymų
        ir jų kiekio.
        Returns: Taškus už klausimą.

        """
        correct_answer = self.get_correct_answer_list()
        my_answer = self.get_my_answers_list()
        score = 0
        if all(i in correct_answer for i in my_answer):
            score = 1
        if len(correct_answer) == 1:
            if sum(i in correct_answer for i in my_answer) == 1 and len(my_answer) == 2:
                score = 0.5
        elif len(correct_answer) == 2:
            if sum(i in correct_answer for i in my_answer) == 1 and len(my_answer) == 1:
                score = 0.5
            elif (
                sum(i in correct_answer for i in my_answer) == 1 and len(my_answer) == 2
            ):
                score = 0.33
        elif len(correct_answer) == 3:
            if sum(i in correct_answer for i in my_answer) == 1 and len(my_answer) == 1:
                score = 0.33
            elif (
                sum(i in correct_answer for i in my_answer) == 2 and len(my_answer) == 2
            ):
                score = 0.66
        elif len(correct_answer) == 4:
            if sum(i in correct_answer for i in my_answer) == 1 and len(my_answer) == 1:
                score = 0.25
            elif sum(i in correct_answer for i in my_answer) == 2:
                if len(my_answer) == 2:
                    score = 0.5
                elif len(my_answer) == 3:
                    score = 0.33
            elif sum(i in correct_answer for i in my_answer) == 3:
                if len(my_answer) == 3:
                    score = 0.75
                elif len(my_answer) == 4:
                    score = 0.33
        return score

    def get_my_answers_list(self):
        """
        Gauna visus žaidėjo pasirinktus atsakymus
        į duotą klausimą.
        Returns: Pasirinktų atsakymų sąrašą.

        """
        answer_list = []
        my_answer = self.get_my_choice()
        for i in my_answer.split(","):
            answer_list.append(i.lstrip())
        return answer_list

    def get_correct_answer_list(self):
        """
        Gauna teisingus atsakymus į duotą klausimą.
        Returns: Teisingų atsakymų sąrašas

        """
        correct_answer_list = []
        correct_answer = Control.get_correct_answer(
            Control.get_question_id(self.labelQuestion["text"])
        )
        for i in correct_answer.split(","):
            correct_answer_list.append(i.lstrip())
        return correct_answer_list

    def destroy_game_widgets(self):
        """
        Sunaikina visus klasės sukurtus elementus.
        Returns: None

        """
        self.buttonNextQuestion.destroy()
        self.labelQuestion.destroy()
        self.checkAnswer1.destroy()
        self.checkAnswer2.destroy()
        self.checkAnswer3.destroy()
        self.checkAnswer4.destroy()

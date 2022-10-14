import tkinter as tk
from tkinter import ttk
from sqlalchemy.orm import sessionmaker
import Models
import Widgets
import Game
import Top10
import Search

Session = sessionmaker(bind=Models.engine)
session = Session()


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.buttonRegister = Widgets.MyButton(text="Register", command=self.register_frame)
        self.buttonTop10 = Widgets.MyButton(text="Top Scores", command=self.top_10_frame)
        self.buttonScoreHistory = Widgets.MyButton(text="Score history", command=self.score_history_frame)

        self.menu = tk.Menu(master)
        self.master.config(menu=self.menu)
        self.submenu = tk.Menu(self.menu, tearoff=False)

        self.menu.add_cascade(label="Menu", menu=self.submenu)
        self.submenu.add_separator()
        self.submenu.add_command(label="Exit", command=master.destroy)

        self.buttonRegister.place(x=435, y=300, anchor="center")
        self.buttonTop10.place(x=635, y=300, anchor="center")
        self.buttonScoreHistory.place(x=835, y=300, anchor="center")

    def register_frame(self):
        self.buttonRegister.destroy()
        self.buttonTop10.destroy()
        self.buttonScoreHistory.destroy()
        Game.Registration(self.master)

    def top_10_frame(self):
        self.buttonRegister.destroy()
        self.buttonTop10.destroy()
        self.buttonScoreHistory.destroy()
        Top10.TopScores(self.master)

    def score_history_frame(self):
        self.buttonRegister.destroy()
        self.buttonTop10.destroy()
        self.buttonScoreHistory.destroy()
        Search.FilteredSearch(self.master)


def main():
    window = tk.Tk()
    MainWindow(window)
    window.geometry("1270x550+520+400")
    window.resizable(False, False)
    window.title("Quiz Game")
    window.mainloop()


if __name__ == "__main__":
    main()

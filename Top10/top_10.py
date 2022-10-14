import tkinter as tk
from tkinter import ttk
import Widgets
import Control
import Main


class TopScores:
    def __init__(self, master):
        self.master = master

        self.tree = ttk.Treeview(columns=("c1", "c2", "c3", "c4"), show="headings")
        self.tree.column("#1", anchor=tk.CENTER, width=150)
        self.tree.heading("#1", text="Date")
        self.tree.column("#2", anchor=tk.CENTER, width=150)
        self.tree.heading("#2", text="Name")
        self.tree.column("#3", anchor=tk.CENTER, width=150)
        self.tree.heading("#3", text="Last name")
        self.tree.column("#4", anchor=tk.CENTER, width=100)
        self.tree.heading("#4", text="Score")
        self.tree.place(x=625, y=250, anchor="center")
        self.rows = Control.top_10_scores()
        for row in self.rows:
            self.tree.insert("", tk.END, values=row)

        self.buttonBack = Widgets.MyButton(text="Back to Main menu", command=self.back_from_top)
        self.labelTop10 = Widgets.MyLabel(text="Top 10 scores")

        self.buttonBack.place(x=635, y=450, anchor="center")
        self.labelTop10.place(x=635, y=70, anchor="center")

    def back_from_top(self):
        self.labelTop10.destroy()
        self.tree.destroy()
        self.buttonBack.destroy()
        Main.MainWindow(self.master)

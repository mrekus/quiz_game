from tkinter import ttk
import tkinter as tk
import Control
import Widgets
import Main


class FinalScore:
    """
    Sukuria ir valdo galutinio rezultato lango po žaidimo elementus.
    """
    def __init__(self, master, player_id):
        self.master = master
        self.player_id = player_id

        self.tree = ttk.Treeview(columns=("c1", "c2", "c3"), show="headings")
        self.tree.column("#1", anchor=tk.CENTER, width=500)
        self.tree.heading("#1", text="Question")
        self.tree.column("#2", anchor=tk.CENTER, width=250)
        self.tree.heading("#2", text="Chosen answer(-s)")
        self.tree.column("#3", anchor=tk.CENTER, width=250)
        self.tree.heading("#3", text="Correct answer(-s)")
        self.rows = Control.last_player_score(self.player_id)
        for row in self.rows:
            self.tree.insert("", tk.END, values=row)

        self.labelFinalScore = Widgets.MyLabel(
            text=f"Your final score is: {Control.get_final_score(self.player_id)}/10"
        )
        self.buttonBack = Widgets.MyButton(
            text="Back to Main menu", command=self.back_from_final_score
        )

        self.labelFinalScore.place(x=650, y=50, anchor="center")
        self.buttonBack.place(x=635, y=470, anchor="center")
        self.tree.place(x=625, y=250, anchor="center")

    def back_from_final_score(self):
        """
        Sunaikina visus lango sukurtus elementus, iškviečia pradinį
        programos langą.
        Returns: None

        """
        self.labelFinalScore.destroy()
        self.tree.destroy()
        self.buttonBack.destroy()
        Main.MainWindow(self.master)

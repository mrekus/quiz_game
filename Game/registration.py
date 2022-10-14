import Widgets
import datetime
import tkinter as tk
from tkinter import messagebox
import Main
import Control
import Game


class Registration:
    def __init__(self, master):
        self.master = master

        self.buttonBack = Widgets.MyButton(
            text="Back to Main menu", command=self.back_from_registration
        )
        self.buttonGame = Widgets.MyButton(
            text="Start Game", command=self.register_player
        )

        self.labelEditName = Widgets.MyLabel(text="Enter name: ")
        self.labelEditLastName = Widgets.MyLabel(text="Enter last name: ")
        self.labelEditDate = Widgets.MyLabel(text="Date: ")

        self.entryFieldName = Widgets.MyEntry()
        self.entryFieldLastName = Widgets.MyEntry()
        self.entryFieldDate = Widgets.MyEntry()
        self.entryFieldDate.insert(
            tk.END, f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        )

        self.buttonBack.place(x=835, y=300, anchor="center")
        self.buttonGame.place(x=435, y=300, anchor="center")

        self.labelEditName.place(x=0, y=0)
        self.labelEditLastName.place(x=0, y=50)
        self.labelEditDate.place(x=0, y=100)

        self.entryFieldName.place(x=300, y=0)
        self.entryFieldLastName.place(x=300, y=50)
        self.entryFieldDate.place(x=300, y=100)
        self.entryFieldDate.config(state="disabled")

    def register_player(self):
        name = self.entryFieldName.get().capitalize()
        last_name = self.entryFieldLastName.get().capitalize()
        date = datetime.datetime.strptime(self.entryFieldDate.get(), "%Y-%m-%d %H:%M:%S")
        if name.strip() == "" or last_name.strip() == "":
            messagebox.showerror(title="Error", message="Incorrect data entered")
        else:
            Control.register_player(name, last_name, date)
            self.start_game()

    def start_game(self):
        self.forget_player_entry_fields()
        Game.PlayGame(self.master)

    def forget_player_entry_fields(self):
        self.labelEditName.destroy()
        self.labelEditLastName.destroy()
        self.labelEditDate.destroy()
        self.entryFieldName.destroy()
        self.entryFieldLastName.destroy()
        self.entryFieldDate.destroy()

        self.buttonBack.destroy()
        self.buttonGame.destroy()

    def back_from_registration(self):
        self.forget_player_entry_fields()
        Main.MainWindow(self.master)

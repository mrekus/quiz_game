import tkinter as tk
from tkinter import ttk


class MyButton(tk.Button):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(
            bg="white",
            fg="black",
            font=("courier", 12, "bold"),
            relief="groove",
            height=4,
            width=20,
            activebackground="#75C1BF",
            activeforeground="#e6d415",
        )
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, _event):
        self["background"] = self["activebackground"]

    def on_leave(self, _event):
        self["background"] = self.defaultBackground


class MyLabel(tk.Label):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(font=("courier", 22, "bold"))


class MyEntry(tk.Entry):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(font=("courier", 14, "bold"), width=23)


class MyCheckbutton(tk.Checkbutton):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(font=("courier", 22, "bold"))


class MyCombobox(ttk.Combobox):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(width=10, font=("courier", 15, "bold"), state="readonly")

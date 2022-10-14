import tkinter as tk


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
            activebackground="#0a0a0a",
            activeforeground="#e6d415",
        )


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

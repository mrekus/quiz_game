import Widgets
import Control
import Main
from datetime import datetime
import tkinter as tk
from tkinter import ttk


class FilteredSearch:
    def __init__(self, master):
        self.master = master

        self.year_list_from = Widgets.MyCombobox(
            values=["2022", "2023", "2024", "2025"]
        )
        self.month_list_from = Widgets.MyCombobox(
            values=["0" + str(i) if len(str(i)) <= 1 else str(i) for i in range(1, 13)],
        )
        self.day_list_from = Widgets.MyCombobox(values=[str(i) for i in range(1, 32)])
        self.year_list_to = Widgets.MyCombobox(values=["2022", "2023", "2024", "2025"])
        self.month_list_to = Widgets.MyCombobox(
            values=["0" + str(i) if len(str(i)) <= 1 else str(i) for i in range(1, 13)],
        )
        self.day_list_to = Widgets.MyCombobox(values=[str(i) for i in range(1, 32)])
        self.year_list_from.set("2022")
        self.month_list_from.set("01")
        self.day_list_from.set("1")
        self.year_list_to.set(str(datetime.now().year))
        self.month_list_to.set(str(datetime.now().month))
        self.day_list_to.set(str(datetime.now().day))

        self.labelEnterDateRange = Widgets.MyLabel(
            text="Filter scores by date:"
        )
        self.labelFrom = Widgets.MyLabel(text="From:")
        self.labelTo = Widgets.MyLabel(text="To:")

        self.buttonBack = Widgets.MyButton(
            text="Back to Main menu", command=self.back_from_search
        )

        self.tree = ttk.Treeview(columns=("c1", "c2", "c3", "c4"), show="headings")
        self.tree.column("#1", anchor=tk.CENTER, width=150)
        self.tree.heading("#1", text="Date")
        self.tree.column("#2", anchor=tk.CENTER, width=150)
        self.tree.heading("#2", text="Name")
        self.tree.column("#3", anchor=tk.CENTER, width=150)
        self.tree.heading("#3", text="Last name")
        self.tree.column("#4", anchor=tk.CENTER, width=100)
        self.tree.heading("#4", text="Score")

        self.labelEnterDateRange.place(x=635, y=50, anchor="center")
        self.buttonBack.place(x=1000, y=200)
        self.tree.place(x=625, y=400, anchor="center")
        self.labelFrom.place(x=400, y=100)
        self.labelTo.place(x=700, y=100)
        self.year_list_from.place(x=400, y=150)
        self.month_list_from.place(x=400, y=200)
        self.day_list_from.place(x=400, y=250)
        self.year_list_to.place(x=700, y=150)
        self.month_list_to.place(x=700, y=200)
        self.day_list_to.place(x=700, y=250)

        self.year_list_from.bind("<<ComboboxSelected>>", self.refresh_table)
        self.month_list_from.bind("<<ComboboxSelected>>", self.refresh_table)
        self.day_list_from.bind("<<ComboboxSelected>>", self.refresh_table)
        self.year_list_to.bind("<<ComboboxSelected>>", self.refresh_table)
        self.month_list_to.bind("<<ComboboxSelected>>", self.refresh_table)
        self.day_list_to.bind("<<ComboboxSelected>>", self.refresh_table)
        self.year_list_to.event_generate("<<ComboboxSelected>>")

    def refresh_table(self, _event):
        for i in self.tree.get_children():
            self.tree.delete(i)
        date_from = (
            f"{self.year_list_from.get()}"
            f"-{self.month_list_from.get()}"
            f"-{self.day_list_from.get()} 00:00:01"
        )
        date_to = (
            f"{self.year_list_to.get()}"
            f"-{self.month_list_to.get()}"
            f"-{self.day_list_to.get()} 23:59:59"
        )
        try:
            date_from = datetime.strptime(date_from, "%Y-%m-%d %H:%M:%S")
            date_to = datetime.strptime(date_to, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            pass
        rows = Control.get_date_range(
            date_from, date_to
        )
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def destroy_widgets(self):
        self.labelFrom.destroy()
        self.labelTo.destroy()
        self.labelEnterDateRange.destroy()
        self.buttonBack.destroy()
        self.year_list_from.destroy()
        self.month_list_from.destroy()
        self.day_list_from.destroy()
        self.year_list_to.destroy()
        self.month_list_to.destroy()
        self.day_list_to.destroy()
        self.tree.destroy()

    def back_from_search(self):
        self.destroy_widgets()
        Main.MainWindow(self.master)

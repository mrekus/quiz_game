from Widgets import *


def search_by_date(self):
    self.labelEnterDateRange = MyLabel(text="Enter date range (YYYY-MM-DD):")
    self.entryFieldDate1 = MyEntry()
    self.entryFieldDate2 = MyEntry()
    self.labelDate1 = MyLabel(text="From:")
    self.labelDate2 = MyLabel(text="To:")
    self.buttonSearchByDate = MyButton(text="Search", command=self.search_date_table)
    self.buttonBack3 = MyButton(text="Back to Main menu", command=self.back_from_search)
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


def search_date_table(self):
    try:
        self.tree3.place_forget()
        self.tree3 = ttk.Treeview(column=("c1", "c2", "c3", "c4"), show="headings")
        self.tree3.column("#1", anchor=CENTER, width=150)
        self.tree3.heading("#1", text="Date")
        self.tree3.column("#2", anchor=CENTER, width=150)
        self.tree3.heading("#2", text="Name")
        self.tree3.column("#3", anchor=CENTER, width=150)
        self.tree3.heading("#3", text="Last name")
        self.tree3.column("#4", anchor=CENTER, width=100)
        self.tree3.heading("#4", text="Score")
        self.tree3.place(x=625, y=400, anchor="center")
        self.rows = get_date_range(
            self.entryFieldDate1.get(), self.entryFieldDate2.get()
        )
        for row in self.rows:
            self.tree3.insert("", END, values=row)
    except:
        self.tree3 = ttk.Treeview(column=("c1", "c2", "c3", "c4"), show="headings")
        self.tree3.column("#1", anchor=CENTER, width=150)
        self.tree3.heading("#1", text="Date")
        self.tree3.column("#2", anchor=CENTER, width=150)
        self.tree3.heading("#2", text="Name")
        self.tree3.column("#3", anchor=CENTER, width=150)
        self.tree3.heading("#3", text="Last name")
        self.tree3.column("#4", anchor=CENTER, width=100)
        self.tree3.heading("#4", text="Score")
        self.tree3.place(x=625, y=400, anchor="center")
        self.rows = get_date_range(
            self.entryFieldDate1.get(), self.entryFieldDate2.get()
        )
        for row in self.rows:
            self.tree3.insert("", END, values=row)


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

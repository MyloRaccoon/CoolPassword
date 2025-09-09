import tkinter as tk
import tkinter.ttk as ttk

from scenes.model import loger
from .model import master_key
from .home import HomeScene


class LoginScene:

    def __init__(self, app):
        self.app = app

        self.lbl_title = ttk.Label(app, text="Welcome back !")

        self.lbl_info = ttk.Label(app, text="Please enter your master key")
        self.lbl_error = ttk.Label(app, text="")
        self.entry = ttk.Entry(app, show="*")
        self.entry.bind("<Return>", self.login)
        self.btn_log = ttk.Button(
            app, text="▶", command=lambda: self.login(), style="Main.TButton"
        )

    def show(self):
        self.lbl_title.grid(pady=20)

        self.lbl_info.grid(row=1)
        self.entry.grid(row=2)
        self.btn_log.grid(row=2, column=1)
        self.lbl_error.grid(row=3)

    def hide(self):
        self.lbl_title.grid_forget()
        self.lbl_info.grid_forget()
        self.entry.grid_forget()
        self.btn_log.grid_forget()
        self.lbl_error.grid_forget()

    def login(self, event=None):
        self.lbl_error.config(text="")
        pwd = self.entry.get()
        self.entry.delete(0, tk.END)

        if master_key.check(pwd):
            loger.login()
            self.hide()
            HomeScene(self.app, self.show).show()
        else:
            self.lbl_error.config(text="Master key incorrect")

import tkinter as tk
import tkinter.ttk as ttk
from typing import Callable

from scenes import style
from scenes.ask_key import AskKeyScene
from scenes.load_save import LoadScene
from scenes.model import loger
from scenes.model import save
from scenes.model.files import KEY_FILE, SAVE_FILE
from scenes.model.save import nuke
from scenes.site_list import SiteList
from .model import passwords


class HomeScene:

    def __init__(self, app, loopback):
        passwords.load()

        self.app = app

        self.btn_logout = ttk.Button(
            app, text="⇱", command=lambda: self.logout(loopback), style="Main.TButton"
        )

        self.search_canvas = tk.Canvas(
            app,
            bg=style.Color.DARKEST,
            borderwidth=0,
            relief="flat",
            highlightthickness=0,
        )

        self.search_lbl = ttk.Label(self.search_canvas, text="Search a site")
        self.search_entry = ttk.Entry(self.search_canvas)
        self.search_entry.bind("<Key>", self.on_filter)

        self.search_lbl.grid(padx=10)
        self.search_entry.grid(row=0, column=1)

        self.sites_canvas = tk.Canvas(
            app,
            bg=style.Color.DARKEST,
            borderwidth=0,
            relief="flat",
            highlightthickness=0,
        )
        self.site_list = SiteList(self.sites_canvas)

        self.site_max_lenght = 20
        self.add_canvas = tk.Canvas(
            app,
            bg=style.Color.DARKEST,
            borderwidth=0,
            relief="flat",
            highlightthickness=0,
        )

        self.add_lbl = ttk.Label(self.add_canvas, text="Add a new site")
        self.add_entry = ttk.Entry(self.add_canvas)
        self.add_entry.bind("<Return>", self.add_site)
        self.add_btn = ttk.Button(
            self.add_canvas,
            text="✚",
            command=lambda: self.add_site(),
            style="Main.TButton",
        )
        self.add_error = ttk.Label(self.add_canvas, text="")

        self.add_lbl.grid(padx=5)
        self.add_entry.grid(row=0, column=1, padx=5)
        self.add_btn.grid(row=0, column=2)
        self.add_error.grid(row=1, pady=5)

        self.save_canvas = tk.Canvas(
            app,
            bg=style.Color.DARKEST,
            borderwidth=0,
            relief="flat",
            highlightthickness=0,
        )

        self.export_btn = ttk.Button(
            self.save_canvas,
            text="🖫",
            command=lambda: self.export_confirm(),
            style="Main.TButton",
        )
        self.import_btn = ttk.Button(
            self.save_canvas,
            text="🗎",
            command=lambda: self.go_to_import(),
            style="Main.TButton",
        )

        self.export_btn.grid()
        self.import_btn.grid(row=0, column=1, padx=3)

        self.nuke_btn = ttk.Button(
            app, text="☢", command=lambda: self.nuke_confirm(), style="Main.TButton"
        )

    def show(self):
        self.save_canvas.pack(side=tk.LEFT, anchor="nw")

        self.btn_logout.pack(side=tk.RIGHT, anchor="ne")

        self.search_canvas.pack(pady=10)

        self.site_list.show()
        self.sites_canvas.pack()

        self.add_canvas.pack(pady=10)

        self.nuke_btn.pack(side=tk.RIGHT, anchor="se")

    def hide(self):
        self.btn_logout.pack_forget()

        self.search_canvas.pack_forget()

        self.site_list.hide()
        self.sites_canvas.pack_forget()

        self.add_canvas.pack_forget()

        self.save_canvas.pack_forget()

        self.nuke_btn.pack_forget()

    def reload(self):
        self.hide()
        self.show()

    def on_filter(self, event=None):
        self.site_list.reload(self.search_entry.get())

    def add_site(self, event=None):
        self.add_error.config(text="")
        new_site = self.add_entry.get()
        if (
            len(new_site) > 0
            and len(new_site) < self.site_max_lenght
            and passwords.SEPARATOR not in new_site
        ):
            passwords.new(new_site)
            self.reload()
        elif passwords.SEPARATOR in new_site:
            self.add_error.config(text='Site name can\'t contain "|"')
        elif len(new_site) >= self.site_max_lenght:
            self.add_error.config(text="Site name too long, sorry")
        self.add_entry.delete(0, tk.END)

    def logout(self, loopback: Callable):
        loger.logout()
        self.hide()
        loopback()

    def export_confirm(self):
        self.hide()
        on_ok = self.export
        on_cancel = self.show
        msg = f"""
        Export a save files

Continuing will create two file in your home directory:
    - {SAVE_FILE}: 
        contains all the data to save
        (your master key, the sites, and your seed)
    - {KEY_FILE}: 
        contains the key to read the file below
You then can import them to any new Cool Password instance 
or one where you now the current master key.
    """
        AskKeyScene(self.app, on_cancel, on_ok, msg).show()

    def export(self):
        save.save()
        self.show()

    def go_to_import(self):
        self.hide()
        on_ok = LoadScene(self.app, self.show, self.show).show
        on_cancel = self.show
        AskKeyScene(self.app, on_cancel, on_ok).show()

    def nuke_confirm(self):
        self.hide()
        AskKeyScene(
            self.app,
            self.show,
            self.nuke,
            """
        ☢ Nuke Cool Password ☢

You are going to nuke this Cool Password instance.
    - your master key will be lost
    - all your registered sites will be lost
    - your seed will be lost
You won't be able to get back your passwords
unless your saved everything with the "🖫" button.
Continuing will quit the application but do not worry about that
            """,
        ).show()

    def nuke(self):
        nuke()
        self.app.quit()

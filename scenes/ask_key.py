import tkinter as tk
from tkinter import ttk

from scenes import style
from scenes.model import master_key


class AskKeyScene:

    def __init__(self, app, on_cancel, on_ok, msg=''):
        self.on_ok = on_ok

        self.lbl_msg = ttk.Label(app, text=msg)

        self.lbl = ttk.Label(app, text="Please enter your master key")
        self.entry = ttk.Entry(app, show="*")
        self.entry.bind("<Return>", self.ok)
        self.error_lbl = ttk.Label(app)

        self.btns_canvas = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)
        self.btn_cancel = ttk.Button(self.btns_canvas, text="⤶", command= lambda: [self.hide(), on_cancel()], style="Main.TButton")
        self.btn_ok = ttk.Button(self.btns_canvas, text="OK", command= lambda: self.ok(), style="Main.TButton")
        self.btn_ok.grid(padx=10)
        self.btn_cancel.grid(row=0, column=1)

    def show(self):
        self.entry.delete(0, tk.END)
        self.error_lbl.config(text="")

        self.lbl_msg.pack()

        self.lbl.pack()
        self.entry.pack()
        self.error_lbl.pack()
        self.btns_canvas.pack()

    def hide(self):
        self.lbl_msg.pack_forget()

        self.lbl.pack_forget()
        self.entry.pack_forget()
        self.error_lbl.pack_forget()
        self.btns_canvas.pack_forget()

    def ok(self, event=None):
        self.error_lbl.config(text="")
        mkey = self.entry.get()
        self.entry.delete(0, tk.END)
        
        if not master_key.check(mkey):
            self.error_lbl.config(text="Master key incorrect")
        else:
            self.hide()
            self.on_ok()
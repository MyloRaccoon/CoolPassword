import tkinter as tk
from tkinter import ttk

from scenes.model import master_key


class AskKeyScene:

	def __init__(self, app, on_cancel, on_ok):
		
		self.lbl = ttk.Label(app, text="Please enter your master key")
		self.entry = ttk.Entry(app, show="*")
		self.error_lbl = ttk.Label(app)
		self.btn_cancel = ttk.Button(app, text="⤶", command= lambda: [self.hide(), on_cancel()])
		self.btn_ok = ttk.Button(app, text="OK", command= lambda: self.ok(on_ok))

	def show(self):
		self.entry.delete(0, tk.END)
		self.error_lbl.config(text="")

		self.lbl.pack()
		self.entry.pack()
		self.error_lbl.pack()
		self.btn_ok.pack()
		self.btn_cancel.pack()

	def hide(self):
		self.lbl.pack_forget()
		self.entry.pack_forget()
		self.error_lbl.pack_forget()
		self.btn_ok.pack_forget()
		self.btn_cancel.pack_forget()

	def ok(self, on_ok):
		self.error_lbl.config(text="")
		mkey = self.entry.get()
		self.entry.delete(0, tk.END)
		
		if not master_key.check(mkey):
			self.error_lbl.config(text="Master key incorrect")
		else:
			self.hide()
			on_ok()
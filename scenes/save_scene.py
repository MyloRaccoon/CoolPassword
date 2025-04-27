import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from pathlib import Path

from scenes.model import master_key, save

class SaveScene:

	def __init__(self, app, loopback):
		self.app = app
		self.return_btn = ttk.Button(app, text="⤶", command=lambda loopback=loopback: self.cancel(loopback))
		self.title_lbl = ttk.Label(app, text="Export a save files")
		self.please_lbl = ttk.Label(app, text="please enter your master key")
		self.key_entry = ttk.Entry(app, show='*')
		self.btn = ttk.Button(app, text="OK", command= lambda: self.export())
		self.error_lbl = ttk.Label(app, text="")

	def show(self):
		self.key_entry.delete(0, tk.END)
		self.error_lbl.config(text="")
		self.return_btn.pack()
		self.title_lbl.pack()
		self.please_lbl.pack()
		self.key_entry.pack()
		self.btn.pack()
		self.error_lbl.pack()

	def hide(self):
		self.return_btn.pack_forget()
		self.title_lbl.pack_forget()
		self.please_lbl.pack_forget()
		self.key_entry.pack_forget()
		self.btn.pack_forget()
		self.error_lbl.pack_forget()

	def reload(self):
		self.hide()
		self.show()

	def cancel(self, loopback):
		self.hide()
		loopback()

	def export(self):
		self.error_lbl.config(text="")
		mkey = self.key_entry.get()
		self.key_entry.delete(0, tk.END)
		if master_key.check(mkey):
			key_path = Path.home() / 'cool_password_save.cpsave'
			save_path = Path.home() / 'cool_password_key.cpkey'
			save.save(key_path, save_path)
			self.error_lbl.config(text=f"Your saves has been saved in '{save_path}', Your key has been saved in '{key_path}'")
		else:
			self.error_lbl.config(text="Master key incorrect")

import tkinter as tk
import tkinter.ttk as ttk
from .model import master_key
from .home import HomeScene

class LoginScene:

	def __init__(self, app):
		self.app = app
		self.lbl_title = ttk.Label(app, text='Please enter your master key')
		self.lbl_error = ttk.Label(app, text="")
		self.entry = ttk.Entry(app, show='*')
		self.entry.bind('<Return>', self.login)
		self.btn_log = ttk.Button(app, text='▶', command = lambda : self.login())

	def show(self):
		self.lbl_title.grid()
		self.entry.grid(row=1)
		self.btn_log.grid(row=1, column=1)
		self.lbl_error.grid(row=2)

	def hide(self):
		self.lbl_title.destroy()
		self.entry.destroy()
		self.btn_log.destroy()
		self.lbl_error.destroy()
	
	def login(self, event=None):
		if master_key.check(self.entry.get()):
			self.hide()
			HomeScene(self.app).show()
		else:
			self.lbl_error.config(text="Master key incorrect")
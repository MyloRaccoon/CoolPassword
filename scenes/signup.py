import tkinter.ttk as ttk
import tkinter as tk

from scenes.login import LoginScene
from scenes.model import loger
from .model import master_key
from .home import HomeScene

class SignupScene:

	def __init__(self, app):
		self.app = app
		self.label = ttk.Label(app, text='Please enter a master key')
		self.entry = ttk.Entry(app, show='*')
		self.entry.bind('<Return>', self.signup)
		self.btn_signup = ttk.Button(app, text='▶', command = lambda : self.signup())

	def show(self):
		self.label.grid()
		self.entry.grid(row=1)
		self.btn_signup.grid(row=1, column=1)

	def hide(self):
		self.label.grid_forget()
		self.entry.grid_forget()
		self.btn_signup.grid_forget()

	def signup(self, event=None):
		new_key = self.entry.get()
		self.entry.delete(0, tk.END)

		if len(new_key) > 0:
			loger.login()
			master_key.save(new_key)
			self.hide()
			HomeScene(self.app, LoginScene(self.app).show).show()


import tkinter as tk
from .model import master_key
from .home import HomeScene

class SignupScene:

	def __init__(self, app):
		self.app = app
		self.label = tk.Label(app, text='Please enter a master key')
		self.entry_master_key = tk.Entry(app)
		self.btn_signup = tk.Button(app, text='sign up', command = lambda : self.signup())

	def show(self):
		self.label.grid()
		self.entry_master_key.grid()
		self.btn_signup.grid()

	def hide(self):
		self.label.destroy()
		self.entry_master_key.destroy()
		self.btn_signup.destroy()

	def signup(self):
		new_key = self.entry_master_key.get()

		if len(new_key) > 0:
			master_key.save(new_key)
			self.hide()
			HomeScene(self.app).show()


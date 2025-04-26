import tkinter.ttk as ttk
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
		self.label.destroy()
		self.entry.destroy()
		self.btn_signup.destroy()

	def signup(self, event=None):
		new_key = self.entry.get()

		if len(new_key) > 0:
			master_key.save(new_key)
			self.hide()
			HomeScene(self.app).show()


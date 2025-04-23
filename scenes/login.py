import tkinter as tk
from .model import master_key
from .home import HomeScene

class LoginScene:

	def __init__(self, app):
		self.app = app
		self.lbl_title = tk.Label(app, text='please enter your master key')
		self.btn_log = tk.Button(app, text='login', command = lambda : self.log())
		self.entry = tk.Entry(app)

	def log(self):
		if master_key.check(self.entry.get()):
			self.hide()
			HomeScene(self.app).show()

	def show(self):
		self.lbl_title.grid()
		self.entry.grid()
		self.btn_log.grid()

	def hide(self):
		self.lbl_title.destroy()
		self.entry.destroy()
		self.btn_log.destroy()
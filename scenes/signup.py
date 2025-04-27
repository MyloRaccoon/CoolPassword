import tkinter.ttk as ttk
import tkinter as tk

from scenes.load_scene import LoadScene
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

		self.load_lbl = ttk.Label(app, text="load a save file")
		login_scene = LoginScene(app)
		home_scene = HomeScene(app, login_scene.show)
		load_scene = LoadScene(app, self.show, home_scene.show)
		self.load_btn = ttk.Button(app, text="🗎", command= lambda: [self.hide(), load_scene.show()])

	def show(self):
		self.label.grid()
		self.entry.grid(row=1)
		self.btn_signup.grid(row=1, column=1)
		self.load_lbl.grid(row=2)
		self.load_btn.grid(row=2, column=1)

	def hide(self):
		self.label.grid_forget()
		self.entry.grid_forget()
		self.btn_signup.grid_forget()
		self.load_lbl.grid_forget()
		self.load_btn.grid_forget()

	def signup(self, event=None):
		new_key = self.entry.get()
		self.entry.delete(0, tk.END)

		if len(new_key) > 0:
			loger.login()
			master_key.save(new_key)
			self.hide()
			HomeScene(self.app, LoginScene(self.app).show).show()


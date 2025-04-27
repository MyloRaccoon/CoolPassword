import tkinter.ttk as ttk
import tkinter as tk

from scenes.load_save import LoadScene
from scenes.login import LoginScene
from scenes.model import loger
from .model import master_key
from .home import HomeScene

class SignupScene:

	def __init__(self, app):
		self.app = app

		self.lbl_welcome = ttk.Label(app, text="Welcome to Cool Password !")

		self.label = ttk.Label(app, text='Please enter a master key')
		self.entry = ttk.Entry(app, show='*')
		self.entry.bind('<Return>', self.signup)
		self.btn_signup = ttk.Button(app, text='▶', command = lambda : self.signup(), style="Main.TButton")

		self.lbl_or = ttk.Label(app, text="or")

		self.load_lbl = ttk.Label(app, text="load a save")
		login_scene = LoginScene(app)
		home_scene = HomeScene(app, login_scene.show)
		load_scene = LoadScene(app, self.show, home_scene.show)
		self.load_btn = ttk.Button(app, text="🗎", command= lambda: [self.hide(), load_scene.show()], style="Main.TButton")

	def show(self):
		self.lbl_welcome.grid(pady=20)
		self.label.grid(row=1)
		self.entry.grid(row=2)
		self.btn_signup.grid(row=2, column=1)
		self.lbl_or.grid(row=3)
		self.load_lbl.grid(row=4)
		self.load_btn.grid(row=4, column=1)

	def hide(self):
		self.lbl_welcome.grid_forget()
		self.label.grid_forget()
		self.entry.grid_forget()
		self.btn_signup.grid_forget()
		self.lbl_or.grid_forget()
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


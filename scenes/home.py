import tkinter as tk

class HomeScene:

	def __init__(self, app):
		self.lbl_title = tk.Label(app, text='Welcome')

	def show(self):
		self.lbl_title.grid()

	def hide(self):
		self.lbl_title.destroy()
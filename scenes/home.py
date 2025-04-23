import tkinter as tk
from .model import passwords

class HomeScene:

	def __init__(self, app):
		self.app = app
		self.lbl_title = tk.Label(app, text='Welcome')
		self.sites_lbl = []
		self.entry_site = tk.Entry(app)
		self.btn_add_site = tk.Button(app, text='Add site', command = lambda: self.add_site())

	def add_site(self):
		new_site = self.entry_site.get()
		if len(new_site) > 0:
			passwords.new(new_site)
			self.entry_site.delete(0,tk.END)
			self.reload()

	def show(self):
		self.lbl_title.grid()
		passwords.load()
		for site in passwords.get_sites():
			lbl = tk.Label(self.app, text=site)
			self.sites_lbl.append(lbl)
			lbl.grid()
		self.entry_site.grid()
		self.btn_add_site.grid()

	def hide(self):
		self.lbl_title.grid_forget()
		while len(self.sites_lbl) != 0:
			self.sites_lbl.pop().grid_forget()
		self.entry_site.grid_forget()
		self.btn_add_site.grid_forget()

	def reload(self):
		self.hide()
		self.show()
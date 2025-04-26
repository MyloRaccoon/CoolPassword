from hashlib import new
import tkinter as tk
import tkinter.ttk as ttk

from scenes import style
from scenes.site_list import SiteList
from .model import passwords

class HomeScene:

	def __init__(self, app):
		passwords.load()

		self.search_canvas = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)
		
		self.search_lbl = ttk.Label(self.search_canvas, text="Search a site")
		self.search_entry = ttk.Entry(self.search_canvas)
		self.search_entry.bind("<Key>", self.on_filter)

		self.search_lbl.grid(padx=10)
		self.search_entry.grid(row=0, column=1)



		self.sites_canvas = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)
		self.site_list = SiteList(self.sites_canvas)


		self.site_max_lenght = 20
		self.add_canvas = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)
		
		self.add_lbl = ttk.Label(self.add_canvas, text='Add a new site')
		self.add_entry = ttk.Entry(self.add_canvas)
		self.add_entry.bind("<Return>", self.add_site)
		self.add_btn = ttk.Button(self.add_canvas, text='✚', command = lambda: self.add_site())
		self.add_error = ttk.Label(self.add_canvas, text="")
		
		self.add_lbl.grid(padx=5)
		self.add_entry.grid(row=0, column=1, padx=5)
		self.add_btn.grid(row=0, column=2)
		self.add_error.grid(row=1, pady=5)

	def on_filter(self, event=None):
		self.site_list.reload(self.search_entry.get())

	def add_site(self, event=None):
		self.add_error.config(text="")
		new_site = self.add_entry.get()
		if len(new_site) > 0 and len(new_site) < self.site_max_lenght:
			passwords.new(new_site)
			self.reload()
		elif len(new_site) >= self.site_max_lenght:
			self.add_error.config(text='Site name too long, sorry')
		self.add_entry.delete(0,tk.END)

	def show(self):

		self.search_canvas.pack(pady=10)

		self.site_list.show()
		self.sites_canvas.pack()

		self.add_canvas.pack(pady=10)

	def hide(self):
		self.search_canvas.pack_forget()

		self.site_list.hide()
		self.sites_canvas.pack_forget()

		self.add_canvas.pack_forget()


	def reload(self):
		self.hide()
		self.show()
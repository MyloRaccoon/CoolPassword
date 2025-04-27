from hashlib import new
import tkinter as tk
import tkinter.ttk as ttk
from typing import Callable

from scenes import style
from scenes.ask_key import AskKeyScene
from scenes.load_scene import LoadScene
from scenes.model import loger
from scenes.save_scene import SaveScene
from scenes.site_list import SiteList
from .model import passwords

class HomeScene:

	def __init__(self, app, loopback):
		passwords.load()

		self.btn_logout = ttk.Button(app, text="⇱", command= lambda: self.logout(loopback))

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


		self.save_canvas = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)

		self.export_btn = ttk.Button(self.save_canvas, text='🖫', command=lambda: self.go_to_export(app))
		self.import_btn = ttk.Button(self.save_canvas, text='🗎', command=lambda: self.go_to_import(app))

		self.export_btn.grid()
		self.import_btn.grid(row=0, column=1, padx=3)


	def show(self):
		self.save_canvas.pack(side=tk.LEFT, anchor='nw')

		self.btn_logout.pack(side=tk.RIGHT, anchor='ne')

		self.search_canvas.pack(pady=10)

		self.site_list.show()
		self.sites_canvas.pack()

		self.add_canvas.pack(pady=10)

	def hide(self):
		self.btn_logout.pack_forget()

		self.search_canvas.pack_forget()

		self.site_list.hide()
		self.sites_canvas.pack_forget()

		self.add_canvas.pack_forget()

		self.save_canvas.pack_forget()


	def reload(self):
		self.hide()
		self.show()

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
 
	def logout(self, loopback: Callable):
		loger.logout()
		self.hide()
		loopback()

	def go_to_export(self, app):
		self.hide()
		SaveScene(app, self.show).show()

	def go_to_import(self, app):
		self.hide()
		on_ok = LoadScene(app, self.show, self.show).show
		on_cancel = self.show
		AskKeyScene(app, on_cancel, on_ok).show()

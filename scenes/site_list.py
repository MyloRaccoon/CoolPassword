import tkinter as tk
import tkinter.ttk as ttk

from scenes.style import Color
from .model import passwords

class SiteList:

	def __init__(self, parent):
		self.parent = parent
		self.canvas = tk.Canvas(parent, bg=Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0, height=685)
		self.scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.canvas.yview)
		self.canvas.config(yscrollcommand=self.scrollbar.set)
		self.canvas_children = []
		self.frame = ttk.Frame(self.canvas)
		self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
		self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

		self.canvas.bind_all("<MouseWheel>", self.on_mousewheel) # Windows / Mac
		self.canvas.bind_all("<Button-4>", self.on_mousewheel) # Linux up
		self.canvas.bind_all("<Button-5>", self.on_mousewheel) # Linux down

		self.n_sites_limit = 18

	def on_mousewheel(self, event):
		if len(passwords.get_sites()) > self.n_sites_limit:
			if event.num == 4:  # Linux scroll up
				self.canvas.yview_scroll(-1, "units")
			elif event.num == 5:  # Linux scroll down
				self.canvas.yview_scroll(1, "units")
			else:  # Windows/Mac
				self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")


	def show(self, filter: str = ""):
		row = 0
		for site in passwords.get_sites():

			if (not filter in site) and filter != "":
				continue

			ttk.Label(self.frame, text=site).grid(row=row, column=0, padx=10, pady=5)

			ttk.Button(
				self.frame, 
				text='⎙', 
				command = lambda site=site: passwords.copy(site)
			).grid(row=row, column=1, padx=10, pady=5)

			ttk.Button(
				self.frame, 
				text='⌫', 
				command = lambda site=site: [passwords.remove(site), self.reload()]
			).grid(row=row, column=2, padx=10, pady=5)

			row += 1

		self.canvas.pack(side=tk.LEFT, fill=tk.BOTH)

		if len(passwords.get_sites()) > self.n_sites_limit:
			self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

	def hide(self):
		for widget in self.frame.winfo_children():
			widget.destroy()
		self.canvas.pack_forget()
		self.scrollbar.pack_forget()

	def reload(self, filter: str = ""):
		self.hide()
		self.show(filter)
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from scenes import style
from scenes.model import loger
from scenes.model.save import load

class LoadScene:

	def __init__(self, app, loopback, on_ok):
		self.app = app

		self.return_btn = ttk.Button(app, text="⤶", command= lambda: [self.hide(), loopback()])


		self.save_file_canvas = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)

		self.save_file_lbl = ttk.Label(self.save_file_canvas, text='import a cool_password_save.cpsave file')
		self.save_file_btn = ttk.Button(self.save_file_canvas, text="🗁", command= lambda: self.import_save_file())
		self.save_file_path = ttk.Label(self.save_file_canvas)

		self.save_file_lbl.grid()
		self.save_file_btn.grid(row=0, column=1)
		self.save_file_path.grid(row=0, column=2)


		self.key_file_canvas = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)

		self.key_file_lbl = ttk.Label(self.key_file_canvas, text='import a cool_password_key.cpkey file')
		self.key_file_btn = ttk.Button(self.key_file_canvas, text="🗁", command= lambda: self.import_key_file())
		self.key_file_path = ttk.Label(self.key_file_canvas)

		self.key_file_lbl.grid()
		self.key_file_btn.grid(row=0, column=1)
		self.key_file_path.grid(row=0, column=2)


		self.master_key_canvas = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)

		self.master_key_lbl = ttk.Label(self.master_key_canvas, text='enter your master key')
		self.master_key_entry = ttk.Entry(self.master_key_canvas, show='*')

		self.master_key_lbl.grid()
		self.master_key_entry.grid(row=0, column=1)


		self.error_lbl = ttk.Label(app)

		self.load_btn = ttk.Button(app, text="OK", command= lambda: self.load(app, on_ok))


	def show(self):
		self.save_file_path.config(text='')
		self.key_file_path.config(text='')
		self.master_key_entry.delete(0,tk.END)

		self.return_btn.pack()
		self.save_file_canvas.pack()
		self.key_file_canvas.pack()
		self.master_key_canvas.pack()
		self.error_lbl.pack()
		self.load_btn.pack()

	def hide(self):
		self.return_btn.pack_forget()
		self.save_file_canvas.pack_forget()
		self.key_file_canvas.pack_forget()
		self.master_key_canvas.pack_forget()
		self.error_lbl.pack_forget()
		self.load_btn.pack_forget()

	def reload(self):
		self.hide()
		self.show()

	def import_save_file(self):
		filetypes = {
			('All files', '*.*'),
			('Cool Password Save files', '.cpsave')
		}

		file = fd.askopenfile(filetypes = filetypes)

		if file != None:
			self.save_file_path.config(text=file.name)

	def import_key_file(self):
		filetypes = {
			('All files', '*.*'),
			('Cool Password Key files', '.cpkey')
		}

		file = fd.askopenfile(filetypes = filetypes)

		if file != None:
			self.key_file_path.config(text=file.name)

	def load(self, app, on_ok, event=None):
		self.error_lbl.config(text="")

		save_path = self.save_file_path.cget("text")
		key_path = self.key_file_path.cget("text")
		mkey = self.master_key_entry.get()

		self.master_key_entry.delete(0,tk.END)

		if not load(mkey, save_path, key_path):
			self.error_lbl.config(text="Master key incorrect")
		else:
			loger.login()
			self.hide()
			on_ok()
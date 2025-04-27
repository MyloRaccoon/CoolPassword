import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from scenes import style
from scenes.model import loger
from scenes.model.save import load

class LoadScene:

	def __init__(self, app, loopback, on_ok):
		self.app = app
		self.on_ok = on_ok

		self.title_lbl = ttk.Label(app, text="Load a save")

		self.info_lbl = ttk.Label(app, text="""To load a save you need: 
	- a Cool Password Save file (.cpsave)
	- the key file to read it, a Cool Password Key file (.cpkey)
	- the master key from this save
Both files are created when hitting the save "🖫" button in the home page
⚠ it's recommended to delete those save file when you imported them
		""")

		self.save_file_canvas = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)

		self.save_file_lbl = ttk.Label(self.save_file_canvas, text='import a .cpsave file')
		self.save_file_btn = ttk.Button(self.save_file_canvas, text="🗁", command= lambda: self.import_save_file(), style="Main.TButton")
		self.save_file_path = ttk.Label(self.save_file_canvas)

		self.save_file_lbl.grid()
		self.save_file_btn.grid(row=0, column=1, padx=10)
		self.save_file_path.grid(row=0, column=2)


		self.key_file_canvas = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)

		self.key_file_lbl = ttk.Label(self.key_file_canvas, text='import a .cpkey file')
		self.key_file_btn = ttk.Button(self.key_file_canvas, text="🗁", command= lambda: self.import_key_file(), style="Main.TButton")
		self.key_file_path = ttk.Label(self.key_file_canvas)

		self.key_file_lbl.grid()
		self.key_file_btn.grid(row=0, column=1, padx=10)
		self.key_file_path.grid(row=0, column=2)


		self.master_key_canvas = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)

		self.master_key_lbl = ttk.Label(self.master_key_canvas, text='master key')
		self.master_key_entry = ttk.Entry(self.master_key_canvas, show='*')
		self.master_key_entry.bind("<Return>", self.load)

		self.master_key_lbl.grid()
		self.master_key_entry.grid(row=0, column=1, padx=10)


		self.error_lbl = ttk.Label(app)


		self.nav_btns = tk.Canvas(app, bg=style.Color.DARKEST, borderwidth=0, relief='flat', highlightthickness=0)

		self.load_btn = ttk.Button(self.nav_btns, text="OK", command= lambda: self.load(), style="Main.TButton")
		self.return_btn = ttk.Button(self.nav_btns, text="⤶", command= lambda: [self.hide(), loopback()], style="Main.TButton")

		self.load_btn.grid()
		self.return_btn.grid(row=0, column=1, padx=10)


	def show(self):
		self.save_file_path.config(text='')
		self.key_file_path.config(text='')
		self.master_key_entry.delete(0,tk.END)

		self.title_lbl.pack(pady=20)

		self.info_lbl.pack()

		self.save_file_canvas.pack(pady=13)
		self.key_file_canvas.pack(pady=13)
		self.master_key_canvas.pack(pady=13)
		self.error_lbl.pack()
		
		self.nav_btns.pack()

	def hide(self):
		self.title_lbl.pack_forget()

		self.info_lbl.pack_forget()

		self.save_file_canvas.pack_forget()
		self.key_file_canvas.pack_forget()
		self.master_key_canvas.pack_forget()
		self.error_lbl.pack_forget()

		self.nav_btns.pack_forget()

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

	def load(self, event=None):
		self.error_lbl.config(text="")

		save_path = self.save_file_path.cget("text")
		key_path = self.key_file_path.cget("text")
		mkey = self.master_key_entry.get()

		self.master_key_entry.delete(0,tk.END)

		if save_path == "":
			self.error_lbl.config(text="please import a .cpsave file")

		elif key_path == "":
			self.error_lbl.config(text="please import a .cpkey file")

		elif mkey == "":
			self.error_lbl.config(text="please enter the master key")

		elif not load(mkey, save_path, key_path):
			self.error_lbl.config(text="Master key incorrect")

		else:
			loger.login()
			self.hide()
			self.on_ok()
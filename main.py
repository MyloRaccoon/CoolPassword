import os
import tkinter as tk
from scenes.home import HomeScene
from scenes.model.files import init_dir
import scenes.style
from scenes.signup import SignupScene
from scenes.login import LoginScene
from scenes.model import master_key
from scenes.model import loger
from scenes.style import Color

if __name__ == '__main__':
	print("hello world")

	init_dir()

	root = tk.Tk()
	root.title('Cool Password')
	root.configure(bg=Color.DARKEST)
	root.grid_anchor("center")
	root.geometry('500x800')
	root.resizable(False, False)

	app = tk.Frame(root)
	app.configure(bg=Color.DARKEST)
	app.grid()

	scenes.style.init()

	if master_key.is_init():
		if loger.is_logged():
			HomeScene(app, LoginScene(app).show).show()
		else:
			LoginScene(app).show()
	else:
		SignupScene(app).show()

	root.mainloop()
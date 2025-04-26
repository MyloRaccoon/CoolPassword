import tkinter as tk
import tkinter.ttk as ttk
import scenes.style
from scenes.signup import SignupScene
from scenes.login import LoginScene
from scenes.model import master_key
from scenes.style import Color

if __name__ == '__main__':
	root = tk.Tk()
	root.title('Cool Password')
	root.configure(bg=Color.DARKEST)
	root.grid_anchor("n")
	root.geometry('500x800')
	root.resizable(False, False)

	app = tk.Frame(root)
	app.configure(bg=Color.DARKEST)
	app.grid()

	scenes.style.init()

	if master_key.is_init():
		LoginScene(app).show()
	else:
		SignupScene(app).show()

	root.mainloop()
import tkinter as tk
from scenes.signup import SignupScene
from scenes.login import LoginScene
from scenes.model import master_key

if __name__ == '__main__':
	root = tk.Tk()
	root.title('Cool Password')
	root.geometry('500x800')
	root.resizable(False, False)

	app = tk.Frame(root)
	app.grid()

	if master_key.is_init():
		LoginScene(app).show()
	else:
		SignupScene(app).show()

	root.mainloop()
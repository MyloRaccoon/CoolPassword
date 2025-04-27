from enum import Enum
import tkinter.ttk as ttk

class Color:
	DARKEST: str = '#28272D'
	DARKER: str = '#585562'
	DARK: str = '#3E3D41'
	BTN_PRESSED: str = '#2D2C30'
	LIGHT: str = 'white'

def init():

	style = ttk.Style()


	style.configure("TButton",
		background = Color.DARKER,
		foreground = Color.LIGHT,
		borderwidth = 0
	)

	style.map("TButton",
		background = [
			('active', Color.DARK), 
			('pressed', Color.BTN_PRESSED)
		],
		relief=[
			('pressed', 'sunken'), 
			('!pressed', 'raised')
		]
	)

	style.configure("Main.TButton",
		width=3
	)

	style.configure("TLabel",
		background = Color.DARKEST,
		foreground = Color.LIGHT
	)

	style.configure("TEntry",
		background = Color.DARKEST,
		foreground = Color.LIGHT,
		fieldbackground = Color.DARK,
		borderwidth = 0,
		highlightthickness=0
	)

	style.configure("TFrame",
		background = Color.DARKEST,
		borderwidth = 0
	)

	style.configure("TScrollbar",
		background=Color.DARKER,
		troughcolor=Color.DARKEST,
		arrowcolor=Color.DARK,
		borderwidth=0,
		relief="flat",
		gripcount=0
	)

	style.map("TScrollbar",
	    background=[
	        ("active", Color.DARK),
	        ("!active", Color.DARKER)
	    ]
	)

	# this apparently is for the combobox in the filedialog
	# am not sure and, because i use gtk apparently, i can't test this lol
	# so mine is ugly sadly :,(
	style.configure("TCombobox",
	    fieldbackground=Color.DARK,
	    background=Color.DARKEST,
	    foreground=Color.LIGHT,
	    arrowcolor=Color.LIGHT,
	    borderwidth=0,
	    relief="flat"
	)
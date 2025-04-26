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
		borderwidth = 0,
		width=3
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
		troughcolor=Color.DARK,
		arrowcolor=Color.DARK,
		borderwidth=0,
		relief="flat",
		gripcount=0
	)
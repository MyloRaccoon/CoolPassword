from pathlib import Path

def login():
	with open('.logged', 'w') as f:
		f.write("true")
		LOGGED = True

def logout():
	with open('.logged', 'w') as f:
		f.write("false")
		LOGGED = False

def is_logged():
	with open('.logged', 'r') as f:
		match f.read():
			case "true":
				return True
			case _: 
				return False
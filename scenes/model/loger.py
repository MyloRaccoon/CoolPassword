from scenes.model.files import LOGER_FILE

def login():
	with open(LOGER_FILE, 'w') as f:
		f.write("true")

def logout():
	with open(LOGER_FILE, 'w') as f:
		f.write("false")

def is_logged():
	if not LOGER_FILE.exists():
		return False
	with open(LOGER_FILE, 'r') as f:
		match f.read():
			case "true":
				return True
			case _: 
				return False
from random import randint
from pathlib import Path

def generate():
	with open('.seed', 'w') as f:
		f.write(str(randint(0, 1000000000)))

def get():
	if not Path('.seed').exists():
		generate()
	with open('.seed', 'r') as f:
		seed = f.read()
	return seed
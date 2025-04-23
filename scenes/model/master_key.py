from cryptography.fernet import Fernet
from pathlib import Path

KEY_FILE = '.master_key'

def is_init():
	return Path(KEY_FILE).exists()

def save(master_key):
	with open(KEY_FILE, "w") as f:
		f.write(master_key)

def get():
	with open(KEY_FILE, "r") as f:
		return f.read()

def check(password):
	return get() == password
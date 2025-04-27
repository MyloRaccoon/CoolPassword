from cryptography.fernet import Fernet
from pathlib import Path
import os

from scenes.model.files import MASTER_KEY_FILE

def is_init():
	return MASTER_KEY_FILE.exists()

def save(master_key):
	with open(MASTER_KEY_FILE, "w") as f:
		f.write(master_key)

def get():
	with open(MASTER_KEY_FILE, "r") as f:
		return f.read()

def check(password):
	return get() == password

def clear():
	if MASTER_KEY_FILE.exists():
		os.remove(MASTER_KEY_FILE)
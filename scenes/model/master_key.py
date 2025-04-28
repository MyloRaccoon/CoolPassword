from cryptography.fernet import Fernet
from pathlib import Path
import os

from scenes.model.files import MASTER_KEY_FILE
from scenes.model.secret import hash_password

MASTER_KEY = ""

def is_init():
	return MASTER_KEY_FILE.exists()

def save(master_key: str):
	MASTER_KEY = master_key
	with open(MASTER_KEY_FILE, "w") as f:
		f.write(hash_password(master_key))

def get_hash():
	with open(MASTER_KEY_FILE, "r") as f:
		return f.read()

def check(password):
	return get_hash() == hash_password(password)

def clear():
	if MASTER_KEY_FILE.exists():
		os.remove(MASTER_KEY_FILE)
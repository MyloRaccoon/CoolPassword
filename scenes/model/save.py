import json
import os
from pathlib import Path

from scenes.model.files import KEY_FILE, SAVE_FILE
from scenes.model.loger import logout
import scenes.model.master_key as master_key_controller
import scenes.model.seed as seed_controller
import scenes.model.passwords as passwords
from scenes.model.secret import decrypt, encrypt, hash_password

def save():
	master_key = master_key_controller.get_hash()
	seed = seed_controller.get()
	sites = passwords.get_sites()

	data = {
		'master_key': master_key,
		'seed': seed,
		'sites': sites
	}
	json_data = json.dumps(data)

	encrypted, key = encrypt(json_data)



	with open(SAVE_FILE, 'wb') as f:
		f.write(encrypted)

	with open(KEY_FILE, 'wb') as f:
		f.write(key)


def load(master_key: str, save_path: str, key_path: str) -> bool:
	with open(key_path, 'rb') as f:
		key = f.read()

	with open(save_path, 'rb') as f:
		crypted = f.read()

	json_data = decrypt(key, crypted)
	data = json.loads(json_data)

	if hash_password(master_key) != data['master_key']:
		return False

	master_key_controller.save(master_key)
	seed_controller.set(data['seed'])
	passwords.set(data['sites'])

	return True


def nuke():
	passwords.clear()
	master_key_controller.clear()
	seed_controller.clear()
	logout()
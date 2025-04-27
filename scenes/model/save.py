import json
from cryptography.fernet import Fernet

import scenes.model.master_key as master_key_controller
import scenes.model.seed as seed_controller
import scenes.model.passwords as passwords
from scenes.model.secret import decrypt, encrypt

def save(save_path, key_path):
	master_key = master_key_controller.get()
	seed = seed_controller.get()
	sites = passwords.get_sites()

	data = {
		'master_key': master_key,
		'seed': seed,
		'sites': sites
	}
	json_data = json.dumps(data)

	encrypted, key = encrypt(json_data)



	with open(save_path, 'wb') as f:
		f.write(encrypted)

	with open(key_path, 'wb') as f:
		f.write(key)


def load(master_key: str, save_path: str, key_path: str) -> bool:
	with open(key_path, 'rb') as f:
		key = f.read()

	with open(save_path, 'rb') as f:
		crypted = f.read()

	json_data = decrypt(key, crypted)
	data = json.loads(json_data)

	if master_key != data['master_key']:
		return False

	master_key_controller.save(data['master_key'])
	seed_controller.set(data['seed'])
	passwords.set(data['sites'])

	return True
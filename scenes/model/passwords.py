import hashlib
from .master_key import get as master_key_get
from pathlib import Path

SEPARATOR = '|'
SITES_FILE = '.sites'
PASSWORDS = {}

def generate(master_key: str, site: str) -> str:
	new_key = master_key + site
	hash_object = hashlib.sha256(new_key.encode())
	return hash_object.hexdigest()

def get_sites():
	if not Path(SITES_FILE).exists():
		return []

	with open(SITES_FILE, 'r') as f:
		content = f.read()

	return content.split(SEPARATOR)

def load():
	for site in get_sites():
		PASSWORDS[site] = generate(master_key_get(), site)

def save():
	content = ''
	for site in PASSWORDS.keys():
		content += site + SEPARATOR
	content = content[:-1]
	with open(SITES_FILE, 'w') as f:
		f.write(content)

def get(site):
	return PASSWORDS[site]

def new(site):
	PASSWORDS[site] = generate(master_key_get(), site)
	save()
import pyperclip

from scenes.model import secret
from .master_key import get as get_master_key
from .seed import get as get_seed
from pathlib import Path

SEPARATOR = '|'
SITES_FILE = '.sites'
PASSWORDS = {}

def generate(master_key: str, site: str, seed: str) -> str:

	return secret.generate(master_key, site, seed)

def get_sites():
	if not Path(SITES_FILE).exists():
		return []

	with open(SITES_FILE, 'r') as f:
		content = f.read()

	if content == '':
		return []

	return content.split(SEPARATOR)

def load():
	for site in get_sites():
		PASSWORDS[site] = generate(get_master_key(), site, get_seed())

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
	PASSWORDS[site] = generate(get_master_key(), site, get_seed())
	save()

def copy(site):
	pyperclip.copy(get(site))

def remove(site):
	PASSWORDS.pop(site)
	save()

def set(sites: list[str]):
	PASSWORDS.clear()
	for site in sites:
		PASSWORDS[site] = generate(get_master_key(), site, get_seed())
	save()
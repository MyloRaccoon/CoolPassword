import os
import pyperclip

from scenes.model import secret
from scenes.model.files import SITES_FILE
from .master_key import MASTER_KEY
from .seed import get as get_seed

SEPARATOR = "|"
PASSWORDS = {}


def generate(master_key: str, site: str, seed: str) -> str:

    return secret.generate(master_key, site, seed)


def get_sites():
    if not SITES_FILE.exists():
        return []

    with open(SITES_FILE, "r") as f:
        content = f.read()

    if content == "":
        return []

    return content.split(SEPARATOR)


def load():
    # TODO load master key in memory to use it and not the h
    for site in get_sites():
        PASSWORDS[site] = generate(MASTER_KEY, site, get_seed())


def save():
    content = ""
    for site in PASSWORDS.keys():
        content += site + SEPARATOR
    content = content[:-1]
    with open(SITES_FILE, "w") as f:
        f.write(content)


def get(site):
    return PASSWORDS[site]


def new(site):
    PASSWORDS[site] = generate(MASTER_KEY, site, get_seed())
    save()


def copy(site):
    pyperclip.copy(get(site))


def remove(site):
    PASSWORDS.pop(site)
    save()


def set(sites: list[str]):
    PASSWORDS.clear()
    for site in sites:
        PASSWORDS[site] = generate(MASTER_KEY, site, get_seed())
    save()


def clear():
    if SITES_FILE.exists():
        os.remove(SITES_FILE)
    load()

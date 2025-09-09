import os
from random import randint

from scenes.model.files import SEED_FILE


def generate():
    with open(SEED_FILE, "w") as f:
        f.write(str(randint(0, 1000000000)))


def get():
    if not SEED_FILE.exists():
        generate()
    with open(SEED_FILE, "r") as f:
        seed = f.read()
    return seed


def set(seed: str):
    with open(SEED_FILE, "w") as f:
        f.write(seed)


def clear():
    if SEED_FILE.exists():
        os.remove(SEED_FILE)

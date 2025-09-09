import hashlib
from cryptography.fernet import Fernet

def generate(master_key: str, site: str, seed: str) -> str:
    new_key = master_key + site + seed

    h = hashlib.sha256(new_key.encode()).hexdigest()

    special_chars = "!@#$%^&*()-_=+[]{}<>?/|"
    majs = "AZERTYUIOPQSDFGHJKLMWXCVBN"

    cool_number = (int(seed) + 1) * 999

    special_part = ''
    for i in range((cool_number % 5) + 1):
        index = ((i+1)*cool_number) % len(special_chars)
        special_part += special_chars[index]

    maj_part = ''
    for i in range((cool_number % 5) + 1):
        index = ((i+1)*cool_number) % len(majs)
        maj_part += majs[index]

    password = h + special_part + maj_part


    password_list = list(password)
    for i in range(len(password_list)):
        j = (i * cool_number + ord(h[i*cool_number % len(h)])) % len(password_list)
        password_list[i], password_list[j] = password_list[j], password_list[i]

    return "".join(password_list)

def encrypt(msg):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return (fernet.encrypt(msg.encode()), key)

def decrypt(key, msg):
    fernet = Fernet(key)
    return fernet.decrypt(msg).decode()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
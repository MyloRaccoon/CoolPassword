import hashlib

def generate(master_key: str, public_key: str) -> str:
	new_key = master_key + public_key
	hash_object = hashlib.sha256(new_key.encode())
	return hash_object.hexdigest()
from model.secret import generate, encrypt, decrypt, hash_password
from cryptography.fernet import Fernet


def test_generate_deterministic():
    """Le mot de passe généré doit toujours être identique avec les mêmes paramètres."""
    pw1 = generate("masterkey", "example.com", "42")
    pw2 = generate("masterkey", "example.com", "42")
    assert pw1 == pw2


def test_generate_different_inputs():
    """Des paramètres différents doivent donner des résultats différents."""
    pw1 = generate("masterkey", "example.com", "42")
    pw2 = generate("masterkey", "example.org", "42")
    pw3 = generate("masterkey2", "example.com", "42")
    pw4 = generate("masterkey", "example.com", "43")

    assert len({pw1, pw2, pw3, pw4}) == 4


def test_encrypt_decrypt_roundtrip():
    """Un message encrypté puis décrypté doit retrouver sa valeur initiale."""
    msg = "super_secret"
    enc, key = encrypt(msg)
    dec = decrypt(key, enc)
    assert dec == msg


def test_encrypt_returns_bytes_and_key():
    """Vérifie que encrypt retourne bien un tuple (bytes, key)."""
    msg = "hello"
    enc, key = encrypt(msg)
    assert isinstance(enc, bytes)
    assert isinstance(key, bytes)
    # la clé doit pouvoir créer un Fernet valide
    Fernet(key)


def test_hash_password_consistency():
    """Le hash doit être déterministe et identique pour la même entrée."""
    h1 = hash_password("password123")
    h2 = hash_password("password123")
    assert h1 == h2


def test_hash_password_uniqueness():
    """Deux mots de passe différents doivent avoir des hash différents."""
    h1 = hash_password("password123")
    h2 = hash_password("differentPassword")
    assert h1 != h2

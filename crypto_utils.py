import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def load_key():
    key_b64 = os.getenv("AES_SECRET_KEY")

    if not key_b64:
        raise Exception("AES_SECRET_KEY not found in .env")

    return base64.b64decode(key_b64)

def encrypt_data(plain_text: str) -> str:
    key = load_key()
    aesgcm = AESGCM(key)

    nonce = os.urandom(12)
    encrypted = aesgcm.encrypt(nonce, plain_text.encode("utf-8"), None)

    return base64.b64encode(nonce + encrypted).decode("utf-8")

def decrypt_data(encrypted_text: str) -> str:
    key = load_key()
    aesgcm = AESGCM(key)

    encrypted_blob = base64.b64decode(encrypted_text)
    nonce = encrypted_blob[:12]
    ciphertext = encrypted_blob[12:]

    decrypted = aesgcm.decrypt(nonce, ciphertext, None)

    return decrypted.decode("utf-8")
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64

key = AESGCM.generate_key(bit_length=256)

with open("secret.key", "wb") as f:
    f.write(base64.b64encode(key))

print(" AES-256 key generated and saved.")
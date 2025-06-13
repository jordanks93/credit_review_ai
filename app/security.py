# security.py
from cryptography.fernet import Fernet
import os

KEY_PATH = "secret.key"
if not os.path.exists(KEY_PATH):
    with open(KEY_PATH, "wb") as f:
        f.write(Fernet.generate_key())

with open(KEY_PATH, "rb") as f:
    key = f.read()
fernet = Fernet(key)

def save_encrypted_file(filepath, data):
    encrypted_data = fernet.encrypt(data)
    enc_path = filepath + ".enc"
    with open(enc_path, "wb") as f:
        f.write(encrypted_data)
    return enc_path

def decrypt_file(enc_path):
    with open(enc_path, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    temp_path = enc_path.replace(".enc", ".pdf")
    with open(temp_path, "wb") as f:
        f.write(decrypted_data)
    return temp_path

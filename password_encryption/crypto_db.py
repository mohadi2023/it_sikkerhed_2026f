import bcrypt
from cryptography.fernet import Fernet

# ---------------------------
# 1️⃣ Password hashing
# ---------------------------
def hash_password(password: str) -> bytes:
    """Hash et password med bcrypt"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed

def check_password(password: str, hashed: bytes) -> bool:
    """Tjekker om password matcher hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# ---------------------------
# 2️⃣ Kryptering af følsomme data
# ---------------------------
# Generer en nøgle (gem den sikkert!)
key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt_data(data: str) -> bytes:
    """Krypter data"""
    return fernet.encrypt(data.encode('utf-8'))

def decrypt_data(encrypted: bytes) -> str:
    """Dekrypter data"""
    return fernet.decrypt(encrypted).decode('utf-8')

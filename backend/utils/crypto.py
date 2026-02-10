import hashlib
from cryptography.fernet import Fernet

# Generate a key for encryption/decryption
# You may need to store this key securely!
key = Fernet.generate_key()
fernet = Fernet(key)


def encrypt_license(license_info: str) -> bytes:
    """Encrypt the license information."""
    return fernet.encrypt(license_info.encode())


def decrypt_license(encrypted_license: bytes) -> str:
    """Decrypt the license information."""
    return fernet.decrypt(encrypted_license).decode()


def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest() 


def verify_password(stored_password_hash: str, provided_password: str) -> bool:
    """Verify a provided password against the stored password hash."""
    return stored_password_hash == hash_password(provided_password)
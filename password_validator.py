# Password validator
def is_password_valid(password: str) -> bool:
    return 8 <= len(password) <= 16


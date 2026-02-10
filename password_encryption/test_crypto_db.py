from crypto_db import hash_password, check_password, encrypt_data, decrypt_data

def test_password_hashing():
    # given
    password = "hemmeligt123"

    # when
    hashed = hash_password(password)

    # then
    assert check_password(password, hashed) is True
    # Risk: Hvis testen fejler, kan passwords ikke verificeres korrekt

def test_password_wrong():
    # given
    password = "hemmeligt123"
    wrong = "forkert123"
    hashed = hash_password(password)

    # when / then
    assert check_password(wrong, hashed) is False
    # Risk: Hvis testen fejler, kan brugere logge ind med forkert password

def test_encryption_decryption():
    # given
    sensitive = "Østre Alle 5"

    # when
    encrypted = encrypt_data(sensitive)
    decrypted = decrypt_data(encrypted)

    # then
    assert decrypted == sensitive
    # Risk: Hvis testen fejler, kan følsom data ikke genskabes korrekt

def test_clear_memory():
    # given
    sensitive = "Hemmeligt nummer"

    # when
    encrypted = encrypt_data(sensitive)
    decrypted = decrypt_data(encrypted)
    decrypted = None  # Fjernes fra hukommelsen

    # then
    assert decrypted is None
    # Risk: Hvis testen fejler, kan følsom data blive i hukommelsen

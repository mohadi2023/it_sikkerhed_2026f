import pytest
from password_validator import is_password_valid

@pytest.mark.parametrize(
    "password,expected",
    [
        ("1234567", False),          # 7 tegn → fejl
        ("12345678", True),          # 8 tegn → OK
        ("1234567890123456", True),  # 16 tegn → OK
        ("12345678901234567", False) # 17 tegn → fejl
    ]
)
def test_password_length(password, expected):
    assert is_password_valid(password) == expected
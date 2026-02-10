from flat_file_db import add_user, get_user_by_id, disable_user

def test_add_user():
    # given
    user = {
        "person_id": 2,
        "first_name": "Peter",
        "last_name": "Larsen",
        "address": "Side Street",
        "street_number": 5,
        "password": "hashed_pw",
        "enabled": True
    }

    # when
    add_user(user)

    # then
    result = get_user_by_id(2)
    assert result is not None
    # Risk: Hvis testen fejler, kan brugere ikke oprettes


def test_user_not_found():
    # given
    person_id = 999

    # when
    result = get_user_by_id(person_id)

    # then
    assert result is None
    # Risk: Systemet kan give adgang til ikke-eksisterende brugere


def test_disable_user():
    # given
    person_id = 2

    # when
    disable_user(person_id)

    # then
    user = get_user_by_id(person_id)
    assert user["enabled"] is False
    # Risk: Deaktiverede brugere kan stadig logge ind

import json
import os

BASE_DIR = os.path.dirname(__file__)
DB_FILE = os.path.join(BASE_DIR, "users.json")


def load_users():
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=2)


def add_user(user):
    users = load_users()
    users.append(user)
    save_users(users)


def get_user_by_id(person_id):
    users = load_users()
    for user in users:
        if user["person_id"] == person_id:
            return user
    return None


def disable_user(person_id):
    users = load_users()
    for user in users:
        if user["person_id"] == person_id:
            user["enabled"] = False
            save_users(users)
            return True
    return False

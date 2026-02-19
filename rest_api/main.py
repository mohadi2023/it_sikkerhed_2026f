from fastapi import FastAPI
from flat_file_db.flat_file_db import add_user, load_users, get_user_by_id, disable_user

app = FastAPI()

@app.get("/")
def root():
    return {"message": "REST API virker"}

@app.get("/users")
def get_users():
    return load_users()

@app.post("/users")
def create_user(user: dict):
    add_user(user)
    return {"message": "User created"}
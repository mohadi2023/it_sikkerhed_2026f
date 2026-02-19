from fastapi import FastAPI, HTTPException
from jose import jwt
from datetime import datetime, timedelta
from password_encryption.crypto_db import check_password
from flat_file_db.flat_file_db import load_users

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

app = FastAPI()

@app.post("/login")
def login(credentials: dict):
    users = load_users()
    
    for user in users:
        if user["username"] == credentials["username"]:
            if check_password(credentials["password"], user["password"].encode()):
                
                token = jwt.encode(
                    {
                        "sub": user["username"],
                        "exp": datetime.utcnow() + timedelta(minutes=30)
                    },
                    SECRET_KEY,
                    algorithm=ALGORITHM
                )
                return {"access_token": token}

    raise HTTPException(status_code=401, detail="Invalid credentials")

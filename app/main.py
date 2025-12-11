from fastapi import FastAPI
from .auth_router import auth_router

app = FastAPI(title="Auth API with OTP")

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Auth API is running!"}

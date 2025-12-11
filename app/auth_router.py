from fastapi import APIRouter, HTTPException, Depends
from .models import UserCreate, UserLogin
from .database import users_collection
from .utils import hash_password, verify_password, create_access_token, create_refresh_token, generate_otp, send_otp_email
from bson import ObjectId

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

# SIGNUP 
@auth_router.post("/signup")
async def signup(user: UserCreate):
    # Check if email already exists
    existing = await users_collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create OTP
    otp = generate_otp()

    # Hash password
    hashed_password = hash_password(user.password)

    # Create user record
    user_doc = {
        "email": user.email,
        "password": hashed_password,
        "otp": otp,
        "is_verified": False
    }

    await users_collection.insert_one(user_doc)

    # Send OTP email
    send_otp_email(user.email, otp)

    return {"message": "Signup successful. OTP sent to email."}


# VERIFY OTP
@auth_router.post("/verify-otp")
async def verify_otp(email: str, otp: str):
    user = await users_collection.find_one({"email": email})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user["otp"] != otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    await users_collection.update_one(
        {"email": email},
        {"$set": {"is_verified": True}, "$unset": {"otp": ""}}
    )

    return {"message": "Email verified successfully!"}


# LOGIN
@auth_router.post("/login")
async def login(user: UserLogin):
    user_in_db = await users_collection.find_one({"email": user.email})

    if not user_in_db:
        raise HTTPException(status_code=404, detail="User not found")

    if not user_in_db["is_verified"]:
        raise HTTPException(status_code=401, detail="Email not verified")

    if not verify_password(user.password, user_in_db["password"]):
        raise HTTPException(status_code=401, detail="Incorrect password")

    # Create JWT tokens
    access_token = create_access_token({"id": str(user_in_db["_id"])})
    refresh_token = create_refresh_token({"id": str(user_in_db["_id"])})

    return {
        "message": "Login successful",
        "access_token": access_token,
        "refresh_token": refresh_token
    }

# Python FastAPI Email OTP Authentication API

A simple and secure authentication API built using **FastAPI + MongoDB + JWT + SMTP Email OTP**.

This project includes:
- User Signup
- OTP Email Verification
- Login with JWT Tokens
- MongoDB Database
- Clean Folder Structure
- Environment-based Configuration

---

##  Features

- Email-based OTP verification
- Hashed password storage
- JWT authentication
- MongoDB integration
- FastAPI backend
- Modular and scalable structure

---

##  Project Structure

```
app/
 ├── auth_router.py
 ├── config.py
 ├── database.py
 ├── models.py
 ├── utils.py
 ├── main.py
.env
requirements.txt
README.md
```

---

## Screenshots

### 1. Signup
<img width="1912" height="931" alt="Screenshot 2025-12-11 195526" src="https://github.com/user-attachments/assets/8a8665ef-a049-402b-857f-87ea720ec90c" />

### 2. Verify-Otp
<img width="1918" height="962" alt="Screenshot 2025-12-11 200834" src="https://github.com/user-attachments/assets/31869277-f3ab-48d7-8dc8-911fc7d7cfe1" />

### 3. Login
<img width="1917" height="972" alt="Screenshot 2025-12-11 201111" src="https://github.com/user-attachments/assets/154fa89b-2064-496f-83a3-c10be34d55e5" />



##  Installation

### 1. Clone the project
```
git clone https://github.com/DayanandSurwase/Email-OTP-Authentication-System-FastAPI-
cd auth-api
```

### 2. Create virtual environment
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install packages
```
pip install -r requirements.txt
```

---

## Create `.env` File

Create a file named `.env` in the project root:

```
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=auth_system

JWT_SECRET=your_secret_key
JWT_ALGORITHM=HS256

SMTP_EMAIL=yourgmail@gmail.com
SMTP_PASSWORD=your_app_password
```

---

## Run the API

```
uvicorn app.main:app --reload
```

API will be live at:

 - http://127.0.0.1:8000  
 - Swagger Docs: http://127.0.0.1:8000/docs

---

##  Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/signup | Create user & send OTP |
| POST | /auth/verify-otp | Verify OTP |
| POST | /auth/login | Login with password |
| GET | /auth/protected | Test JWT |

---

##  License
MIT

---

## Contribute
Feel free to fork and improve this project!

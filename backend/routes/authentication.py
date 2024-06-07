# route/authentication.py
from fastapi import APIRouter, HTTPException
from models.AuthModel import AuthRequest
import requests
import jwt

router = APIRouter()

GOOGLE_CLIENT_ID = ""
GOOGLE_CLIENT_SECRET = ""
GOOGLE_REDIRECT_URI = "http://localhost:3000"
SECRET_KEY = ""  # Secret key for JWT token

@router.post("/authenticate")
def authenticate(auth_request: AuthRequest):
    token_url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "code": auth_request.code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to authenticate")
    
    access_token = response.json().get("access_token")
    if not access_token:
        raise HTTPException(status_code=400, detail="Access token not received")

    user_info_response = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
    if user_info_response.status_code != 200:
        raise HTTPException(status_code=user_info_response.status_code, detail="Failed to fetch user info")
    
    user_info = user_info_response.json()

    # Generate JWT token
    #jwt_token = jwt.encode(user_info, SECRET_KEY, algorithm="HS256")

    # Here you can save the JWT token to a database or use it as a session token
    # For demonstration purposes, let's return it in the response
    #return {"session_token": jwt_token}
    return user_info

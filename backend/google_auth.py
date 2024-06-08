import os
from google.oauth2 import id_token
from google.auth.transport import requests

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from google.oauth2 import id_token
from google.auth.transport import requests
import time
from dotenv import load_dotenv

load_dotenv()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
google_client_id = os.getenv("GOOGLE_CLIENT_ID")


def validate_token(token: str):
    """Validates Google ID token and checks expiry."""
    try:
        print("token: ", token)
        print("GOOGLE_CLIENT_ID: ", google_client_id)
        idinfo = id_token.verify_oauth2_token(
            token, requests.Request(), google_client_id
        )

        print("idinfo: ", idinfo)

        # Check issuer
        if idinfo["iss"] not in ["accounts.google.com", "https://accounts.google.com"]:
            raise ValueError("Wrong issuer.")

        # Check expiry (exp is in Unix timestamp format)
        current_time = int(time.time())
        if current_time > idinfo["exp"]:
            raise ValueError("Token expired.")

        # Extract user information
        user_info = {
            "user_id": idinfo["sub"],
            "email": idinfo["email"],
            # ... other relevant user data
        }

        print("user_info: ", user_info)

        return user_info
    except ValueError as e:
        print("ValueError: ", e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def authenticate(access_token):
    """
    Authenticates the user with the provided Google access token.
    If successful, returns the user's information.
    """
    try:
        user_info = validate_token(access_token)
        return {"success": True, "user_info": user_info}
    except HTTPException as e:
        # If the token is invalid or expired, raise the exception to be handled by FastAPI
        raise e
    except Exception as e:
        # Catch any unexpected errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Authentication failed due to an internal server error.",
        )

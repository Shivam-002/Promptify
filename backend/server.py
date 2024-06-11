from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# from routes.chat import router as chat_router
from routes.query import router as query_router

from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost:3000/",
    "https://localhost:3000/",
    "promptify-psi.vercel.app",
]


CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


# @app.middleware("http")
# async def verify_google_token(request: Request, call_next):
#     print("Request : ", request)
#     print("Headers : ", request.headers)
#     authorization: str = request.headers.get("Authorization")
#     print("Auth : ", authorization)
#     if not authorization:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Authorization header is missing",
#         )

#     token = authorization.split(" ")[1]

#     try:
#         # Use the 'credential' field directly as the ID token
#         idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

#         if idinfo["iss"] not in ["accounts.google.com", "https://accounts.google.com"]:
#             raise ValueError("Wrong issuer.")

#         user_id = idinfo["sub"]
#         request.state.user_id = user_id
#     except ValueError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     print("Authorized User...")
#     response = await call_next(request)
#     return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_router, prefix="/api/v1/query", tags=["Query"])


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):

    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": f"{exc.detail}"},
    )

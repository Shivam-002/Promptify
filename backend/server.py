from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from routes.authentication import router as auth_router
from routes.query import router as query_router

app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(query_router, prefix="/api/v1/query", tags=["Query"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):

    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": f"{exc.detail}"},
    )

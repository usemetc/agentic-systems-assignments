from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

# This line MUST be here for Uvicorn to find the app
app = FastAPI()

# 1. Middleware for Logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Before request: {request.method} {request.url.path}")
    response = await call_next(request)
    print(f"After request: {response.status_code}")
    return response

# 2. Hello Route
@app.get("/hello")
async def hello():
    return {"message": "Hello, Welcome to FastAPI!"}

# 3. Custom 404 Exception Handler
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={"message": "The requested resource was not found"},
    )
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "E-commerce System", "Status": "Online"}
    
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/search")
def search_user(name: Optional[str] = None, age: Optional[int] = None):
    # This dictionary will be returned as JSON
    return {
        "status": "Search Results",
        "received_name": name,
        "received_age": age,
        "query_provided": name is not None or age is not None
    }
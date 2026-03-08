from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Root endpoint so you don't get a 404
@app.get("/")
def home():
    return {"message": "Server is running! Go to /docs to test the search."}

# The Search Endpoint
@app.get("/search")
def search_user(name: Optional[str] = None, age: Optional[int] = None):
    # Returns the inputs back to the web browser as JSON
    return {
        "status": "Success",
        "data_received": {
            "name": name,
            "age": age
        }
    }
@app.get("/")
def home():
    return {"message": "Welcome to the API! Go to /docs for the interactive UI."}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
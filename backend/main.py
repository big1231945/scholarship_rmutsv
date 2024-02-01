from fastapi import FastAPI
from app.API import api
import uvicorn
app = FastAPI()

app.include_router(api.router, prefix="/admin",
                   tags=["Admin"],
                   responses={404: {"description": "Not found"}})


if __name__ == "__main__":
    uvicorn.run(app=app, port=8000)
    # uvicorn main:app --reload

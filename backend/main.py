from fastapi import FastAPI ,APIRouter
import uvicorn
app = FastAPI()






if __name__ =="__main__":
    uvicorn.run(app=app,port=5700)

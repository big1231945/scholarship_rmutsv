from fastapi import APIRouter, Depends,UploadFile
from app.Security import JWT
from .schemas import schemas
from ..Database.ConnectDB import SessionLocal
from . import crud
from sqlalchemy.orm import Session
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create_from")
def create_from(form: schemas.FormCreate, db: Session = Depends(get_db)):
    crud.create_from(db=db, form=form)


@router.delete("/delete/{id}")
def delete_from(id: int, db: Session = Depends(get_db)):
    crud.delete_form(db=db, id=id)


@router.get("/all", response_model=list[schemas.Student])
def all(db: Session = Depends(get_db)):
    data = crud.get_all(db=db)
    return data


@router.get("/filter_time", response_model=list[schemas.Student])
def get_data_by_time(time: schemas.TimeBetween, db: Session = Depends(get_db)):
    data = crud.filter_time(db=db, start=time.start, end=time.end)
    return data


@router.put("/update/{id}")
def update(id: int, data: dict, db: Session = Depends(get_db)):
    crud.update(db=db, data=data, id=id)


@router.post("/login/{username}")
async def login(username: str):
    access_token = JWT.create_access_token(data={"sub": username})
    return JWT.Token(access_token=access_token, token_type="bearer")


@router.post("/decode")
async def decode_test(data: dict):
    data = JWT.decode_access_token(
        token=data['token'], username=data["username"])
    
@router.post("/uploadfile/")
async def update_file(file:UploadFile):
    return file.filename


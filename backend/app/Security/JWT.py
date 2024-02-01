from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import timedelta, datetime, timezone
from pydantic import BaseModel

SECRET_KEY = "sdafsdKLJGIKJHFo328974IUisduhfygefuew92384uhdgevYUGF334JDGHgUekUYFGfygYFGKJYGGjyg38725"
ALGORITHM = "HS256"
ACCESS_TOKENEXPIRE_HOUR = 12

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Token(BaseModel):
    access_token: str
    token_type: str


def create_access_token(data: dict, expries_delta: timedelta | None = None):
    to_encode = data.copy()
    if expries_delta:
        expries = datetime.now(timezone.utc)+expries_delta
    else:
        expries = datetime.now(timezone.utc) + timedelta(hours=15)
    to_encode.update({"exp": expries})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str, username: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        data = jwt.decode(token=token, algorithms=ALGORITHM, key=SECRET_KEY)
    except JWTError:
        raise credentials_exception
    print(data)
    if username != data["sub"]:
        raise HTTPException(detail="แก่ไม่มีสิทธิ์ มาเรียกฉันว่าพ่อ!",
                            status_code=status.HTTP_401_UNAUTHORIZED)
    return data

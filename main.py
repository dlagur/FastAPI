from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, get_db
from models import User

# 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 서버 URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    """
    Fetch all users from the database and return as JSON.
    """
    users = db.query(User).all()
    user_list = [
        {"id": user.id, "name": user.name, "phone": user.phone, "age": user.age, "job": user.job}
        for user in users
    ]
    return JSONResponse(content={"users": user_list})

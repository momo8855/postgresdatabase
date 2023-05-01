from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import cursor, conn
from .config import settings

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    cursor.execute("""SELECT * FROM pg_settings WHERE name = 'port' """)
    posts = cursor.fetchall()
    print(type(posts))
    print(posts)
    return {"Hello World"}